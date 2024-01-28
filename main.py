def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = count_words(text)
    letter_dict = count_characters(text)
    letter_list = dict_to_sorted_list(letter_dict)
    
    print("--- Begin report ---")
    print(f"{word_count} words found in the document")
    print(" ")
    
    for letter in letter_list:
         print(f"The '{letter}' character was found {letter_dict[letter]} times")

    print("--- End report ---")


def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents


def count_words(text):
     text_size = len(text.split())
     return text_size

def count_characters(text): 
    letter_count = {}

    for l in text:
        letter = l.lower()
        if not letter in letter_count:
            letter_count[letter] = 1
        else:
            letter_count[letter] += 1
    return letter_count


def dict_to_sorted_list(dict):
    letter_list = []
    for key in dict:
        if key.isalpha():
            letter_list.append(key)
    letter_list.sort()
    return letter_list


main()