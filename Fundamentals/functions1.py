def table(a):
    print("Table of " + str(a) + " is:")
    for i in range(1, 11):
        print(a*i)


print("Enter a number to print its table = ")
num = int(input())
table(num)
