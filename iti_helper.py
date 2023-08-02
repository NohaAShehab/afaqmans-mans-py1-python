

def askforInt(message):
    while True:
        num =  input(message)
        if num.isdigit():
            return  int(num)

        print("---- please enter valid number-------")



def sayhello():
    print("-- hello world --")


if __name__=='__main__':
    age = askforInt("please enter your age: ")
    print(age, type)