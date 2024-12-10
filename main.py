from collections import Counter

def count_words(text):
    return len(text.split())

def count_characters(text):
    clean_text = "".join(char.lower() for char in text if char.isalpha())
    return Counter(clean_text)

def prepare_report(char_count):
    return [{"character": char, "count": count} for char, count in char_count.items()]

# Sorting function
def sort_on_count(item):
    return item["count"]

def print_report(text, file_path):
    word_count = count_words(text)
    char_count = count_characters(text)
    report = prepare_report(char_count)
    report.sort(key=sort_on_count, reverse=True)

    print(f"--- Begin report of {file_path} ---")
    print(f"{word_count} words found in the document.")
    for item in report:
        print(f"The '{item['character']}' character was found {item['count']} times.")
    print(f"--- End report ---")

# Read file and generate report
file_path = "books/frankenstein.txt"
with open(file_path) as f:
    file_contents = f.read()

print_report(file_contents, file_path)
