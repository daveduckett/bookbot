import operator

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    char_count = get_char_count(text)
    print(text)
    display_report(word_count, char_count)

    

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_word_count(text):
    word_count = len(text.split())
    return word_count

def get_char_count(text):
    char_dictionary = {}
    for char in text.lower():
        if char not in char_dictionary.keys():
            count = 0
            for letter in text.lower():
                if char == letter:
                    count += 1
            char_dictionary[char] = count
    return char_dictionary


def display_report(w_count, c_count):
    c_count_list = []
    for c in c_count:
        if c.isalpha() == True:
            temp_c_dict = {c:c_count[c]}
            c_count_list.append(temp_c_dict)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{w_count} found in this documents")

    for c_dict in c_count_list:
        for key, value in c_dict.items():
            print(f"The {key} character was found {value} times")

    print("--- End report ---")


if __name__ == "__main__":
    main()