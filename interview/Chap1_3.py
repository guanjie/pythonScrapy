# Chap1_3 Design algorithm to remove the duplicated chars in a string
## Changed the question to find the index of the string that we want to remove


def main():
    string = "Eric is the maan"
    print removeDuplicatedChars(string)


def removeDuplicatedChars(string):
    string_list = list(string)

    char_dict = dict()
    index_removed = []

    for index in xrange(len(string_list)):
        index_char = string_list[index]
        if index_char not in char_dict:
            char_dict[index_char] = 1
        else:
            index_removed.append(index)
    return index_removed


if __name__ == "__main__":
    main()
