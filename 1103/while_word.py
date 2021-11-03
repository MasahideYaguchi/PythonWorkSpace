tan = []

while True:
 num = (input("単語を入力してください："))

 if num == "":
     
     break
 if num in tan:
     print("すでに登録済みです")
 elif num =="LIST":
     print(tan)
 else:
     tan.append(num)

print(tan)