n=input("整数を入力してください")
total = 0
average = 0
num = int(n)
i = 0
while i <= num:
    total += i
    i += 1
average = total / num
print(f'1～{n}までの合計：{total}')
print(f'平均：{average}')