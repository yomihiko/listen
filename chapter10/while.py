count = 0
while count < 10:
    print(count)
    count += 1

flg = True
while flg:
    user_input = input()
    if not user_input:
        flg = False
