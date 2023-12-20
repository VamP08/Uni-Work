def find_anagrams(word, word_list):
    return list(filter(lambda w: sorted(w) == sorted(word), word_list))

word = "rat"
word_list = ["car", "tar", "rat", "art", "star"]

anagrams = find_anagrams(word, word_list)

print("Anagrams of '{}' are: {}".format(word, ', '.join(anagrams)))
