def find_anagram(word, l):
    return list(filter(lambda x: sorted(word) == sorted(x), l))
    # anagrams = []
    # for w in l:
    #     if sorted(word) == sorted(w):
    #         anagrams.append(w)
    # return anagrams


print(find_anagram("abba", ["baba", "daca", "dbae", "abab", "daba"]))

