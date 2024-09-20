def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    print(text)
    print(f"There are {word_count} words in this book")

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_word_count(text):
    word_count = len(text.split())
    return word_count

if __name__ == "__main__":
    main()