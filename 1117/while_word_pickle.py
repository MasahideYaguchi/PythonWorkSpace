import pickle
import os

FILE = 'word.pkl'

if os.path.isfile(FILE):

   with open(FILE, 'rb') as f:
    tan = pickle.load(f)
else:
    tan = []

    tan = []

while True:
 num = (input("単語を入力してください："))

 if num == "":
     print('終了します')
     break

 if num in tan:
     print('すでに登録済みです') #入力された値がリストに存在
     continue #続ける
 elif num =='LIST':
     print('単語リスト：',tan)  #単語リスト出力
     continue #続ける
 else: #リストに存在しない
     tan.append(num) #入力値をリストにつなげている


print('これまでに覚えた単語：',tan)

with open(FILE, 'wb') as f:
 pickle.dump(tan, f)
