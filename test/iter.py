from time import sleep
from py_load import *

myLoadingBar = LoadingBar(45, barLength=50)
myLoadingBar.progress = 0
myLoadingBar.borderChars = ["[", "]"]
myLoadingBar.progressChar = "#"
myLoadingBar.emptyChar = " "
myLoadingBar.borderCharsColors = [LoadingBar.Colors.WHITE]
myLoadingBar.progressCharColors = [LoadingBar.Colors.BLUE]
myLoadingBar.emptyCharColors = [LoadingBar.Colors.RED]
myLoadingBar.includePercent = True

print("foo")
for i in SmartBar(range(6), myLoadingBar):
    sleep(0.5)
print("\nbar")