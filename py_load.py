class LoadingBar:
    """
    Py-Load main class.

    Code available on Github.
    """

    # Class with a list of all the different ANSI codes in order to select colors easily.
    class Colors:
        """
        Color Class.

        This class has constants which are ANSI codes.

        If the name of the variable ends with `BG`, it will apply the color to the background of where the text is.

        If the name ends with `2`, it will use the darker variant of the color.
        """
        END       = '\33[0m'
        BOLD      = '\33[1m'
        ITALIC    = '\33[3m'
        URL       = '\33[4m'
        BLINK     = '\33[5m'
        BLINK2    = '\33[6m'
        SELECTED  = '\33[7m'

        BLACK    = '\33[30m'
        RED      = '\33[31m'
        GREEN    = '\33[32m'
        YELLOW   = '\33[33m'
        BLUE     = '\33[34m'
        VIOLET   = '\33[35m'
        BEIGE    = '\33[36m'
        WHITE    = '\33[37m'

        BLACKBG   = '\33[40m'
        REDBG     = '\33[41m'
        GREENBG   = '\33[42m'
        YELLOWBG  = '\33[43m'
        BLUEBG    = '\33[44m'
        VIOLETBG  = '\33[45m'
        BEIGEBG   = '\33[46m'
        WHITEBG   = '\33[47m'

        GREY      = '\33[90m'
        RED2      = '\33[91m'
        GREEN2    = '\33[92m'
        YELLOW2   = '\33[93m'
        BLUE2     = '\33[94m'
        VIOLET2   = '\33[95m'
        BEIGE2    = '\33[96m'
        WHITE2    = '\33[97m'

        GREYBG    = '\33[100m'
        REDBG2    = '\33[101m'
        GREENBG2  = '\33[102m'
        YELLOWBG2 = '\33[103m'
        BLUEBG2   = '\33[104m'
        VIOLETBG2 = '\33[105m'
        BEIGEBG2  = '\33[106m'
        WHITEBG2  = '\33[107m'

    def __init__(self, 
                 total:              int, 
                 borderChars:        list = ["[", "]"], 
                 progressChar:       str  = "#", 
                 emptyChar:          str  = " ", 
                 borderCharsColors:  list = [Colors.END], 
                 progressCharColors: list = [Colors.END], 
                 emptyCharColors:    list = [Colors.END],
                 includePercent:     bool = False, 
                 percentChar:        str  = "%", 
                 percentLocation:    bool = True,
                 barLength:          int  = 50):
        """
        Initialize the Loading Bar.

        Customize the characters specifying the `borderChars`, `progressChar`, and `emptyChar` arguments.

        Customize the colors specifying the `borderCharsColors`, `progressCharColors`, and `emptyCharColors` arguments.

        You can do this by doing `<loadingBarName>.<argumentsName> = <value>`. 
        This can also be specified when initializing.
        """

        self.total = total
        """
        The total/max value of the loading bar.
        """
        self.progress = 0
        """
        The progress value of the loading bar. Not a precentage.
        """
        self.borderChars = borderChars
        """
        Default: "[", "]"

        A list that should have two values, the opening border character and the closing border character.

        They surround the loading bar's progress meter.

        Eg:
        ```
        ...
        myLoadingBar.borderChars = ["{", "}"]
        myLoadingBar.display()
        ```
        Output: `{##########}`
        """
        self.progressChar = progressChar
        """
        Default: "#"

        The progress character / the fill character.
        """
        self.emptyChar = emptyChar
        """
        Default: " " (space)

        The empty character
        """
        self.borderCharsColors = borderCharsColors
        """
        Default: [Colors.END]

        An array of the colors of the border characters.

        Each element in the array will be added as a color.

        So for example, if you wanted green text with a white background you would do:

        `myLoadingBar.borderCharsColors = [py_load.LoadingBar.Colors.GREEN, py_load.LoadingBar.Colors.WHITEBG]`
        """
        self.progressCharColors = progressCharColors
        """
        Default: [Colors.END]

        An array of the colors of the progress character.

        Each element in the array will be added as a color.

        So for example, if you wanted green text with a green background you would do:

        `myLoadingBar.progressCharColors = [py_load.LoadingBar.Colors.GREEN, py_load.LoadingBar.Colors.GREENBG]`
        """
        self.emptyCharColors = emptyCharColors
        """
        Default: [Colors.END]

        An array of the colors of the empty character.

        Each element in the array will be added as a color.

        So for example, if you wanted orange text with a red background you would do:

        `myLoadingBar.emptyCharColors = [py_load.LoadingBar.Colors.ORANGE, py_load.LoadingBar.Colors.REDBG]`
        """
        self.includePercent = includePercent 
        """
        Default: False

        Decides whether the loading bar will be displayed with a percent on one of the sides.

        For example:

        ```
        ...
        myLoadingBar.includePercent = True
        myLoadingBar.display()
        ```
        Output: `[##########] 100%`
        """

        self.percentChar = percentChar
        """
        Default: "%"

        The character next to the percentage.

        Does nothing if `includePercent` isn't set to true.

        For example:

        ```
        ...
        myLoadingBar.includePercent = True
        myLoadingBar.percentChar = "$"
        myLoadingBar.display()
        ```
        Output: `[##########] 100$`
        """
        self.percentLocation = percentLocation
        """
        Default: True

        Sets which side the precent and precent character will appear.

        True to have the percent on the right, and false to have it on the left.

        For example:

        ```
        ...
        myLoadingBar.includePercent = True
        myLoadingBar.display()
        ```
        Output: `[##########] 100%`
        """
        self.barLength = barLength
        """
        Default: 50

        The length (in characters) of the loading bar.
        """
    
    def display(self, autoPrint = True):
        """
        Display the Loading Bar.

        Disable `autoPrint` to have the method only return the string instead of printing it using the `print()` method.

        Enable `includePercent` to enable displaying the percent with the loading bar.

        Make `percentLocation` true to have the percent on the right, and false to have it on the left.

        Make sure to use the `print()` function right after calling this to reposition the cursor and avoid some issues.
        """

        # TODO: Make code even cleaner and more organized.

        def merge(input):
            return "".join(input)

        DISPLAYPERCENT = round((self.progress / self.total) * self.barLength)
        PERCENT = round((self.progress / self.total) * 100)
        if PERCENT > 100:
            PERCENT = 100
        
        END = LoadingBar.Colors.END
        PROGRESSCOLORS = merge(self.progressCharColors)
        BORDER = END + merge(self.borderCharsColors)
        BORDER1 = BORDER + self.borderChars[0] + END
        BORDER2 = BORDER + self.borderChars[1] + END

        REDUCT = len( BORDER + END + PROGRESSCOLORS)

        toPrint = ""

        toPrint += BORDER1
        toPrint += PROGRESSCOLORS 

        for i in range(DISPLAYPERCENT):
            length = len(toPrint) - REDUCT
            limit = self.barLength + len(self.borderChars[0])

            if length < limit:
                toPrint += self.progressChar

        toPrint += (END + merge(self.emptyCharColors))
        
        limit = self.barLength - DISPLAYPERCENT
        for i in range(limit):
            toPrint += self.emptyChar
        
        toPrint += BORDER2
        if self.includePercent:
            if self.percentLocation:
                toPrint += f" {PERCENT}{self.percentChar}"
            else:
                toPrint = f"{PERCENT}{self.percentChar} {toPrint}"

        if autoPrint:
            print(toPrint, end="\r")
        return toPrint

class SmartBar:
    """
    SmartBar class.
    """

    def __init__(self, iterable, bar: LoadingBar = None):
        """
        Super quickly and easily make a loading bar by using it in something like a `for` loop.
        
        Eg.
        
        ```
        for i in SmartBar(range(6)):
            doStuff()
        ```
        
        And have a loading bar automatically appear.

        However to specify what bar will appear you can also do `SmartBar(<iterable>, <loadingBar>)`

        It doesn't just have to be `range()`, it can also be any iterable.

        It may also have use outside of `for` loops, but it hasn't been tested yet.
        """
        self.iterable = iterable
        self.TOTAL = len(self.iterable) - 1
        if bar != None: 
            self.bar = bar
            self.bar.total = self.TOTAL
            return
        self.bar = LoadingBar(self.TOTAL)
    
    def __iter__(self):
        self.iteration = 0
        return self

    def __next__(self):
        if self.iteration <= self.TOTAL:
            self.bar.display()
            self.iteration += 1
            self.bar.progress = self.iteration
        else:
            raise StopIteration