import time
import pyautogui

name=input("Enter The Name of your Friend u wanna disturb: ")
input("Switch to the WhatsApp Web chat window and press Enter to continue...")

animals = [
    "ant", "bear", "cat", "dog", "elephant", "fox", "giraffe", "horse", "iguana", "jaguar",
    "kangaroo", "lion", "monkey", "newt", "owl", "panda", "quokka", "rabbit", "snake", "tiger",
    "unicorn", "vulture", "wolf", "xerus", "yak", "zebra", 
    "alpaca", "bat", "cheetah", "dolphin", "eagle", "flamingo", "goat", "hamster", "impala",
    "jellyfish", "koala", "lemur", "mongoose", "narwhal", "otter", "penguin", "quail", "rhinoceros",
    "sloth", "toucan", "urial", "viper", "wombat", "x-ray tetra", "yabby", "zebu",
    "alligator", "buffalo", "chimpanzee", "dalmatian", "elephant seal", "frog", "gazelle", "hedgehog",
    "ibex", "jackal"
]

while True:
    for animal in animals:
        message = f"*{name}* `aik {animal} hai`" 
        pyautogui.typewrite(message)
        pyautogui.press('enter')
        time.sleep(1)

