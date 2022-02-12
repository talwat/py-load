# TESTING SCRIPT

from time import sleep
from py_load import LoadingBar

def test_main():
    myLoadingBar = LoadingBar(45, barLength=50)
    myLoadingBar.progress = 0
    myLoadingBar.borderChars = ["[", "]"]
    myLoadingBar.progressChar = "#"
    myLoadingBar.emptyChar = " "
    myLoadingBar.borderCharsColors = [LoadingBar.Colors.WHITE]
    myLoadingBar.progressCharColors = [LoadingBar.Colors.GREEN]
    myLoadingBar.emptyCharColors = [LoadingBar.Colors.RED]
    myLoadingBar.includePercent = True
    myLoadingBar.includeNums = True

    print("foo")
    for i in range(6):
        myLoadingBar.display()
        myLoadingBar.progress += 10
        sleep(0.5)
    print("\nbar")
    assert myLoadingBar

test_main()