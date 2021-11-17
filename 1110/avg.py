DATA_FILENAME = 'test.csv'

with open(DATA_FILENAME, 'r', encoding='utf-8') as f:
    person_data = []#一人分のリスト
    title = f.readline().strip().split(',')#1行目の読み込み
    for line in f:#残りの行を読み込み
        person_data.append(line.strip().split(','))#,で分割して格納
print('person_dataは',person_data)
col = 1
avg = [0] * len(title)
while col < len(title):
     for score in person_data:
         avg[col] += int(score[col])/len(person_data)
col += 1

print(title[1:])#一人分ずつ出力
print(avg[1:])