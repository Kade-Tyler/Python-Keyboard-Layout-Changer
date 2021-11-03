import ctypes
from ctypes import wintypes

# Loading ctypes libraries
user32 = ctypes.windll.LoadLibrary("User32.dll")

# argtypes, restypes.
user32.UnloadKeyboardLayout.argtypes = [ wintypes.HKL ]

current_layout = user32.GetKeyboardLayout(0)
print(hex(current_layout))
new_layout = 0x4091009 # English primary, French secondary. 
user32.ActivateKeyboardLayout(new_layout, 0x00000008)

test = input("Type something, keyboard layout should've changed:  ")
print(test)
current_layout = user32.GetKeyboardLayout(0)
print(hex(current_layout))
