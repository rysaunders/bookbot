def main():
    with open("books/frankenstein.txt", "r") as f:
        file_contents = f.read()
        print(file_contents)

    words = count_words(file_contents)
    # count the letters
    letters = count_letters(file_contents)

    print_report(letters, words)


def count_words(text):
    words = text.split()
    return len(words)


def count_letters(text):
    # Create a dictionary to count letters
    letter_counts = {}
    
    # Count each letter
    for char in text.lower():
        if char.isalpha():
            letter_counts[char] = letter_counts.get(char, 0) + 1
    
    # Convert to list of dictionaries and sort
    letters = [{"char": char, "count": count} for char, count in letter_counts.items()]
    letters.sort(key=lambda x: x["count"], reverse=True)
    return letters


def print_report(letters, words):
    print("--- Report ---")
    print(f"{words} words found in the document")
    print(f"{len(letters)} letters found in the document")
    for letter_dict in letters:
        print(f"The '{letter_dict['char']}' character was found {letter_dict['count']} times")
    print("--- End of Report ---")


if __name__ == "__main__":
    main()