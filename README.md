# Trails of Cold Steel Randomizer

## Latest Version: [1.3.0](https://github.com/nnguyen259/ColdSteelRandomizer/releases/tag/1.3.0)

## Experimental Version: None

## Introduction

Hello, I am nnguyen259, although you might have seen me with the name hell259 elsewhere (most notably Reddit and Discord). Cold Steel 1 was my introduction to Trails series and needless to say, it is very special to me. I started learning to mod Cold Steel 1 back in 2018, after seeing SoftBrilliant's [Difficulty Mod](https://www.reddit.com/r/Falcom/comments/c0o756/cs1_difficulty_pack_v12/) (He is an awesome guy, and is working on all sort of rebalance patches for other Trails games as well).

This project has been in the work since the start of Summer 2020, although I first thought about it way earlier. And with the events happened in 2020, I finally have the time to transform my thoughts into reality. I am glad to finally be able to release it. Hopefully you will have a good time replaying Cold Steel 1 with this.

## Installation

The list of releases can be found here: https://github.com/nnguyen259/ColdSteelRandomizer/releases

Currently only binary for Windows is available. I do not own a Mac and Linux is not something I have a good grasp on, so Windows only for now. If you would like to build the binary yourself from the source code, feel free to go ahead. Personally I use [cx_Freeze](https://cx-freeze.readthedocs.io/en/latest/) to create the Windows binary.

## Usage

The randomizer will only work with the English release of Cold Steel 1 due to how the files are structured.

Usage otherwise is pretty straightforward. After you have downloaded and launched the application, you will be greeted by this window:

![](https://media.discordapp.net/attachments/785577919904219197/795839395390816306/unknown.png?width=804&height=676)

The Game Location is the folder where the game .exe is located.

Before attempting to randomize the game, it is recommended that you make a back of the folders `text` and `scripts` inside the `data` folder. You can also verify the integrity of the game files from Steam to restore the game to its original state.

After picking the seed (optional) and the options you want. Press Randomize! to begin the process. It might take a bit for the randomizer to finish, afterwards a dialogue will be shown and the results will be saved to `result.txt` file in the same folder as the randomizer.

## Randomizer Options
### Character
* **Base Stat and Stat Growth:** Randomize the starting stat and stat growth for every character, including Sara and Angelica. The higher the variance, the more random it gets. Increase Base Stat option will give every character an extra 300 HP and 30 DEF at the start of the game.
* **Crafts:** Randomize the craft pool for every character. The character will still have the same amount of total crafts and the level learn for those crafts, but the actual craft pool will be different. However, they will still use their old animation as if they are using their original crafts. Therefore, it is possible that crafts might not work as expected due to the interaction with the animation.
* **Original Crafts:** Only enabled when randomized craft is also enabled. These crafts are all original from me (nnguyen259) or player submitted. To submit your own craft, go [here](https://forms.gle/dxvDuajCURGcbGda6).

### Orbment Options
* **Orbment Line:** Create a new orbment line for each character and randomly assign slots to have an elemental lock.
* **Base EP and EP Growth:** Each character will have a different starting amount of EP as well as the amount of EP gain when opening an orbment slot.

### Master Quartz and Chests Options
* **Reshuffle Master Quartz:** Each master quartz will take place of another master quartz, including starting master quartz, shop, chest, and special master quartz (Chevalier, Thor, Emblem, ...)

* **Normalize Master Quartz:** Make sure that late game master quartz (Vermillion, Thor, etc...) will have their effects even at lv1 with some rebalance done so that they are appropriate for the level.

* **Randomize Master Quartz Arts:** Randomize the art(s) each master quartz give per level (up to 2). The chance for getting an art will be rolled separatedly so you can end up with 0, 1, or 2 arts per master quartz level.

* **Shuffle Chests:** Randomly shuffle the contents of every chest in the game with the exception of the first Needle Shoot chest, Master Quartz chests and Sepith chests. There are three mode:

    1. Separated Pools: The contents of each type of chest (Normal, Rare and Monster) can only be shuffled into the same type of chest. 

    2. Combine Rare and Monster: Rare and Monster chests will share the same pool.

    3. Combine Everything: Every chest will be treated the same.

### Enemy Options
Note: Playble characters as enemies will not be randomized.
* **Enemy Stats:** Randomize enemy main four stats (STR, DEF, ATS, ADF). If the enemy has 0 ATS, it will not be changed. The higher the variance, the more random it is.
* **Enemy Elemental/Affliction/Unbalance Efficacy:** Generate new values for these efficacy for each enemy. There is an option to prevent Petrify/Deathblow/Vanish efficacy from being randomized.
* **Enemy Drops:** Randomize enemy drops. U-Material will not be changed. If "Keep Drop in Same Category" is enabled, randomized drop will be in the same category as normal drop. Otherwise, it will be a random armor/boots/accessory/quartz/consumables/materials.

### Misc. Options
* **Resources Gain:** These are options to increase the amount of EXP, Sepith, Sepith Mass after the battle as well as reduce the amount of Sepith needed to unlock character orbment slots. Helpful since you can easily end up with multiple characters having long orbment line or when you want to minimize battles.

* **La Forte:** Replace the Needle Shoot quartz with La Forte in Prologue. Helpful to go through the game faster.

* **Cookbook:** Shuffle which item will be the normal, good, peculiar and unique result of the recipe. Also shuffle which character will cook the "unique" result.

## Bugs
* Petrifying Phase 1 of Prologue Boss then instant kill will softlock the game.
* Wild Card can soft lock the game under various circumstances.

## TODO List
* More crafts.
* Shop?
* I'm open for suggestions

## Special Thanks
* SoftBrilliant and the Modding Community for help with testing.
* ChampionBeef for playing and providing feedback.
