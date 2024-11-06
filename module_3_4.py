def single_root_words(root_word, *other_words):
    same_words = []

    for i in range(len(other_words)):
        root_word = root_word.lower()
        lowercase_words = [word.lower() for word in other_words]
        if root_word in lowercase_words[i] or lowercase_words[i] in root_word:
            same_words.append(other_words[i])
    return same_words


print(single_root_words('rich', 'Richest', 'orichalcum', 'cheers', 'riches'))
print(single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel'))
