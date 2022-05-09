"""
Informacje:
    Print Hello There
"""


def hello_there():
    print('hello there')


def main():
    hello_there()
    return 0

if __name__ == '__main__':
    if main() == 0:
        exit(0)
    else:
        exit(1)
