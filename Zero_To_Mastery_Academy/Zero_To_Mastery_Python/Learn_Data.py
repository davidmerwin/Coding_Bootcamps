"""
This module demonstrates using dictionaries and sets in Python. Dictionaries provide key-value mappings in Python. They can store user profiles
and other structured data. Sets represent unordered collections of unique elements.
Sets support operations like difference to find missing elements.
"""

from typing import List, Set

# Dictionary storing user profile information
user: dict[str, str] = {
    'age': '22',
    'username': 'Shogun',
    'weapons': ['katana', 'shuriken'],
    'is_active': 'True',
    'clan': 'Japan'
}


def print_user(user: dict) -> None:
    """
    Prints the given user dictionary

    Parameters:
      user (dict): The user dictionary

    Returns: None
    """

    print(user)


# Print initial user
print_user(user)

# Add new weapon to weapons list
user['weapons'].append('shield')

# Print user with added weapon
print_user(user)

# Update dictionary with new key-value pair   
user['is_banned'] = 'False'

# Print user with new key  
print_user(user)

# Change value of is_banned key to True 
user['is_banned'] = 'True'

# Print updated user
print_user(user)

# Create new user by copying existing and updating values
user2 = user.copy()
user2['age'] = '100'
user2['username'] = 'Timbo'

# Print new user
print_user(user2)

# Set of all students 
school: Set[str] = {'Bobby', 'Tammy', 'Jammy', 'Sally', 'Danny'}

# List of students in attendance
attendance: List[str] = ['Jammy', 'Bobby', 'Danny', 'Sally']


def find_absent(all_students: Set[str], attended: List[str]) -> Set[str]:
    """
    Finds students absent by taking the difference between all 
    and those attended.
  
    Parameters:
      all_students (Set[str]): All students
      attended (List[str]): Students attended
  
    Returns:
      Set of absent students
    """

    return all_students.difference(attended)


# Find missing students by taking the difference  
print(find_absent(school, attendance))



