DATA_FILENAME = 'test.csv'

with open(DATA_FILENAME, 'r', encoding='utf-8') as f:
    person_data = []#一人分のリスト
    title = f.readline()#1行目の読み込み
    for line in f:#残りの行を読み込み
        line = line.strip()#行末の改行を取り除く
        person_data.append(line.split(','))#,で分割して格納

for data in person_data:#各人のデータを一人ずつ出力
    name, scores = data[0],data[1:]#名前と得点に分ける
    scores = [int(num) for num in scores]#文字列を数字に変換
    total = sum(scores)#合計を求める
    print(name,total)#一人分ずつ出力