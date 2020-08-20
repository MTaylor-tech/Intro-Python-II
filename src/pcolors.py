def prRed(str): print("\u001b[38;5;1m{}\u001b[0m".format(str))
def prGreen(str): print("\u001b[38;5;2m{}\u001b[0m".format(str))
def prYellow(str): print("\u001b[38;5;3m{}\u001b[0m".format(str))
def prBlue(str): print("\u001b[38;5;4m{}\u001b[0m".format(str))
def prLightPurple(str): print("\u001b[38;5;5m{}\u001b[0m".format(str))
def prPurple(str): print("\u001b[38;5;57m{}\u001b[0m".format(str))
def prCyan(str): print("\u001b[38;5;6m{}\u001b[0m".format(str))
def prOrange(str): print("\u001b[38;5;172m{}\u001b[0m".format(str))
def prGrey(str): print("\u001b[38;5;8m{}\u001b[0m".format(str))
def prBlack(str): print("\u001b[38;5;0m{}\u001b[0m".format(str))
def prBrightRed(str): print("\u001b[38;5;9m{}\u001b[0m".format(str))
def prBrightGreen(str): print("\u001b[38;5;10m{}\u001b[0m".format(str))
def prBrightYellow(str): print("\u001b[38;5;11m{}\u001b[0m".format(str))
def prBrightBlue(str): print("\u001b[38;5;12m{}\u001b[0m".format(str))
def prBrightLightPurple(str): print("\u001b[38;5;13m{}\u001b[0m".format(str))
def prBrightCyan(str): print("\u001b[38;5;14m{}\u001b[0m".format(str))
def prBrightOrange(str): print("\u001b[38;5;208m{}\u001b[0m".format(str))
def prBrightWhite(str): print("\u001b[38;5;15m{}\u001b[0m".format(str))
def prColor(str, color): print("\u001b[38;5;{}m{}\u001b[0m".format(color, str))
def inRed(str): return input("\u001b[38;5;1m{}\u001b[0m".format(str))
def inGreen(str): return input("\u001b[38;5;2m{}\u001b[0m".format(str))
def inYellow(str): return input("\u001b[38;5;3m{}\u001b[0m".format(str))
def inBlue(str): return input("\u001b[38;5;4m{}\u001b[0m".format(str))
def inLightPurple(str): return input("\u001b[38;5;5m{}\u001b[0m".format(str))
def inPurple(str): return input("\u001b[38;5;57m{}\u001b[0m".format(str))
def inCyan(str): return input("\u001b[38;5;6m{}\u001b[0m".format(str))
def inOrange(str): return input("\u001b[38;5;172m{}\u001b[0m".format(str))
def inGrey(str): return input("\u001b[38;5;8m{}\u001b[0m".format(str))
def inBlack(str): return input("\u001b[38;5;0m{}\u001b[0m".format(str))
def inBrightRed(str): return input("\u001b[38;5;9m{}\u001b[0m".format(str))
def inBrightGreen(str): return input("\u001b[38;5;10m{}\u001b[0m".format(str))
def inBrightYellow(str): return input("\u001b[38;5;11m{}\u001b[0m".format(str))
def inBrightBlue(str): return input("\u001b[38;5;12m{}\u001b[0m".format(str))
def inBrightLightPurple(str): return input("\u001b[38;5;13m{}\u001b[0m".format(str))
def inBrightCyan(str): return input("\u001b[38;5;14m{}\u001b[0m".format(str))
def inBrightOrange(str): return input("\u001b[38;5;208m{}\u001b[0m".format(str))
def inBrightWhite(str): return input("\u001b[38;5;15m{}\u001b[0m".format(str))
def inColor(str, color): return input("\u001b[38;5;{}m{}\u001b[0m".format(color, str))

def prNiceBlue(str): print("\033[96m{}\033[00m".format(str))
def inNiceBlue(str): return input("\033[96m{}\033[00m".format(str))

def prItalic(str): print("\x1B[3m{}\x1B[23m".format(str))
def inItalic(str): return input("\x1B[3m{}\x1B[23m".format(str))
def prBold(str): print("\x1B[3m{}\x1B[23m".format(str))
def inBold(str): return input("\x1B[1m{}\x1B[23m".format(str))

def show_colors():
    for i in range(16):
        for j in range(16):
            n = i*16+j
            prColor('{}'.format(n),n)

italic = "\x1B[3m"
bold = "\x1B[1m"
clear_style = "\x1B[23m"

def sRed(str): return "\u001b[38;5;1m{}\u001b[0m".format(str)
def sGreen(str): return "\u001b[38;5;2m{}\u001b[0m".format(str)
def sYellow(str): return "\u001b[38;5;3m{}\u001b[0m".format(str)
def sBlue(str): return "\u001b[38;5;4m{}\u001b[0m".format(str)
def sLightPurple(str): return "\u001b[38;5;5m{}\u001b[0m".format(str)
def sPurple(str): return "\u001b[38;5;57m{}\u001b[0m".format(str)
def sCyan(str): return "\u001b[38;5;6m{}\u001b[0m".format(str)
def sOrange(str): return "\u001b[38;5;172m{}\u001b[0m".format(str)
def sGrey(str): return "\u001b[38;5;8m{}\u001b[0m".format(str)
def sBlack(str): return "\u001b[38;5;0m{}\u001b[0m".format(str)
def sBrightRed(str): return "\u001b[38;5;9m{}\u001b[0m".format(str)
def sBrightGreen(str): return "\u001b[38;5;10m{}\u001b[0m".format(str)
def sBrightYellow(str): return "\u001b[38;5;11m{}\u001b[0m".format(str)
def sBrightBlue(str): return "\u001b[38;5;12m{}\u001b[0m".format(str)
def sBrightLightPurple(str): return "\u001b[38;5;13m{}\u001b[0m".format(str)
def sBrightCyan(str): return "\u001b[38;5;14m{}\u001b[0m".format(str)
def sBrightOrange(str): return "\u001b[38;5;208m{}\u001b[0m".format(str)
def sBrightWhite(str): return "\u001b[38;5;15m{}\u001b[0m".format(str)
def sColor(str, color): return "\u001b[38;5;{}m{}\u001b[0m".format(color, str)

clear_color = "\u001b[0m"
red = "\u001b[38;5;1m"
green = "\u001b[38;5;2m"
blue = "\u001b[38;5;3m"
light_purple = "\u001b[38;5;4m"
purple = "\u001b[38;5;57m"
cyan = "\u001b[38;5;6m"
orange = "\u001b[38;5;172m"
grey = "\u001b[38;5;8m"
black = "\u001b[38;5;0m"
bright_red = "\u001b[38;5;9m"
bright_green = "\u001b[38;5;10m"
bright_yellow = "\u001b[38;5;11m"
bright_blue = "\u001b[38;5;12m"
bright_light_purple = "\u001b[38;5;13m"
bright_cyan = "\u001b[38;5;14m"
bright_orange = "\u001b[38;5;208m"
bright_white = "\u001b[38;5;15m"
color_start = "\u001b[38;5;"
