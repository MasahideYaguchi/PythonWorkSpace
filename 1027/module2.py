import sys
input_ = float(input('角度を入力してください（度）：'))

angle =  input_ * math.pi /180

print(f'{input_}度 -> {angle}ラジアン')
print(f'sin({input_} => {math.sin(angle)})')