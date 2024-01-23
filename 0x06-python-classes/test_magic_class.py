#!/usr/bin/python3
import importlib.util
import sys

def main():
    # Dynamic import of the MagicClass from '103-magic_class.py'
    spec = importlib.util.spec_from_file_location("MagicClass", "./103-magic_class.py")
    magic_class = importlib.util.module_from_spec(spec)
    sys.modules["MagicClass"] = magic_class
    spec.loader.exec_module(magic_class)

    MagicClass = magic_class.MagicClass

    radius = 5
    magic_circle = MagicClass(radius)

    print("Area:", magic_circle.area())
    print("Circumference:", magic_circle.circumference())

if __name__ == "__main__":
    main()
