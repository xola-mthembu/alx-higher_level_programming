#!/usr/bin/python3
class LockedClass:
    def __init__(self):
        self._first_name = None

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        if self._first_name is not None:
            raise AttributeError("'LockedClass' object cannot set attribute")
        self._first_name = value
