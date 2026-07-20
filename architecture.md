# Instant Pathfinder: Agentic Architecture Planning

This document serves as a workspace for brainstorming and planning the multi-agent system that will generate Pathfinder 2e adventure modules. 

## 1. Architecture Paradigm: GraphFlow

The app will make use of GraphFlow in the AgentChat API from Microsoft's AutoGen, which will allow for a stateful, multi-agent conversation. Custom 
agents will be created for each stage and process of the adventure generation pipeline using ChromaDB to store conversation history and metadata. The 
agents will have access to tools to facilitate their work as needed such as querying an SQLite database of Pathfinder 2e rules and data. The primary model will be an Ollama local LLM.

## 2. The Process of Generating an Adventure Module

### Definitions

1. An adventure module is defined as a quest with a number of encounters for which the experience point total is 1000 (the experience required to gain a single level) and the total treasure is equal to the recommended treasure by level for a party of X characters of Y level.
2. There is a GM and X player characters. The default value for X is 4. The generator will handle adjustments in balance for different values of X.
    1. The GM guides the players through the quest through descriptions of the environment and NPCs provided by the generator based on the quest, adjudicating the results of the player characters' actions, and describing the results of each encounter and each scene.
    2. The player characters are level Y. The default value for Y is 1. The generator will handle adjustments in balance for different values of Y.
3. A quest is defined as a story that follows the three act structure. The three acts are defined as follows:
    1. Act I: The Setup. This act introduces the characters, the setting, and the conflict.
    2. Act II: The Confrontation. This act builds on the conflict introduced in Act I and escalates the stakes.
    3. Act III: The Resolution. This act resolves the conflict introduced in Act II and provides a sense of closure.
5. Each act has a number of scenes. A scene is defined as an encounter that takes place within a single location.
    1. The number of scenes is the minimum number of encounters required to advance the plot in a meaningful way for that act.
    2. A scene establishes the location based on the needs of the quest and the preceding encounter, introduces the encounter, and provides a resolution for that encounter.
    3. A scene is resolved once the encounter is resolved. The scene resolution follows the encounter resolution and describes the immediate consequences of the encounter.
    4. Each scene builds upon the previous scene just as each act builds upon the previous act.
    5. Not every scene is in a new location, some scenes may take place in the same location as a preceding scene, such as in a dungeon where multiple events might happen, or an already visited location.
6. The locations of scenes are collectively known as a region. A region is a geographic area that contains settlements such as villages, towns, and cities, as well as natural locations such as forests, mountains, rivers, and dungeons.
    1. The region is defined by the milieu, themes, and setting of the quest. For example, an urban fantasy quest might take place in a region that includes a number of city districts, underground tunnel networks, and abandoned buildings. A high fantasy quest might take place in a region that includes a number of villages, towns, cities, forests, mountains, rivers, and dungeons.
    2. A region should contain a number of settlements and natural locations roughly proportional to its size and the scope of the quest. So a quest taking place in a small rural area might contain only a single village and a few surrounding natural locations, while a quest taking place in a large city might contain a number of different districts and a small number of surrounding natural locations (if any).
    3. A region may not include any settlements or natural locations depending on the quest. For instance, a quest that takes place entirely within a city might not include any natural locations, while a quest that takes place entirely within a dungeon might not include any settlements or natural locations.
7. A scene's location must make sense in the context of the region, the preceding scene, the encounter within the scene, the anticipated next scene, and the overall quest structure.
    1. A location can be of any size, from a single room in a dungeon or building, to an entire building such as an inn or shop, to a district within a town or city, to an entire town or city, to a wilderness area.
    2. The size of a location should be appropriate for the encounter taking place. For example, a social encounter might take place in a single room, while a combat encounter might take place in a large room (or multiple connected rooms/areas). A skill challenge might take place in a location that is either large or small depending on the nature of the challenge. For example, a skill challenge to disarm a trap might take place in a room, while a skill challenge to evade capture might take place in a city district or wilderness area.
    3. The location of a scene should make sense in the context of the region. For example, a quest taking place in a small rural area should not have a scene that takes place in a large city. A quest taking place in a city should have a location that is appropriate for the scene.
8. An encounter is defined as a combat encounter, a social encounter, a skill challenge, or a hazard.
    1. When an encounter is created its type is chosen based on the needs of the scene and its place in the story. So the first scene of Act I will almost always be a social encounter, while the last scene of Act III will almost always be a combat encounter.
        1. Combat encounters involve enemy creatures appropriately chosen from a database table of Pathfinder 2e creatures. Combat encounters are resolved once all enemies are dead, incapacitated, or have fled.
        2. Social encounters involve NPCs created for the needs of the quest. Social encounters have an objective and is resolved once the NPCs have been influenced in a way that meets the objective. The objective is determined by the quest.
        3. Skill challenges involve a series of skill checks that must be completed to overcome an obstacle or series of obstacles. Obstacles are described by the quest, but compared against the available skill data within the database to create the actual skill challenge. The skill challenge is resolved once the obstacle or obstacles have been overcome.
        4. Hazards are similar to skill challenges, but they are traps that must be disarmed or avoided. Hazards are predefined in the database, but which hazard to use is determined by the quest by selecting the most relevant one. A hazard is resolved once the players have successfully disarmed or avoided the hazard.
    2. An encounter's level begins as equal to the party's level. 
    3. Encounters have five threat levels: Trivial, Easy, Moderate, Severe and Extreme. Threat levels modify the encounter level. The threat level is determined by the encounter's place in the story with Act I encounters tending toward lower threat levels (Trivial or Easy), Act II encounters tending toward higher threat levels (Easy, Moderate, or Severe), and Act III encounters tending toward the highest threat levels (Severe or Extreme).
    4. Encounters have rewards measured in experience points and treasure determined by the final encounter level.
    5. Encounters can involve a number of different checks such as perception checks (what player characters are aware of), skill checks (what player characters do) and save checks (how well player characters respond to sudden events). There are two types of Difficulties for checks: level and simple.
        1. Level DCs are determined by a table in the database based on the party's level.
            1. An example of a Level DC is a skill challenge, wherein difficulties are set by the party's level.
        2. Simple DCs are determined contextually based on the type of check and the expected level of training required to accomplish it. 
            1. An example of a Simple DC is a locked door. But in this case, the locked door would not have a difficulty set by the party's level, but rather contextually based on the type of check (unlocking a door) and the expected level of training from the Trainings table in the database. A mundane locked door would have a DC of 15 (Trained). If, however, the story described the door as being made of adamantine and being locked with a complex arcane mechanism, the difficulty would instead be 30 (Master).
9. Non-player characters or NPCs used in scenes are collectively known as the cast.
    1. Some NPCs will appear in multiple scenes throughout the quest, such as in a town where the PCs may need to interact with the same NPCs in different scenes. The generator should keep track of the NPCs it has created and the scenes they appear in, so that they can be consistently represented throughout the quest.
    2. Some NPCs may only appear for a single scene.
    3. When creating an NPC, the generator will use the following attributes: Name, Ancestry, Class or Profession, Skills and Level. These attributes will be used to determine the NPC's behavior and abilities.
    4. The size of the cast should be the minimum number of characters required to serve the needs of the quest, but never less than one. The size of the cast should be appropriate for the quest. So a quest taking place in a small rural area might have a cast of only a few NPCs, while a quest taking place in a large city might have a cast of a dozen or more NPCs.
    5. The cast should be diverse and interesting, with a variety of ancestries, classes and professions. The cast should also be appropriate for the quest. So a quest taking place in a small rural area should have a cast of characters that are appropriate for that area. A quest taking place in a city should have a cast of characters that are appropriate for that city.
    6. The cast should be consistent throughout the quest. So if an NPC is created for a specific scene, they should be represented consistently throughout that scene. If an NPC appears in multiple scenes, they should be represented consistently throughout all of the scenes they appear in.
    7. Not every scene needs a cast member; some scenes may have no cast members at all. For example, a combat encounter might not have any cast members, while a social encounter might have several.