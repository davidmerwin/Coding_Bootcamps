# Imports the List data type from the typing module
# This allows us to annotate the types of variables below
from typing import List

"""
This is a Python module that prints an image using a 2D list of 0s and 1s.

A module in Python contains reusable code and can be imported and used by other code.

The syntax `if __name__ == '__main__':` at the bottom allows this module to be 
imported without running the code automatically.

A list in Python is an ordered collection of elements that can contain different data types.
Lists are defined using square brackets [] with elements separated by commas.

A 2D list contains lists within a list, representing a matrix or grid structure.
"""

# This is a 2D list variable called `picture` that stores the image
# The `List[List[int]]` annotation indicates it is a list of integer lists
picture: List[List[int]] = [

    # Each inner list represents a row of the image
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0]
]


# This is a function definition with a docstring describing what it does
# Functions encapsulate reusable logic in Python
def print_image(image: List[List[int]]) -> None:
    """
    Prints the given 2D image list row-wise

    The `image` parameter is the 2D list representing the image
    It is annotated as a list of integer lists to define the expected structure

    This function does not return anything, indicated by the `None` return type annotation
    """

    # Loop over each inner list representing a row
    for row in image:

        # Loop over each element representing a pixel
        for pixel in row:

            # An if statement allows conditional logic in Python
            # This checks if the pixel value is 1
            if pixel:

                # Print a '*' character for a filled pixel
                print('*', end='')

                # The else block runs if the if condition is false
            else:

                # Print a space character for an empty pixel
                print(' ', end='')

        # Print a newline after each row
        print('')


# Python executes the code in this block when the module is run directly
# Modules can be reused across different scripts
if __name__ == '__main__':
    # Call the print_image function to print the picture variable
    print_image(picture)
