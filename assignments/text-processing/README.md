# 📘 Assignment: Python Text Processing

## 🎯 Objective

Master Python string manipulation, file I/O operations, and text processing techniques. Learn to read, parse, transform, and write text data while working with different file formats and applying various string methods.

## 📝 Tasks

### 🛠️ String Manipulation and Analysis

#### Description
Write functions that manipulate and analyze strings using Python's built-in string methods. Implement text transformation, searching, and pattern matching operations.

#### Requirements
Completed program should:

- Create a function to convert text to different cases (uppercase, lowercase, title case)
- Implement string searching and counting functionality (find occurrences of words)
- Write a function that removes punctuation and extra whitespace from text
- Create a word frequency counter that returns the most common words
- Implement a text reversal function
- Use string methods like `.split()`, `.strip()`, `.replace()`, `.find()`, and `.count()`
- Example usage:
  ```python
  text = "Hello, World! Hello Python."
  count_word("Hello", text)  # Returns 2
  ```

### 🛠️ File Input and Output Operations

#### Description
Work with files by reading text data, processing it, and writing results back to new files. Handle different file operations safely and work with file paths.

#### Requirements
Completed program should:

- Read text from an input file line by line
- Process each line and accumulate results
- Write processed data to an output file
- Implement error handling for missing or inaccessible files
- Use context managers (`with` statements) for file operations
- Create a function that counts lines, words, and characters in a file
- Implement a function that filters lines based on specific criteria
- Handle both relative and absolute file paths correctly

### 🛠️ Text Transformation and Data Extraction

#### Description
Build functions that extract meaningful data from text, transform text formats, and structure unstructured text data.

#### Requirements
Completed program should:

- Parse CSV-like data (comma or tab-separated values) into structured data
- Extract specific information from text (e.g., emails, phone numbers, URLs using string methods)
- Convert between different text formats (e.g., markdown to plain text)
- Implement a function that generates a summary or report from processed text
- Create functions that validate text input (e.g., check email format, validate phone numbers)
- Write processed data back to files in a structured format
- Test functions with sample text files and verify output correctness
