def word_lower(string):
    #大文字小文字に変換
    return string.lower()

def delete_char(string):
    #スペースに置き換え
    ng_list = '.,:()"[]'
    for c in ng_list:
        string = string.replace(c,'')
    return string
def word_split(string):
    words = string.split(' ')
    return words
def remove_null(words_list):
    #空のkeyの要素削除する。辞書を返す。
    if '' in words_list:
        del words_list['']
    if '' in words_list:
        del words_list['']
    return words_list

DATA_FILENAME = 'sentence.txt'
word_dic = {} #空の辞書を作成｛｝
with open(DATA_FILENAME) as f:
    # word_dic = {} ここに書いてもいい
    for line in f:
        line = line.strip() #改行コードを取り除く
        line = word_lower(line)
        line = delete_char(line)
        print(line)
        words = word_split(line)
        for word in words:
            if word in word_dic: #辞書のキーに単語が存在するか?
        # if word in word_dic.keys(): #別の書き方
                word_dic[word] += 1 #カウントアップ
            else:
                word_dic[word] = 1 #初めての単語なので初期値１
        word_dic = remove_null(word_dic)

len_max = 0
for word in word_dic.keys():
    len_max = max(len_max, len(word))
for word in sorted(word_dic):
    print(f'{word:{len_max}}:{word_dic[word]}')
# for word in sorted(word_dic):
#     print(f'{word:}:{word_dic[word]}')
    print(word_dic)