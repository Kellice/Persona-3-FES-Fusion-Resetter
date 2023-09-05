import easyocr
from pynput.keyboard import Key, Controller
import time
import numpy as np
import pyautogui

reader = easyocr.Reader(['en'], gpu=False)
keyboard = Controller()
# This line initialises the OCR for reading the skills and the keyboard variable for inputs
# If you have a GPU in your system that is good, you can set the gpu argument
# in the first line to "True" to increase processing speed

#Verbose will print extra information, mostly things for debugging
verbose = True

# TODO define functions for the code
def pressButton(button):
    """
    Press a button on the keyboard the release it
    :param button: the button to be pressed
    :return: None
    """
    keyboard.press(button)
    time.sleep(.15)
    keyboard.release(button)
    time.sleep(.35)

#TODO Initialize all variables

# Key binds
circle = 'z'
cross = 'x'

wantedSkills = ["Spell Master", "Repel Dark", "Black Viper", "Mind Charge"]
unwantedSkills = ["Marin Karin", "Eerie Sound", "Eerie_Sound"]
numInnateSkills = 2
numInheritSkills = 3
numTotal = numInnateSkills + numInheritSkills
numRightHandSide = numTotal - 4

skillLocations = []
# add an index for every skill
for i in range(numTotal):
    skillLocations.append(i)
idx = 0
# remove innate skills from being read
for i in range(numInnateSkills):
    # Remove from front
    skillLocations.pop(idx)
    # Check if there is a skill on the right to skip
    if numRightHandSide > 0:
        idx += 1
        numRightHandSide -= 1
oneList = []
for i in range(len(skillLocations)):
    oneList.append(1)

if verbose:
    print('The array for skill locations:' + str(skillLocations))

# This pauses the program for a moment to allow you to tab over to the emulator
time.sleep(4)
# After that it initialises the "wrong" and "correct" variables so the while loop won't immediately break
correct = 0
wrong = 1
while correct < 4 or wrong > 0:
    # This loop keeps the program resetting as long as you do not have the skills you want
    # Set the correct < x to the amount of skills you want to inherit, and wrong > x to
    # the maximum amount of unwanted skills you will allow
    #TODO Edit for fes not allowing personas to be easily put in slots 1 and 2
    # @Kelli I edited your code to use a function to make it look clear and more readable
    pressButton(circle)
    pressButton(circle)
    pressButton(cross)
    pressButton(cross)
    time.sleep(0.4)
    # This runs through the inputs to reset a persona
    # The current inputs have "Circle" bound to "d" and "Cross" bound to "s"
    # The series of inputs will reset between two personas as long as the persona that is
    # selected second is in the first slot of all personas
    # The sleep command at the end of the section is a necessity to allow the screen to load
    # the persona before taking a screenshot and reading it
    # You may be able to decrease the delays of inputs if you have a fast system, but if your
    # system slows down or freezes it will cause the automation to break
    # You can also include the inputs to select a persona not in the first slot, but this will
    # increase the amount of time needed for each reset
    # To reset for a cross, pentagon or hexagon spread, the only inputs needed are one "Circle"
    # input and the one "Cross" input

    #TODO read screen dimesions and do math to find the correct region
    pyautogui.screenshot('screenshot.png', region=(348, 733, 809, 233))
    result = reader.readtext('screenshot.png')
    print(result)
    # This takes a screenshot and saves it in the folder in which the file is being run from
    # It will automatically overwrite the last screenshot, so you will not need to remove a
    # mass of screeshots from your files
    # The region argument is bound to where the skills box shows up on my system
    # Depending on your system's resolution and set-up it may be different
    # To find the region for your computer, take a screenshot of the emulator as you will have it while resetting
    # Use an image editing software to find the bounds or the screen, and input them into the region argument
    # The argument is formatted as "(Upper left corner X value, Upper left corner Y value,
    # Horizontal length, Vertical height)"
    # I was able to find this very easily in paint.net, though most image editing software
    # will likely allow you to do something similar
    # The rest of the section reads the screen via the OCR, and nothing there needs to be formatted

    #TODO remove hard coded arrays and use varibles
    step1 = np.array(result)
    step2 = step1[skillLocations, oneList]
    step3 = np.array2string(step2)
    # This step takes the output of the OCR and converts it into a usable string for the filter
    # Depending on what you are fusing, you will need to alter the values in the "step2" variable
    # The OCR reads left to right, top to bottom, while the game lists skills from top to bottom before going over a row
    # Depending on how many skills you are passing on, you will have more or less skills in the step2 part
    # There will be an image on the GitHub age explaining this in more detail, but I'll put what I can in the comments
    # Basically, the skills in order of inheritance have a value of "0,2,4,6,1,3,5,7" in that order
    # For example, if you are fusing an Orpheus with 4 extra skills, the innate skill of Bash will
    # have a value of 0, and the inherited skills will have values of 2, 4, 6, and 1
    # In this case, the input for step2 should be "[2,4,6,1]", although the order does not matter
    # The second set of numbers in brackets will always be 1, and you need a 1 for each skill
    # For example if you are inheriting 3 skills it should read "[1,1,1]", and for 5 skills it should read "[1,1,1,1,1]"
    # The rest of the variables do not need to be altered

    #TODO replace hard coded array with varible array with user input
    target1 = wantedSkills
    filter1 = list(filter(lambda x: x in step3, target1))
    correct = len(filter1)
    print(step3)
    print(filter1)
    print(correct)

    target2 = unwantedSkills
    filter2 = list(filter(lambda x: x in step3, target2))
    wrong = len(filter2)
    print(filter2)
    print(wrong)
# The last step in the loop filters the skills read from the OCR and updates the variabels keeping the loop running
# Target1 is for any skills that are desired, and Target2 is for undesired skills
# The skills are case sensitive, and some skills that have multiple words may have
# and underline in them when read by the OCR e.g. "Raging_Tiger"
# I would suggest watching the log that the program prints as it goes along to determine
# how the OCR reads the skill, or put in both options into the filter
# After filtering, the program prints out all the information at the various steps so you can
# see what it is reading and doing if you need to troubleshoot
# If you are only looking for specific skills and do not care which additional skills are rolled,
# you can comment out the target2 section
# If you are only looking to exclude specific skills and do not care what other skills are rolled,
# such as when making an intermediate, comment out the target1 section

keyboard.press(Key.esc)
time.sleep(0.25)
keyboard.press(Key.esc)
print("Finished!")
# This final line runs after the loop is finished
# The escape key is the default key to pause the emulation in PCSX2, which is the emulator I used
# I added this just so it wouldn't proceed to run any longer than necessary, and it can be removed if not desired
