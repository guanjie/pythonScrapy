# Chap1_5.py - Write a method to replace all spaces in a string with '%20'


def main():
    string = "asdfffasde  asdfegasdf asdf    "
    print afterEncoding(string)


def afterEncoding(string):
    string = string.strip()
    string_list = string.split(' ')

    # Get new string_list with all items
    new_string_list = []
    for item in string_list:
        if item is not '':
            new_string_list.append(item)
            print item

    new_string = '%20'.join(new_string_list)
    return new_string

if __name__ == "__main__":
    main()
