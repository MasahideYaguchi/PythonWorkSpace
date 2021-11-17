def str2int(s):
 """str2int 文字列を数値に変換した値を返す"""
 if type(s) is str:
     if s.isnumeric():#数値かどうか確認
       return int(s)#true
     else:
       return 0
 else:
  return s #文字列ではなかった時
print(str2int('a'))
print(str2int('10'))
print(str2int(100))