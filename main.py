def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
   # print(f"{num_words} words found in the document \n")
   # print(f"Letter count: {get_letter_count(text)}")


    print("--- Begin report of books/frankenstein.txt --- \n\n")
    print(f"Number of words: {num_words} \n")

    letter_count = get_letter_count(text)
    for letter, count in letter_count.items():
        print(f"The {letter} was found {count} times")




def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_letter_count(text):
    lower_case_text = text.lower()
    letter_count = {}
    for letter in lower_case_text:
        if letter.isalpha():
            if letter in letter_count:
                letter_count[letter] += 1
            else:
                letter_count[letter] = 1

    return letter_count


    
    


main()
