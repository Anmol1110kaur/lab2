"""
Python Text Processing Starter Code

This is a starter template for working with strings, file I/O, and text manipulation.
Implement the functions below to practice text processing skills.

Key concepts to implement:
- String methods and manipulation
- File reading and writing operations
- Text parsing and extraction
- Error handling for file operations
- Data transformation and structuring
"""

import os
from typing import List, Dict, Tuple


# ============================================================================
# TASK 1: String Manipulation and Analysis
# ============================================================================

def convert_to_uppercase(text: str) -> str:
    """Convert text to uppercase"""
    # TODO: Implement using string methods
    pass


def convert_to_lowercase(text: str) -> str:
    """Convert text to lowercase"""
    # TODO: Implement using string methods
    pass


def count_word_occurrences(word: str, text: str) -> int:
    """
    Count how many times a word appears in text (case-insensitive)
    
    Example:
        count_word_occurrences("hello", "Hello world, hello Python!")  # Returns 2
    """
    # TODO: Implement word counting
    pass


def remove_punctuation_and_whitespace(text: str) -> str:
    """
    Remove punctuation and normalize whitespace (multiple spaces to single space)
    
    Example:
        remove_punctuation_and_whitespace("Hello,  world!!!  ")  
        # Returns "Hello world"
    """
    # TODO: Implement using string methods (strip, replace, etc.)
    pass


def get_word_frequency(text: str, top_n: int = 5) -> Dict[str, int]:
    """
    Count word frequencies and return the top N most common words
    
    Example:
        text = "apple banana apple cherry banana apple"
        get_word_frequency(text, 2)  # Returns {'apple': 3, 'banana': 2}
    """
    # TODO: Split text into words, count occurrences, return top N
    pass


def reverse_text(text: str) -> str:
    """Reverse the text string"""
    # TODO: Implement text reversal
    pass


# ============================================================================
# TASK 2: File Input and Output Operations
# ============================================================================

def count_file_statistics(file_path: str) -> Dict[str, int]:
    """
    Read a file and return statistics: line count, word count, character count
    
    Returns:
        {"lines": int, "words": int, "characters": int}
    
    Note: Use context manager (with statement) for file handling
    """
    # TODO: Implement file reading and statistics calculation
    pass


def filter_lines_from_file(input_file: str, output_file: str, 
                          filter_func, *args) -> int:
    """
    Read from input_file, filter lines using filter_func, write to output_file
    
    Args:
        input_file: Path to input file
        output_file: Path to output file
        filter_func: Function that takes a line and returns True/False
        *args: Additional arguments to pass to filter_func
    
    Returns:
        Number of lines written to output_file
    
    Note: Handle file not found errors gracefully
    """
    # TODO: Implement file filtering with error handling
    pass


def read_file_safely(file_path: str) -> List[str]:
    """
    Read file and return list of lines, handling errors gracefully
    
    Returns:
        List of lines if successful, empty list if file not found
    """
    # TODO: Implement safe file reading with try-except
    pass


def write_to_file(file_path: str, content: str) -> bool:
    """
    Write content to file, creating the file if it doesn't exist
    
    Returns:
        True if successful, False if error occurred
    """
    # TODO: Implement file writing with error handling
    pass


# ============================================================================
# TASK 3: Text Transformation and Data Extraction
# ============================================================================

def parse_csv_line(line: str, delimiter: str = ",") -> List[str]:
    """
    Parse a CSV line into a list of values
    
    Example:
        parse_csv_line("John, 30, Engineer")  # Returns ["John", "30", "Engineer"]
    """
    # TODO: Split by delimiter and strip whitespace from each field
    pass


def extract_emails(text: str) -> List[str]:
    """
    Extract email addresses from text (simple pattern: word@word.word)
    
    Example:
        extract_emails("Contact: john@example.com or jane@test.org")
        # Returns ["john@example.com", "jane@test.org"]
    """
    # TODO: Implement email extraction using string methods
    # Hint: Look for @ symbol and common patterns
    pass


def extract_phone_numbers(text: str) -> List[str]:
    """
    Extract phone numbers from text (pattern: ###-###-#### or (###) ###-####)
    
    Example:
        extract_phone_numbers("Call 555-123-4567 or (555) 987-6543")
        # Returns ["555-123-4567", "(555) 987-6543"]
    """
    # TODO: Implement phone number extraction
    pass


def validate_email(email: str) -> bool:
    """
    Validate email format (simple check: contains @ and has text before/after)
    
    Example:
        validate_email("user@example.com")  # Returns True
        validate_email("invalid.email")     # Returns False
    """
    # TODO: Implement email validation
    pass


def generate_text_report(text: str) -> Dict[str, any]:
    """
    Generate a report with text statistics and analysis
    
    Returns:
        {
            "character_count": int,
            "word_count": int,
            "line_count": int,
            "average_word_length": float,
            "unique_words": int,
            "most_common_word": str
        }
    """
    # TODO: Implement text analysis and report generation
    pass


def process_text_file(input_file: str, output_file: str) -> bool:
    """
    Read from input file, clean and process text, write to output file
    
    Processing should include:
    - Remove punctuation
    - Normalize whitespace
    - Convert to lowercase
    - Generate word frequency count
    - Write cleaned text and statistics to output file
    
    Returns:
        True if successful, False if error occurred
    """
    # TODO: Implement complete text processing pipeline
    pass


if __name__ == "__main__":
    # Example usage and testing
    print("Text Processing Assignment")
    print("===========================")
    
    # TODO: Add test code here to verify your implementations
    # Example:
    # text = "Hello world, hello Python! HELLO everyone."
    # print(f"Word count: {count_word_occurrences('hello', text)}")
    # print(f"Uppercase: {convert_to_uppercase(text)}")
