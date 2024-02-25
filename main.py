def count_words(text: str) -> int:
    words = text.split()
    return len(words)

def count_letters(text: str):
    lower_text = text.lower()
    r = dict()
    for l in lower_text:
        if l in r:
            r[l] += 1
        else:
            r[l] = 1
    return r

def print_letters_for_book(book: str):
    letter_counts = count_letters(book)
    sorted_letters = sorted(letter_counts.keys())
    for letter in sorted_letters:
        if letter.isalpha():
            print(f'The \'{letter}\' was found {letter_counts[letter]} times')

def read_file(path: str) -> int:
    with open(path) as f:
        return f.read()

def print_book_report(book: str, name: str):
    print(f'--- {name} ---')
    print(f'{count_words(book)} words found in the document')
    print_letters_for_book(book)

def main() -> int:
    book = read_file('./books/frankenstein.txt')
    print_book_report(book, 'Frankenstein')
    return 0

main()
