users = ["Bob", "Tom", "Ken"]

int_number = [1, 2, 3, 4, 5]

bob_info = ["Bob", "Dylan", 79]

# 次のmembersというリストから "Bob" と "Tom" を取得して出力してください
members = ["Bob", "Tom", "Ken"]
print(members[0])
print(members[1])

# 次のリストを利用して、"Name: Bob Dylan, Age: 79"と出力してください
bob_info = ["Bob", "Dylan", 79]
print("Name:" + bob_info[0] + " " + bob_info[1] + " Age" + str(bob_info[2]))

# for を使って odd_numbers の各要素を出力してください
for odd_numbers in range(1, 10, 2):
    print(odd_numbers)

# for を使って even_numbers のそれぞれの値を2倍した値を出力してください
for even_numbers in range(1, 9):
    if even_numbers % 2 == 0:
        print(even_numbers)

# users_info を使って次のような出力をしてください
users_info = [["Bob", 79], ["Tom", 59], ["Ken", 61]]

for i in range(3):
    print("Name:" + users_info[i][0] + "," + "age:" + str(users_info[i][1]))

# 下記のコードが期待通り動作するような辞書を定義してください
bob_info = {"first_name": "Bob", "family_name": "Dylan", "age": 79}

print(bob_info["first_name"])  # "Bob"
print(bob_info["family_name"])  # "Dylan"
print(bob_info["age"])  # 79

# print(dice()) # 1から6の整数をランダムに出力する
import random


def dice():
    return random.randint(1, 6)


print(dice())
