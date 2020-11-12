# Trails of Cold Steel Randomizer

## Latest Version: [1.0.0](https://github.com/nnguyen259/ColdSteelRandomizer/releases/tag/1.0.0)

## Experimental Version: [1.1.0-beta](https://github.com/nnguyen259/ColdSteelRandomizer/releases/tag/1.1.0-beta)

## Introduction

Hello, I am nnguyen259, although you might have seen me with the name hell259 elsewhere (most notably Reddit and Discord). Cold Steel 1 was my introduction to Trails series and needless to say, it is very special to me. I started learning to mod Cold Steel 1 back in 2018, after seeing SoftBrilliant's [Difficulty Mod](https://www.reddit.com/r/Falcom/comments/c0o756/cs1_difficulty_pack_v12/) (He is an awesome guy, and is working on all sort of rebalance patches for other Trails games as well).

This project has been in the work since the start of Summer 2020, although I first thought about it way earlier. And with the events happened in 2020, I finally have the time to transform my thoughts into reality. I am glad to finally be able to release it. Hopefully you will have a good time replaying Cold Steel 1 with this.

## Installation

The list of releases can be found here: https://github.com/nnguyen259/ColdSteelRandomizer/releases

Currently only binary for Windows is available. I do not own a Mac and Linux is not something I have a good grasp on, so Windows only for now. If you would like to build the binary yourself from the source code, feel free to go ahead. Personally I use [cx_Freeze](https://cx-freeze.readthedocs.io/en/latest/) to create the Windows binary.

## Usage

The randomizer will only work with the English release of Cold Steel 1 due to how the files are structured.

Usage otherwise is pretty straightforward. After you have downloaded and launched the application, you will be greeted by this window:

![](https://cdn.discordapp.com/attachments/588527782674432013/776477326564524112/UI.png)

The Game Location is the folder where the game .exe is located.

Before attempting to randomize the game, it is recommended that you make a back of the folders `text` and `scripts` inside the `data` folder. You can also verify the integrity of the game files from Steam to restore the game to its original state.

After picking the seed (optional) and the options you want. Press Randomize! to begin the process. It might take a bit for the randomizer to finish, afterwards a dialogue will be shown and the results will be saved to `result.txt` file in the same folder as the randomizer.

## Randomizer Options
### Character
* **Base Stat and Stat Growth:** Randomize the starting stat and stat growth for every character, including Sara and Angelica. The higher the variance, the more random it gets.
* **Crafts:** Randomize the craft pool for every character. The character will still have the same amount of total crafts and the level learn for those crafts, but the actual craft pool will be different. However, they will still use their old animation as if they are using their original crafts. Therefore, it is possible that crafts might not work as expected due to the interaction with the animation.

### Orbment Options
* **Orbment Line:** Create a new orbment line for each character and randomly assign slots to have an elemental lock.
* **Base EP and EP Growth:** Each character will have a different starting amount of EP as well as the amount of EP gain when opening an orbment slot.

### Enemy Options
Note: Playble characters as enemies will not be randomized.
* **Enemy Stats:** Randomize enemy main four stats (STR, DEF, ATS, ADF). If the enemy has 0 ATS, it will not be changed. The higher the variance, the more random it is.
* **Enemy Elemental/Affliction/Unbalance Efficacy:** Generate new values for these efficacy for each enemy.

## TODO List
* Optionally prevent Petrify/Deathblow/Vanish Efficacy from being randomized (coming 1.1)
* Shuffle Master Quartz Locations (coming 1.1)
* More to come...

## Special Thanks
* SoftBrilliant and the Modding Community for help with testing.