numbers = [3, 7, 10, 15, 20]

while True:
    answer = input("数字を入力してください('q'で終了)：")

    if answer == "q":
        break

    try:
        answer = int(answer)

        if answer in numbers:
            print("正解")
        else:
            print("不正解")

    except ValueError:
        print("数字か'q'を入力してください")
