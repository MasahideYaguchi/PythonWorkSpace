DATA_FILENAME = 'word_list.txt'

word_dic = {}
with open(DATA_FILENAME) as f:
    # word_dic = {}
    for word in f:
        word = word.strip()
        if word in word_dic:
        # if word in word_dic.keys
            word_dic[word] += 1
        else:
            word_dic[word] = 1

print(word_dic)

