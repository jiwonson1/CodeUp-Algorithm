ingredients = ["x 25", "y 35", "a 20", "q 80"]
# 300는 이윤 / - (0)
menu = ["pizza xxyy 300", "lemon yy 200"
        "watter xx 100", "burger xy 300"]
sell = ["pizza 3", "burger 4"]
dic = {}
# 총 가격 이윤을 구하시오

dic = dict(kv.split(' ') for kv in ingredients)
menu_arr = list(kv.split(' ') for kv in menu)
sell_arr = list(kv.split(' ') for kv in sell)

answer = 0
s = 0
for i in range(len(sell)):
    temp = ''
    price = 0
    for j in range(len(menu)):
        if sell_arr[i][0] == menu_arr[j][0]:
            #xxyy
            print(sell_arr[i][0])
            temp = menu_arr[j][1]
            for t in temp:
              price += int(dic[t])
            price = int(menu_arr[j][2]) - price
            answer += price * int(sell_arr[i][1])
print(answer)
