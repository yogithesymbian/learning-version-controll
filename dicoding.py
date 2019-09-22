__author__ = "yogithesymbian"
import sys
from color import ColorPrint as warna

print("dicodingidn")


def footer():
    warna.print_fail("===============FOOTER===============")


def start():
    authorName = "Yogi Arif Widodo  | yogithesymbian"
    authorUrl = "image url(https://avatars2.githubusercontent.com/u/28316296?s=400&u=e22e07736450e363997d6eb3534aa184a51c761c&v=4)"
    print(authorName)
    print(authorUrl)
    warna.print_pass("gitkraken")
    footer()


if __name__ == '__main__':
    try:
        start()
    except KeyboardInterrupt as err:
        print(err)
        sys.exit(0)
