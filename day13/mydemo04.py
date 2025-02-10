class Dog:
    def sleep(self):
        print("The dog is sleeping")

class Cat:
    def sleep(self):
        print("The cat is sleeping")

def animal(aaa):

    aaa().sleep()

if __name__ == '__main__':
    animal(Dog)