# Usage

## Getting Started

To import the module, do `from py_load import LoadingBar`.

Then, to initialize a loading bar do: `myLoadingBar = LoadingBar(<total>)`.

To set the progress do `myLoadingBar.progress = <value>`

And finally to display the loading bar do `myLoadingBar.display()`

Full Example:

```python
from py_load import LoadingBar

imageLoadingBar = py_load.LoadingBar(len(images))
i = 0

for image in range(images):
    resize(image)
    i += 1
    imageLoadingBar.progress = i
    imageLoadingBar.display()

print()
print("Done!")
```

## Customizing the bar

### Characters

The loading bars characters can be customized by setting the `borderChars`, `progressChar`, and `emptyChar` arguements.

These can be changed by doing `<loadingBar>.<arguement> = <value>`, or by using the arguements when initializing the Loading Bar.

*Note: `progressChar` and `emptyChar` are strings, but `borderChars` is a list that should contain two values.*

### Colors

The loading bars colors can also be changed by setting `borderCharsColors`, `progressCharColors` and `emptyCharColors`.

These values can be set while initializing the bar or later by doing `<loadingBar>.<arguement> = <value>`.

*Note: These values should be a list, to allow you to add both a foreground and a background.*
