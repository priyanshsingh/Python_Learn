def greeting(outro):
    print("Hey, Whats your name?")
    name = input()
    print("Hello there, " + name + " !, " + outro)


for i in range(0, 5):
    greeting("It was nice meeting you")
    i += 1
