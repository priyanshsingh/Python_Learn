def table(num):
    print("Table of " + num + " is:")
    for i in range(1, 11):
        print(num*i)
        i = i+1


print("Enter a number to print its table = ")
num = input()
table(num)
