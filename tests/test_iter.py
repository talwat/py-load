# SMARTBAR TESTING SCRIPT

from time import sleep
from py_load import SmartBar, LoadingBar

def user_main():
    myLoadingBar = LoadingBar(45, barLength=50)
    myLoadingBar.progress = 0
    myLoadingBar.borderChars = ["[", "]"]
    myLoadingBar.progressChar = "#"
    myLoadingBar.emptyChar = " "
    myLoadingBar.borderCharsColors = [LoadingBar.Colors.WHITE]
    myLoadingBar.progressCharColors = [LoadingBar.Colors.BLUE]
    myLoadingBar.emptyCharColors = [LoadingBar.Colors.RED]
    myLoadingBar.includePercent = True
    myLoadingBar.includeNums = True

    print("foo")
    for i in SmartBar(range(6), myLoadingBar):
        sleep(0.3) # Here instead you would do stuff
    print("bar")

def test_main():
    myLoadingBar = LoadingBar(45, barLength=50)
    myLoadingBar.progress = 0
    myLoadingBar.borderChars = ["[", "]"]
    myLoadingBar.progressChar = "#"
    myLoadingBar.emptyChar = " "
    myLoadingBar.borderCharsColors = [LoadingBar.Colors.WHITE]
    myLoadingBar.progressCharColors = [LoadingBar.Colors.BLUE]
    myLoadingBar.emptyCharColors = [LoadingBar.Colors.RED]
    myLoadingBar.includePercent = True
    myLoadingBar.includeNums = True

    print("foo")
    for i in SmartBar(range(6), myLoadingBar):
        pass # Here you would do stuff
    print("bar")

if __name__ == "__main__":
    user_main()
else:
    test_main()