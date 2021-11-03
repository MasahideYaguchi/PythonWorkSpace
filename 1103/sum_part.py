input_num1 = int(input("数字1："))
input_num2 = int(input("数字2："))

my_sum = 0
for i in range(input_num1, input_num2+1):
    my_sum += i
print('{0}から{1}までの合計は{2}です'
.format(input_num1,input_num2,my_sum))