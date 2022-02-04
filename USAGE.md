# Usage

## Getting Started

To import the module, do `import py_load`.

Then, to initialize a loading bar do: `myLoadingBar = py_load.LoadingBar(<total>)`.

To set the progress do `myLoadingBar.progress = <value>`

And finally to display the loading bar do `myLoadingBar.display()`

Full Example:

```python
import py_load

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

The loading bar can be customized by setting the `borderChars`, `progressChar`, and `emptyChar` arguements.

These can be changed by doing `<loadingBar>.<arguement> = <value>`, or by using the arguements when initializing the Loading Bar.

*Note: `progressChar` and `emptyChar` are strings, but `borderChars` is a list that should contain two values.*
