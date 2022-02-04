# TESTING SCRIPT

from time import sleep
import py_load

myLoadingBar = py_load.LoadingBar(45, barLength=50)
myLoadingBar.progress = 0
print("foo")
for i in range(6):
    sleep(0.5)
    myLoadingBar.progress += 10
    myLoadingBar.display()
print("\nbar")