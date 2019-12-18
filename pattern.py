def pattern(n):
    for i in n:
        print("|", end= "")
        print("*" * int(i))
n="12345"
pattern(n)

