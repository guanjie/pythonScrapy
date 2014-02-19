# Check and see if two strings are anagrams
# ? string_list.sort() only returns Null, it's an action. No return


def main():
    string1 = "abcdefg"
    string2 = "cdefgabcg"
    print isAnagram(string1, string2)


def isAnagram(string1, string2):
    string_list1 = list(string1)
    string_list2 = list(string2)

# Sort function doesn't return
    string_list1.sort()
    string_list2.sort()
    return string_list1 == string_list2

if __name__ == "__main__":
    main()
