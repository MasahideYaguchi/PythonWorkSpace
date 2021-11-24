DATA_FILENAME = 'word_list.txt'

word_dic = {} #空の辞書を作成｛｝
with open(DATA_FILENAME) as f:
    # word_dic = {} ここに書いてもいい
    for word in f:
        word = word.strip() #改行コードを取り除く
        if word in word_dic: #辞書のキーに単語が存在するか?
        # if word in word_dic.keys(): #別の書き方
            word_dic[word] += 1 #カウントアップ
        else:
            word_dic[word] = 1 #初めての単語なので初期値１
#練習４
#len_max = 0
#for word in word_dic.keys():
#  len_max = max(len_max, len(word))
#for word in sorted(word_dic):
#    print(f'{word:{len_max}}:{word_dic[word]}')
for word in sorted(word_dic):
    print(f'{word:}:{word_dic[word]}')
print(word_dic)

