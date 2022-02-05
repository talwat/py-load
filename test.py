# TESTING SCRIPT

from time import sleep
import py_load
from py_load import LoadingBar

myLoadingBar = LoadingBar(45, barLength=50)
myLoadingBar.progress = 0
myLoadingBar.borderChars = ["[", "]"]
myLoadingBar.progressChar = " "
myLoadingBar.borderCharsColors = [LoadingBar.Colors.WHITEBG, LoadingBar.Colors.BLACK]
myLoadingBar.progressCharColors = [LoadingBar.Colors.GREENBG, LoadingBar.Colors.BLACK]
myLoadingBar.emptyCharColors = [LoadingBar.Colors.REDBG]

for i in range(6):
    sleep(0.5)
    myLoadingBar.progress += 10
    myLoadingBar.display()
print("\nbar")