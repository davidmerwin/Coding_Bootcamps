# Imports the Any type from typing to annotate variable types
from typing import Any

"""
This Python script demonstrates object-oriented programming by defining and 
using a Cat class.A class in Python represents a blueprint for creating objects. Objects created 
from classes are called instances.Classes define attributes and behaviors associated with an object. They encapsulate 
related data and functionality together.Objects represent unique instances of a class. Each object has its own distinct 
attribute values, but share behaviors defined by the class.This allows abstraction - objects provide a simple interface to interact with and 
hide internal complexity. 
Classes support inheritance - child classes can inherit attributes and behaviors 
from parent classes.
Objects also enable polymorphism - objects of different classes can be treated alike 
if they have the same method names and signatures.  
"""

# Class names are typically CamelCased
class Cat:

    # Class attributes are shared by all instances of this class
    # Attributes are data associated with a class or instance
    species: str = 'mammal'

    # The constructor method is called when a new instance is created
    # self refers to the instance being constructed
    def __init__(self, name: str, age: int) -> None:
        """
    Initialize a new Cat instance with the given name and age

    Parameters:
      name (str): The cat's name
      age (int): The cat's age in years

    Attributes:
      self.name - The name of the cat
      self.age - The age of the cat
    """

    # Instance attributes are unique to each object instance
    self.name = name
    self.age = age

# Create Cat instances by calling the constructor
# Objects encapsulate data and provide an interface to behaviors
peanut = Cat("Peanut", 3)
garfield = Cat("Garfield", 5)
snickers = Cat("Snickers", 1)

# Functions accept positional arguments and keyword arguments
# *args collects positional arguments into a tuple
def get_oldest_cat(*args: int) -> int:
    """
  Finds the oldest cat from the passed ages

  Parameters:
    *args: Tuple of ages

  Returns:
    The maximum age
  """

    return max(args)

# Call function with the ages of the cats
print(f"The oldest cat is {get_oldest_cat(peanut.age, garfield.age, snickers.age)} years old.")




