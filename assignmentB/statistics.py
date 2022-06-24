"""
データを入力してください(スペース区切り) > 1 1 2 3 5 8 13 21
合計値: 54
最大値: 21
最小値: 1
平均値: 6
"""
# -*- coding: utf-8 -*-
"""
s = str(input("データを入力してください >").split(", "))
r = int(s)
sum = 0
for i in r:
    sum += s[i]
print(sum)
"""
# 合計値
s = input("データを入力してください >").split(" ")


def sum():
    sum_number = 0
    for r in range(0, len(s)):
        sum_number = sum_number + int(s[r])

    # input("データを入力してください >").split(", ")

    return sum_number


print("合計値:" + str(sum()))


# 最大値


def max():
    max = s[0]
    for r in range(1, len(s)):
        if max <= s[r]:
            max = s[r]
    return max


print("最大値:" + max())

# 最小値


def mini():
    mini = s[0]
    for r in range(1, len(s)):
        if mini >= s[r]:
            mini = s[r]
    print("最小値:" + mini)


mini()

# 平均値


def average_number():
    average = int(sum()) / len(s)
    print(f"平均値:{average}")


average_number()
