import greeting


def main():
    name: str = input('Whats your name? ')
    greeting.greet(name)


# To compile our .pyx script
# python setup.py build_ext --inplace
if __name__ == '__main__':
    main()
