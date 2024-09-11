def replace_b_with_c(sentence):
    words = sentence.split()

    modified_words = []

    for word in words:
        modified_word = word.replace('b', 'c')
        modified_word = modified_word.replace('B', 'C')
        modified_words.append(modified_word)

    for word in modified_words:
        print(word)

sentence = "Bob brings beautiful butterflies"
replace_b_with_c(sentence)