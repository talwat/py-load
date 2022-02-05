class LoadingBar:
    """
    Py-Load main class.
    """

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
                 barLength:          int  = 50):
        """
        Initialize the Loading Bar.

        Customize the way it looks by specifying the `borderChars`, `progressChar`, and `emptyChar` arguements.

        You can do this by doing `<loadingBarName>.<arguementName> = <value>`. 
        This can also be specified when initializing.
        """

        self.total = total
        """The total/max value of the loading bar."""
        self.progress = 0
        """The progress value of the loading bar. Not a precentage."""
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
        self.barLength = barLength
        """
        Default: 50

        The length (in characters) of the loading bar.
        """
    
    def display(self, autoPrint = True):
        """
        Display the Loading Bar.

        Disable `autoPrint` to have the method only return the string instead of printing it using the `print()` method. 

        Make sure to use the `print()` function right after calling this to reposition the cursor and avoid some issues.
        """

        # TODO: Make code even cleaner and more organized.

        def merge(input):
            return "".join(input)

        PERCENT = round((self.progress / self.total) * self.barLength)
        
        END = LoadingBar.Colors.END
        PROGRESSCOLORS = merge(self.progressCharColors)
        BORDER = END + merge(self.borderCharsColors)
        BORDER1 = BORDER + self.borderChars[0] + END
        BORDER2 = BORDER + self.borderChars[1] + END

        REDUCT = len( BORDER + END + PROGRESSCOLORS)

        toPrint = ""

        toPrint += BORDER1
        toPrint += PROGRESSCOLORS 

        for i in range(PERCENT):
            length = len(toPrint) - REDUCT
            limit = self.barLength + len(self.borderChars[0])

            if length < limit:
                toPrint += self.progressChar

        toPrint += (END + merge(self.emptyCharColors))
        
        limit = self.barLength - PERCENT
        for i in range(limit):
            toPrint += self.emptyChar
        
        toPrint += BORDER2

        if autoPrint:
            print(toPrint, end="\r")
        return toPrint