# TESTING SCRIPT

from time import sleep
from py_load import LoadingBar

def user_main():
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
        sleep(0.3) # Here instead you would do stuff
    print("\nbar")

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
        # Here you would do stuff
    print("\nbar")

if __name__ == "__main__":
    user_main()
else:
    test_main()