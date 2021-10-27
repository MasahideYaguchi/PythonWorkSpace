fruits = ['バナナ','リンゴ','オレンジ']

while True:
 num = (input("果物をカタカナで入力してください："))

 if num == "":
     
     break
 if num in fruits:
     print(num + "は、知っています！")
 else:
     print(num + "は、知りませんでした。覚えておきます。")
     fruits.append(num)

print('知っている果物')
print(fruits)