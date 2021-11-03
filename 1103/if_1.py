while True:
  input_string = input('好きな文字を入力してください：')
  if input_string == '':   
         break
if input_string.isnumeric():
    print('数字')
elif input_string.isalpha():
    print('アルファベット')
else:
        print('その他')