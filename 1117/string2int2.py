def str2int(s):
 """list2int 文字列を数値に変換した値を返す（List 対応）"""
 if type(s) is str:
     if s.isnumeric():
      return str2int(s)
 elif type(s) is list:
      result = []
      for i in s:
          result.append(str2int(i))
      return result
 else:
      return None
print(str2int(['5','ab','100',10,1]))
print(str2int('100'))
print(str2int('xyz'))
