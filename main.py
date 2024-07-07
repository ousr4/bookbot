def main():
    book = "books/frankenstein.txt"
    with open(book) as f:
        file_contents = f.read()
        num_words = count_words(file_contents)
        num_chars = count_characters(file_contents)
        num_chars = convert(num_chars)
        print_report(book, num_words, num_chars)


def count_words(content):
    words = content.split()
    return len(words)


def count_characters(content):
    char_dict = {}
    for word in content:
        lower_word = word.lower()
        for char in lower_word:
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1
    return char_dict


def convert(num_chars):
    chars = []
    for char in num_chars:
        if char.isalpha():
            chars.append({"letter": char, "num": num_chars[char]})
    chars.sort(reverse=True, key=sort_on)
    return chars


def sort_on(dict):
    return dict["num"]


def print_report(book, num_words, num_chars):
    print(f"--- Begin report for book {book} ---")
    print(f"{num_words} words found in the document")
    print("")
    for dict in num_chars:
        print(dict)
        char = dict["letter"]
        num = dict["num"]
        print(f"The {char} character was found {num} times")
    print("--- End report ---")


main()
