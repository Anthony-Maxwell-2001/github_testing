"""Testing GitHub"""


def main():
    print("Hello World!")
    name = get_name()
    print("Hello ", name)


def get_name():
    name = input("Name: ")
    return name


main()
