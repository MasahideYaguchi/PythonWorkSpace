
import time
num = int(input('何匹数えますか？：'))

a = 1
while True:
 time.sleep(a * 0.8)
 print("羊が" + str(a) + "匹")
 a += 1
 if a > num:
      break