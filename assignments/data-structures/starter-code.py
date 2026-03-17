"""
Python Data Structures Starter Code

This is a starter template for working with Python's core data structures:
lists, dictionaries, sets, and tuples.

Implement the functions below to practice data structure manipulation skills.

Key concepts to implement:
- List operations: indexing, slicing, sorting, filtering
- Dictionary operations: key-value access, iteration, comprehensions
- Set operations: union, intersection, difference
- Tuple unpacking and immutability
- Choosing the right data structure for each problem
"""

from typing import List, Dict, Set, Tuple, Any
from collections import namedtuple


# ============================================================================
# TASK 1: Lists and List Operations
# ============================================================================

def create_list_from_range(start: int, end: int, step: int = 1) -> List[int]:
    """
    Create a list of integers from start to end with the given step
    
    Example:
        create_list_from_range(1, 10, 2)  # Returns [1, 3, 5, 7, 9]
    """
    # TODO: Implement using range() or list comprehension
    pass


def remove_duplicates(items: List[Any]) -> List[Any]:
    """
    Remove duplicates from a list while preserving order
    
    Example:
        remove_duplicates([1, 2, 2, 3, 1, 4])  # Returns [1, 2, 3, 4]
    """
    # TODO: Implement without changing order
    pass


def reverse_list(items: List[Any]) -> List[Any]:
    """Reverse a list without using the built-in reverse() method"""
    # TODO: Implement list reversal
    pass


def find_second_largest(numbers: List[int]) -> int:
    """
    Find the second largest number in a list
    
    Example:
        find_second_largest([10, 5, 8, 12, 9])  # Returns 10
    """
    # TODO: Implement finding second largest element
    pass


def filter_by_condition(items: List[int], condition) -> List[int]:
    """
    Filter list items that satisfy a condition function
    
    Example:
        filter_by_condition([1, 2, 3, 4, 5], lambda x: x > 3)  # Returns [4, 5]
    """
    # TODO: Implement using list comprehension or filter()
    pass


def flatten_nested_list(nested: List[List[int]]) -> List[int]:
    """
    Flatten a nested list into a single list
    
    Example:
        flatten_nested_list([[1, 2], [3, 4], [5]])  # Returns [1, 2, 3, 4, 5]
    """
    # TODO: Implement flattening
    pass


def sort_by_multiple_criteria(items: List[Tuple[str, int]], 
                              sort_by: str = "name") -> List[Tuple[str, int]]:
    """
    Sort a list of tuples by name or age
    
    Example:
        items = [("Alice", 30), ("Bob", 25), ("Charlie", 30)]
        sort_by_multiple_criteria(items, "name")  # Returns [("Alice", 30), ("Bob", 25), ("Charlie", 30)]
        sort_by_multiple_criteria(items, "age")   # Returns [("Bob", 25), ("Alice", 30), ("Charlie", 30)]
    """
    # TODO: Implement sorting with key parameter
    pass


# ============================================================================
# TASK 2: Dictionaries and Key-Value Operations
# ============================================================================

def build_frequency_dict(items: List[Any]) -> Dict[Any, int]:
    """
    Count occurrences of each item and return frequency dictionary
    
    Example:
        build_frequency_dict(['a', 'b', 'a', 'c', 'b', 'a'])
        # Returns {'a': 3, 'b': 2, 'c': 1}
    """
    # TODO: Implement frequency counting
    pass


def word_frequency_from_text(text: str) -> Dict[str, int]:
    """
    Extract words from text and count their frequencies
    
    Example:
        word_frequency_from_text("hello world hello python")
        # Returns {'hello': 2, 'world': 1, 'python': 1}
    """
    # TODO: Split text and count word frequencies
    pass


def merge_dictionaries(dict1: Dict, dict2: Dict) -> Dict:
    """
    Merge two dictionaries, with dict2 values overriding dict1 values for common keys
    
    Example:
        merge_dictionaries({'a': 1, 'b': 2}, {'b': 3, 'c': 4})
        # Returns {'a': 1, 'b': 3, 'c': 4}
    """
    # TODO: Implement dictionary merging
    pass


def invert_dictionary(d: Dict[str, int]) -> Dict[int, List[str]]:
    """
    Invert dictionary so values become keys and keys become values
    Handle multiple keys with same value by grouping them in a list
    
    Example:
        invert_dictionary({'a': 1, 'b': 2, 'c': 1})
        # Returns {1: ['a', 'c'], 2: ['b']}
    """
    # TODO: Implement dictionary inversion
    pass


def find_common_keys(dict1: Dict, dict2: Dict) -> Set:
    """Find keys that exist in both dictionaries"""
    # TODO: Implement finding common keys
    pass


def get_nested_value(d: Dict, key_path: str, default=None) -> Any:
    """
    Get value from nested dictionary using dot notation
    
    Example:
        d = {'user': {'name': 'Alice', 'age': 30}}
        get_nested_value(d, 'user.name')  # Returns 'Alice'
        get_nested_value(d, 'user.email', 'N/A')  # Returns 'N/A'
    """
    # TODO: Implement nested dictionary access
    pass


def build_student_database(students_data: List[Tuple[str, int, float]]) -> Dict:
    """
    Build a student database from list of tuples (name, age, gpa)
    
    Example:
        data = [("Alice", 20, 3.8), ("Bob", 21, 3.6)]
        db = build_student_database(data)
        # Returns {'Alice': {'age': 20, 'gpa': 3.8}, 'Bob': {'age': 21, 'gpa': 3.6}}
    """
    # TODO: Implement database building
    pass


# ============================================================================
# TASK 3: Sets and Tuples with Advanced Operations
# ============================================================================

def find_common_elements(set1: Set, set2: Set) -> Set:
    """Find intersection of two sets"""
    # TODO: Implement using set intersection
    pass


def find_unique_elements(set1: Set, set2: Set) -> Set:
    """
    Find elements that are in either set but not in both (symmetric difference)
    
    Example:
        find_unique_elements({1, 2, 3}, {2, 3, 4})  # Returns {1, 4}
    """
    # TODO: Implement symmetric difference
    pass


def find_difference(set1: Set, set2: Set) -> Set:
    """Find elements in set1 that are not in set2"""
    # TODO: Implement set difference
    pass


def remove_duplicates_preserve_order(items: List[Any]) -> List[Any]:
    """
    Remove duplicates while preserving original order using both list and set
    
    Example:
        remove_duplicates_preserve_order([1, 2, 2, 1, 3])  # Returns [1, 2, 3]
    """
    # TODO: Implement using set to track seen items
    pass


def unpack_tuple(data: Tuple[str, int, float]) -> Tuple[str, int, float]:
    """
    Unpack tuple into individual variables and return them in different order
    
    Example:
        name, age, score = unpack_tuple(("Alice", 25, 95.5))
    """
    # TODO: Implement tuple unpacking
    pass


def create_student_tuple() -> Tuple:
    """
    Create a named tuple for student data with fields: name, id, gpa, major
    
    Example:
        Student = create_student_tuple()
        alice = Student("Alice", 12345, 3.8, "Computer Science")
        print(alice.name)  # Alice
    """
    # TODO: Use namedtuple to create Student type
    pass


def find_all_intersections(sets_list: List[Set]) -> Set:
    """
    Find the intersection of all sets in a list
    
    Example:
        find_all_intersections([{1, 2, 3}, {2, 3, 4}, {2, 3, 5}])
        # Returns {2, 3}
    """
    # TODO: Implement finding common elements across multiple sets
    pass


# ============================================================================
# TASK 4: Complex Data Structure Integration
# ============================================================================

def sort_students_by_gpa(students: List[Dict]) -> List[Dict]:
    """
    Sort list of student dictionaries by GPA (descending)
    
    Example:
        students = [
            {'name': 'Alice', 'gpa': 3.8},
            {'name': 'Bob', 'gpa': 3.6},
            {'name': 'Charlie', 'gpa': 3.9}
        ]
        # Returns sorted by GPA descending
    """
    # TODO: Implement sorting of dictionaries
    pass


def group_by_key(items: List[Dict], key: str) -> Dict[Any, List[Dict]]:
    """
    Group list of dictionaries by a specific key
    
    Example:
        items = [
            {'department': 'CS', 'name': 'Alice'},
            {'department': 'CS', 'name': 'Bob'},
            {'department': 'Math', 'name': 'Charlie'}
        ]
        group_by_key(items, 'department')
        # Returns {'CS': [{...}, {...}], 'Math': [{...}]}
    """
    # TODO: Implement grouping logic
    pass


def filter_and_transform(students: List[Dict], 
                         min_gpa: float, 
                         max_age: int) -> List[Dict]:
    """
    Filter students by GPA and age, then transform to include only name and gpa
    
    Example:
        students = [
            {'name': 'Alice', 'age': 20, 'gpa': 3.8},
            {'name': 'Bob', 'age': 25, 'gpa': 3.2}
        ]
        filter_and_transform(students, 3.5, 22)
        # Returns [{'name': 'Alice', 'gpa': 3.8}]
    """
    # TODO: Implement filtering and transformation
    pass


def aggregate_statistics(students: List[Dict]) -> Dict[str, float]:
    """
    Calculate aggregate statistics from student list
    
    Returns:
        {
            'average_gpa': float,
            'average_age': float,
            'max_gpa': float,
            'min_gpa': float
        }
    """
    # TODO: Implement statistics calculation
    pass


if __name__ == "__main__":
    # Example usage and testing
    print("Data Structures Assignment")
    print("==========================")
    
    # TODO: Add test code here to verify your implementations
    # Example:
    # numbers = [1, 2, 2, 3, 1, 4]
    # print(f"Removed duplicates: {remove_duplicates(numbers)}")
    # 
    # students = [("Alice", 30), ("Bob", 25)]
    # print(f"Sorted: {sort_by_multiple_criteria(students, 'age')}")
