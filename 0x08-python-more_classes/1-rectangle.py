#!/usr/bin/python3
"""class that defines a rectangle with width
and height
"""

class Rectangle:
    """Here is a rectangle class with some properties
    like width and height
    """
    def __init__(self, width, height):
        """width and height Default Values"""
        self.width = 0  
        self.height = 0     
        """instantiation with optional width and height"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """width
        """
        return self.__width
        
    @property
    def height(self):
        """height
        """
        return self.__height

    @width.setter
    """width setter"""
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    """height setter"""
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be >= 0")
        self.__height = value





