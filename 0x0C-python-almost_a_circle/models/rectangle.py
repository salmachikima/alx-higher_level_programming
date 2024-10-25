#!/usr/bin/python3
"""define a class rectangle"""


from models.base import Base


class Rectangle(Base):
    """Class defines properties of Rectangle

     Attributes:
        width (int): rectangle width
        height (int): rectangle height
        y (int): y
        x (int): x
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Creates instance of rectangle

        Args:
            height (int): height of rectangle
            width (int): width of rectangle
            y (int, optional): y. Default to 0
            x (int, optional): x. Defaults to 0
            id (int, optional): Identity number. Default to nothing
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def __str__(self):
        """Prints a rectangle"""
        return ("[Rectangle] ({}) {:d}/{:d} - {:d}/{:d}".
                format(self.id, self.__x, self.__y, self.__width,
                       self.__height))

    @property
    def width(self):
        """retriever of width

        Returns:
            int: rectangle's width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Setter's property for width of the rectangle.

        Args:
            value (int): rectangle width

        Raises:
            TypeError: if width is not int
            ValueError: if width less than 0 or equal to it
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """retriever of the width

        Returns:
            int: rectangle height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Property setter for the height

        Args:
            value (int): height

        Raises:
            TypeError: if height is not an int
            ValueError: if height is less than 0 or equale to it
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """retriever of x

        Returns:
            int: x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """x proprety setter

        Args:
            value (int): x

        Raises:
            TypeError: if x is not an int
            ValueError: if x is less or equal to 0
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """retreiver of y

        Returns:
            int: y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """y proprety setter

        Args:
            value (int): y

        Raises:
            TypeError: if y is not an int
            ValueError: if y is less or equal to 0
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """calculate rectangle area

        Returns:
            int: area
        """
        return self.__width * self.__height

    def display(self):
        """Prints the Rectangle instance with # in stdout"""
        if self.__y > 0:
            for i in range(self.__y):
                print()
            self.__y = 0
        for i in range(self.__height):
            for j in range(self.__width):
                if self.__y == j:
                    print(" " * self.__x, end="")
                print("#", end="")
            print()

    def update(self, *args, **kwargs):
        """Assigning to the attribute an arg

        Args:
            *args (tuple): args
            **kwargs (dict): double pointer
        """

        # print("args {}".format(type(args)))
        # print("kwargs {}".format(type(kwargs)))
        if args is not None and len(args) is not 0:
            list_atrr = ['id', 'width', 'height', 'x', 'y']
            for i in range(len(args)):
                setattr(self, list_atrr[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Returns representation of a rectangle in the dictionnary

        Returns:
            dict: rectangle
        """
        dict = {}
        dict["id"] = self.id
        dict["width"] = self.width
        dict["height"] = self.height
        dict["x"] = self.x
        dict["y"] = self.y
        return (dict)
