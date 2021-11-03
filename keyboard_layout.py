# A program that changes the keyboard layout.
# First will run for random.

import ctypes
from ctypes import wintypes

# Loading ctypes libraries
user32 = ctypes.windll.LoadLibrary("User32.dll")

# argtypes, restypes.
user32.GetKeyboardLayout.argtypes = [ wintypes.DWORD ]
user32.ActivateKeyboardLayout.argtypes = [ wintypes.HKL, wintypes.UINT ]
user32.LoadKeyboardLayoutA.argtypes = [wintypes.LPCSTR, wintypes.UINT]
user32.UnloadKeyboardLayout.argtypes = [ wintypes.HKL ]
user32.GetKeyboardLayout.restype = wintypes.HKL


print( "==" * 50)

# Prints the current layout. 
stored_layout = wintypes.LPCSTR('00000409')
print(str(stored_layout) + "\n" + "--" * 50)

# Sets new layout
new_layout = wintypes.LPCSTR(0x4190412) # Russian primary, Korean sublanguage. 
user32.ActivateKeyboardLayout(new_layout, 0x00000008)
user32.LoadKeyboardLayoutA(new_layout, 0x00000001)

# Tests new layout
test = input("Type something, keyboard layout should've changed:  ")
print(test)
current_layout = user32.GetKeyboardLayout(0)
print(hex(current_layout))

# Reverts to old layout. 
user32.LoadKeyboardLayoutA(stored_layout, 0x00000001)
user32.UnloadKeyboardLayout(0x4190412)
'''
https://docs.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-getkeyboardlayout
https://docs.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-activatekeyboardlayout
https://docs.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-loadkeyboardlayouta
https://docs.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-unloadkeyboardlayout
https://kbdlayout.info/
'''