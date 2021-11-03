tan = []

while True:
 num = (input("単語を入力してください："))

 if num == "":
     
     break
 if num in tan:
     print("すでに登録済みです")
 elif num =="LIST":
     print('単語リスト：',tan)
 else:
     tan.append(num)

print('これまでに覚えた単語：',tan)