Instant Pathfinder (Working Name)
=================

This will house the development of the Pathfinder 2e Module Generator.


GOAL: To create and develop a module generator for Pathfinder 2e.

A Module is defined, in this usage, as a simple adventure typically consisting of a single quest wherein a party of adventurers perform a task for a reward. Generally a Module contains a settlement, a dungeon, a number of NPCs, a quest and treasure.

There are several different types of generators out there - name, npc, monster, treasure and even dungeon generators - out there and yet no one has brought these together into a unified product that can be used to create a complete adventure module. This is what I intend to do.

So far, I have identified these elements that exist in a standard Adventure Module:

	1. A Settlement or Starting Location
	2. A Task to Accomplish
	3. NPCs to Provide Information, Obstacles or Hooks
	4. A Dungeon or Task Location
	5. A Resolution or Reward

These are simply the bare necessities of a module. The ultimate goal is to utilize local LLM prompt engineering and hard coded random tables to create a fun, playable, and unique adventure every time you click a button.

CURRENT PROGRESS: I've extracted some of the basic Pathfinder 2e elements such as ancestries, classes, items, and creatures into JSON
files which will eventually be imported into an SQLite database. The next step will be to construct metadata JSON objects such as level-
based difficulties and other useful rules and tables.