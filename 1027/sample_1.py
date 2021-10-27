# while ループ
#  キーボードから入力→数値に変換
#  もし入力した値が 0 なら break
#  もし数値が 2 で割り切れたら
#  「偶数です」出力
#  そうでなければ
#  「奇数です」出力
while True:
    num = int(input("整数を入力してください (終了 -> 0)"))

    if num == 0:
        break

    if num % 2 == 0 :
        print("偶数です。")
    else:
        print("奇数です。")
    