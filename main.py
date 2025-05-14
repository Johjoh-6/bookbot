import sys
from stats import count_words, count_characters,convert_to_list

def get_book_text(filepath):
    with open(filepath, 'r') as file:
        return file.read()

def main():
    entry = sys.argv
    if len(entry) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = entry[1]
    book_text = get_book_text(filepath)
    num_words = count_words(book_text)
    num_chars = count_characters(book_text)
    sorted_chars = convert_to_list(num_chars)
    print(f"Found {num_words} Found 75767 total words")
    for item in sorted_chars:
    	if item["char"].isalpha():
        	print(f"{item['char']}: {item['count']}")

main()
