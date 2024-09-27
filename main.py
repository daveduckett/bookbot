def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    char_count = get_char_count(text)
    print(text)
    print(f"There are {word_count} words in this book")
    print(f"The character count in this book is as follows:\n {char_count}")
    

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
    



if __name__ == "__main__":
    main()