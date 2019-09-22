import sys

print("dicodingidn")


def start():
    print("hello world")


if __name__ == '__main__':
    try:
        start()
    except KeyboardInterrupt as err:
        print(err)
        sys.exit(0)
