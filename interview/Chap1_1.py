# Chapter1_1 questionn - return if a method contains all different chars
"""Use set datastructure to get the number of the set,
if they are the same then return the same"""


def main():
    string = 'abcdefghijklmnn'
    print isAllDifferent(string)


def isAllDifferent(string):
    string_set_num = len(set(string))
    string_length = len(string)
    return string_set_num == string_length


if __name__ == "__main__":
    main()
