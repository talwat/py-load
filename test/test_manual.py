# MANUEL UPDATE SCRIPT

from time import sleep
from py_load import LoadingBar

def test_main():
    myLoadingBar = LoadingBar(45, barLength=50)
    myLoadingBar.progress = 0
    myLoadingBar.borderChars = ["[", "]"]
    myLoadingBar.progressChar = "#"
    myLoadingBar.emptyChar = " "
    myLoadingBar.borderCharsColors = [LoadingBar.Colors.WHITE]
    myLoadingBar.progressCharColors = [LoadingBar.Colors.YELLOW]
    myLoadingBar.emptyCharColors = [LoadingBar.Colors.RED]
    myLoadingBar.includePercent = True
    myLoadingBar.includeNums = True

    print("foo")
    myLoadingBar.display()
    sleep(0.1) # Here instead you would do stuff
    myLoadingBar.progress += 10

    myLoadingBar.display()
    sleep(0.1) # Here instead you would do stuff
    myLoadingBar.progress += 10

    myLoadingBar.display()
    sleep(0.1) # Here instead you would do stuff
    myLoadingBar.progress += 10

    myLoadingBar.display()
    sleep(0.1) # Here instead you would do stuff
    myLoadingBar.progress += 10

    print("\nbar")

test_main()