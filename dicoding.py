__author__ = "yogithesymbian"
import sys
from color import ColorPrint as warna

# print("dicodingidn")


def hackNasa():
    print("hello world")


def header():
    warna.print_warn("============================")
    print("""

 _   _ _____    _    ____  _____ ____
| | | | ____|  / \  |  _ \| ____|  _
| |_| |  _|   / _ \ | | | |  _| | |_) |
|  _  | |___ / ___ \| |_| | |___|  _ <
|_| |_|_____/_/   \_\____/|_____|_| \_

    """)
    warna.print_warn("============================")


def footer():
    warna.print_fail("=================================")

    print("""

     _____ ___   ___ _____ _____ ____
|  ___/ _ \ / _ \_   _| ____|  _
| |_ | | | | | | || | |  _| | |_) |
|  _|| |_| | |_| || | | |___|  _ <
|_|   \___/ \___/ |_| |_____|_| \_


    """)
    warna.print_footer("")
    warna.print_fail("=================================")


def start():
    authorName = "Yogi Arif Widodo  | yogithesymbian"
    authorUrl = "image url(https://avatars2.githubusercontent.com/u/28316296?s=400&u=e22e07736450e363997d6eb3534aa184a51c761c&v=4)"
    print(authorName)
    print(authorUrl)
    warna.print_pass("gitkraken")
    footer()


if __name__ == '__main__':
    try:
        header()
        start()
    except KeyboardInterrupt as err:
        print(err)
        sys.exit(0)
