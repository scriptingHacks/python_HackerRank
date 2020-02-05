import textwrap

def wrap(string, max_width):
    return textwrap.fill(string, max_width)


if __name__ == '__main__':
    print(wrap("ABCDEFGHIJKLIMNOQRSTUVWXYZ", 4))
