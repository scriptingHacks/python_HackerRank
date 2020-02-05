def count_substring(string, sub_string):
    string_len = len(string)
    found_places = []
    for n in range(string_len):
        index_found = string.find(sub_string, n, string_len)
        if index_found not in found_places and index_found is not -1:
            found_places.append(index_found)

    return len(found_places)

if __name__ == '__main__':
   print(count_substring("ABCDCDC", "CDC"))