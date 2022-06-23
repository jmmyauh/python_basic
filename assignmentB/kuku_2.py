""" 
行数を入力してください: 4
列数を入力してください: 6
1 2 3 4 5 6 
2 4 6 8 10 12 
3 6 9 12 15 18 
4 8 12 16 20 24
"""
c = int(input("行数を選択してください:"))
k = int(input("列数を入力してください:"))

for i in range(1, c + 1):
    for j in range(1, k + 1):
        print(i * j, end=' ')
    print()
