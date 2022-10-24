Hello, and welcome to the readme for my goofy little program!
This program is intended to be able to automatically reset a persona fusion in Persona 3 FES and determine what skills it has and whether or not it should be kept.
I wrote this in PyCharm in about a week and with no experience in programming at all, so there are likely more efficient ways to do what this does.
I have not tested the program in Persona 3 Original and Persona 3 Portable, but I would assume that it should also work for those games if you set it up correctly.
This program works by taking a screenshot of the game window in an emulator, then using an OCR to read the screenshot and determine what skills it has.
As I mentioned, I have no experience with programming, so there is no UI at all.
Everything will need to be input directly into the program, so you will need an IDE that can both edit and run python projects.
I have inlcuded comments in the code to hopefully explain everything that would need to be done, but I expect it may not be comprehensive enough.
I may work on adding a UI and properly packing the program into an executable file, but that is for another day.
If you run into any issues, try to contact me on GitHub if at all possible.
I'm not very familiar with its workings, but hopefully it should work.

Before using this program, I would suggest viewing [the Big Guide on GameFAQs](https://gamefaqs.gamespot.com/ps2/932312-shin-megami-tensei-persona-3/faqs/49926)
I would specifically recommend looking at section 5b and reading the note on **Skill Ranks**, as they are incredibly important when trying to get very high ranking skills onto a persona.
Additionally, [this github page](https://aqiu384.github.io/megaten-fusion-tool/p3fes/personas) is extremely useful when trying to find a path to fuse down for a specific persona.


# To use the program, create a new project file in your python IDE and import the required libraries.
I have been having trouble with uploading the entirety of the project, so the best way to use this yourself is to create a new project in your IDE, import the .py file into the folder, and then import the libraries to finish the installation.

The required libraries for this project are easyocr, pynput, and pyautogui. The install commands are as follows

`pip install easyocr`

`pip install pynput`

`pip install pyautogui`

Additionally, you can use the project settings in PyCharm to add the packages to the interpreter. Searching for the packages by name should come up with only a few results, so it should be somewhat simple once you find the window.

![An example image of how the array for skills is laid out when fusing](/SkillExample.png)

Above is how the skills should be numbered when editing them in line 68. In this example, skills 1, 3, 5 & 6 are the inherited skills, so the line should read `step2 = step1[[1, 3, 5, 6], [1, 1, 1, 1]]`



Also, in case you're wondering, TheGrinder is my pet name for the project.
I named it as such since it reminds me of the monster grinder from Backyard Monsters, which is a very specific reference from a few years ago.
