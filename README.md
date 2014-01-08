Instant Pathfinder (Working Name)
=================

This will house the development of the Pathfinder Module Generator.


GOAL: To create and develop a module generator for Pathfinder.

A Module is defined, in this usage, as a simple adventure typically consisting of a single quest wherein a party of adventurers perform a task for a reward. Generally a Module contains a settlement, a dungeon, a number of NPCs, a quest and treasure.

There are several different types of generators out there - name, npc, monster, treasure and even dungeon generators - out there and yet no one has brought these together into a unified product that can be used to create a complete adventure module. This is what we intend to do.

PHASE I: Project Scoping

So far, we have identified these elements that exist in a standard Adventure Module:

	1. A Settlement or Starting Location
	2. A Quest or Other Goal to Accomplish
	3. A Dungeon or Quest/Goal Location
	4. A Resolution or Reward

These are simply the bare necessities of a module. How these are implemented still need to be decided. Currently we've been brainstorming what we 'could' implement:

	1. NPC generator (including NPC class levels or PC class levels depending upon PC level and NPC's relationship to quest)
	2. Settlement generator
	3. Dungeon generator
	4. Monster generator
	5. Treasure generator
	6. Front end customization controls:
		- Party Level
		- Party Size
		- PC Classes
		- Settlement Size
		- Settlement Region (Desert, Jungle, Plains, Coast, etc)
		- Dungeon Size
		- Dungeon Difficulty
		- Reward Level
	
	Additional thoughts:
	
	1. Weather/Atmosphere generator
	2. Base Settlement size on PC level
	3. Assign every NPC to a building in generated Settlement
	4. PC Generator (based on archetypes)
	5. An "intelligent" treasure generator that if it rolls up a weapon, armor or scroll ensures that its usable by a member of the party
	6. Base monster generation off of regional location, or when generating monsters, only pick ones from the same region so you don't get Ice golems and Fire Elementals in the same building
	7. Flavor text generation. I want this to feel as much like a hand written module as possible.
	
To complete project scoping, we'll need to determine all of the variables we want to incorporate into the alpha version and create a process by which we can introduce new elements into future versions.

Next Steps:

	1. Research Existing Modules
		- Look for any and all Pathfinder Modules
		- See what they include and don't include
		- Get a feel for they all share in common
	2. Draft up ideas for Random Elements and how we could implement them
	3. Research existing random tables and charts
	4. Collect it all and then we'll have a discussion over what we can/should include

Obviously we aren't going to accomplish this all in one day, but I believe that for the alpha build, we can at least get to a playable state.

PHASE II: Element Design

Once we have determined what elements to include in the alpha build, we can begin the process of designing our random algorithms. Some will be simple as there are tables for pathfinder already in existence, but others will be a bit more difficult.

Exploration of other content generators will be crucial at this stage as we don't want to go about reinventing the wheel.

PHASE III: PoC Development

At this stage we will begin development of the individual random elements as a sort of proof of concept. Why are we doing this instead of creating it all in one go? Well I'd like the Module Generator to be... well... modular.

That is as new random elements are designed, they can be dropped in or incorporated into the overarching design quickly and easily.

To that end, once we've proven that we're randomly generating content we move to Phase IV.

PHASE IV: Framework Design

In order to combine our disparate elements, we'll need some kind of Framework to carry it all together. At this phase we'll design such a Framework and figure out how to marriage multiple elements together.

We should also to take care to remember our two ends: The first is a simple web front end that can control the internal elements and the second is the HTML or PDF output at the other end.

PHASE V: Framework Development

Once we have defined how all the random elements will talk to each other we can begin development on the actual Framework.

PHASE VI: Element Implementation

At this stage we'll go back and review and test our random elements and check for efficiency and adaptability. Once they're ready we'll plug them into our framework and move onto the next phase.

PHASE VII: Module Testing

We'll need to do everything we can to break the generator, throw as much crap into it as possible

PHASE VIII: Framework and Element Clean UP

After testing is clean up. Simple as that.

PHASE IX: Securing

The last thing we need is to stand up something that is easily hacked and destroyed, so once we have our generator up and running we'll batten down the hatches

PHASE X: Launch

At this point we should be ready to launch. We'll purchase a domain and hosting, and pray that we did everything right