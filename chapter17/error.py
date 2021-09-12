your_input = input("数値を入力＞")
try:
    number = int(your_input)
    print(10 / number)
except ValueError:
    print("は？")
except ZeroDivisionError:
    print("ゼロ徐算")