#!/usr/bin/python3
"""
Module 101-locked_class
Contains class LockedClass with no class or object attribute,
which only allows dynamic creation of the `first_name` instance attribute.
"""


class LockedClass:
    """
    A class that prevents dynamic creation of new instance attributes,
    except if the attribute is named 'first_name'.

    Methods:
        __setattr__(self, name, value): Overrides default attribute setting.
    """

    def __setattr__(self, name, value):
        """
        Override method to set attributes for LockedClass instances.
        Permits 'first_name' attr to be set; others will raise AttributeError.

        Args:
            name (str): The name of the attribute.
            value (any): The value of the attribute.

        Raises:
            AttributeError: If attribute name is not 'first_name'.
        """
        if name != "first_name":
            raise AttributeError(
                "'LockedClass' object has no attribute '{}'"
                .format(name))
        self.__dict__[name] = value
