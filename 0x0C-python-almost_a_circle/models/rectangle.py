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
        """Height retriever.

        Returns:
            int: height of rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Property setter for height of rectangle.

        Args:
            value (int): height of rectangle.

        Raises:
            TypeError: if height is not an integer.
            ValueError: if height is less than or equal to zero.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """x retriever.

        Returns:
            int: x.
        """
        return self.__x

    @x.setter
    def x(self, value):
        """Property setter for x.

        Args:
            value (int): x.

        Raises:
            TypeError: if x is not an integer.
            ValueError: if x is less than or equal to zero.
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """y retriever.

        Returns:
            int: y.
        """
        return self.__y

    @y.setter
    def y(self, value):
        """Property setter for y.

        Args:
            value (int): y.

        Raises:
            TypeError: if y is not an integer.
            ValueError: if y is less than or equal to zero.
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Calculates area of a rectangle.

        Returns:
            int: area.
        """
        return self.__width * self.__height

    def display(self):
        """Prints in stdout the Rectangle instance with the character #."""
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
        """Assigns an argument to each attribute

        Args:
            *args (tuple): arguments.
            **kwargs (dict): double pointer to a dictionary.
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
        """Returns the dictionary representation of a Rectangle.

        Returns:
            dict: rectangle.
        """
        dict = {}
        dict["id"] = self.id
        dict["width"] = self.width
        dict["height"] = self.height
        dict["x"] = self.x
        dict["y"] = self.y
        return (dict)
