# 📘 Assignment: Data Structures in Python

## 🎯 Objective

Master Python's core data structures including lists, dictionaries, sets, and tuples. Learn when to use each structure, how to manipulate them efficiently, and solve real-world problems using the right data structure for each task.

## 📝 Tasks

### 🛠️ Lists and List Operations

#### Description
Work with Python lists to store, organize, and manipulate sequences of data. Implement functions that perform common list operations like sorting, searching, filtering, and transforming data.

#### Requirements
Completed program should:

- Create and initialize lists with different data types
- Perform list operations: append, insert, remove, pop, extend
- Implement list slicing and indexing
- Sort lists using `.sort()` and `sorted()` with custom keys
- Filter lists using list comprehensions and built-in functions
- Implement functions to find duplicates, remove duplicates, and reverse lists
- Use nested lists and iterate through them correctly
- Example usage:
  ```python
  numbers = [3, 1, 4, 1, 5, 9, 2, 6]
  remove_duplicates(numbers)  # Returns [3, 1, 4, 5, 9, 2, 6]
  ```

### 🛠️ Dictionaries and Key-Value Operations

#### Description
Use dictionaries to store and retrieve data using key-value pairs. Implement programs that organize data, count occurrences, and perform lookups efficiently.

#### Requirements
Completed program should:

- Create and initialize dictionaries with various key-value types
- Access, add, and update dictionary values
- Iterate through dictionary keys, values, and items
- Use `.get()`, `.keys()`, `.values()`, `.items()` methods
- Implement dictionary comprehensions
- Create nested dictionaries and access nested values
- Build a word frequency counter using dictionaries
- Implement functions to merge dictionaries and find common keys
- Handle missing keys gracefully with default values
- Example usage:
  ```python
  text = "hello world hello python"
  word_freq = build_frequency_dict(text)  # Returns {'hello': 2, 'world': 1, ...}
  ```

### 🛠️ Sets and Tuples with Advanced Operations

#### Description
Work with sets for unique data and efficient set operations, and use tuples for immutable data storage. Implement functions that leverage set properties and tuple unpacking.

#### Requirements
Completed program should:

- Create and initialize sets and tuples
- Perform set operations: union, intersection, difference, symmetric difference
- Use set methods: `.add()`, `.remove()`, `.discard()`, `.update()`
- Identify and remove duplicates using sets
- Implement functions using tuple unpacking and multiple assignment
- Create named tuples for structured data
- Understand when to use tuples vs lists (immutability, hashability)
- Find common elements between multiple collections
- Implement Venn diagram operations with sets
- Example usage:
  ```python
  set1 = {1, 2, 3, 4}
  set2 = {3, 4, 5, 6}
  find_common_elements(set1, set2)  # Returns {3, 4}
  ```

### 🛠️ Complex Data Structure Integration

#### Description
Combine multiple data structures to solve real-world problems and organize complex data patterns.

#### Requirements
Completed program should:

- Create and work with lists of dictionaries
- Build dictionaries with tuple keys and list values
- Implement functions that transform between different data structures
- Sort lists of dictionaries by multiple criteria
- Filter and group data using appropriate structures
- Build a student database using combined structures
- Implement search and aggregation functions
- Handle edge cases and validate data structure operations
