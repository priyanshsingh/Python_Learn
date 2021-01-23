def table(a):
    print("Table of " + a + " is:")
    for i in range(1, 11):
        print(a*i)


print("Enter a number to print its table = ")
num = input()
table(num)
