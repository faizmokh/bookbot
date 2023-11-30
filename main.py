import os
from collections import Counter

class Book:
    def __init__(self, contents):
        self.__contents = contents
        
    def get_words_count(self):
        """
        returns the number of words in the book.
        """
        return len(self.__contents.split())
    
    def get_letter_frequency(self):
        """
        returns a dictionary with the frequency of each letter in the book
        """
        letters_only = filter(str.isalpha, self.__contents.lower())
        return Counter(letters_only)

def generate_report(book, path_to_file):
    """
    returns a string with the report of the book
    """
    word_count = book.get_words_count()
    letter_frequency = book.get_letter_frequency()
    
    lines = []
    for char, count in sorted(letter_frequency.items(), key=lambda item: item[1], reverse=True):
        lines.append(f"The '{char}' character was found {count} times")
        
    report = "\n".join(lines)
    
    return f"""
    ---- Begin report of {path_to_file} ----
    {word_count} words found in the document.
    
    {report}
    --- End report ---
    """

def main():
    path_to_file = os.path.join("books", "frankestein.txt")
    with open(path_to_file) as f:
        file_contents = f.read()

        book = Book(file_contents)
        report = generate_report(book, path_to_file)
        print(report)
        
if __name__ == "__main__":
    main()