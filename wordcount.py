# put your code here.

def find_word_count(text_file):
    word_count_dict = {}
    test_file = open(text_file)

    for line in test_file:
        line = line.rstrip()
        word_list = line.split(' ')
        for word in word_list:
            word = word.rstrip(",").rstrip(".").rstrip("?").lower()
            word_count_dict[word] = word_count_dict.get(word, 0) + 1
            # if not word.isalpha():
            #     print(word)
            #     word = word.rstrip()
            #     print(word)
            #     word = word.lower()
            #     word_count_dict[word] = word_count_dict.get(word, 0) + 1
            # else:
            #     word = word.lower()
            #     word_count_dict[word] = word_count_dict.get(word, 0) + 1
            # ------------------------ ^ not the best way, do regular expressions
            # insead. In fact, reg express the whole thing p much
    print(word_count_dict)

    close(text_file)

# print(find_word_count("twain.txt"))
print(find_word_count("test.txt"))



