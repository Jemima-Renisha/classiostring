class IOstring:
    def __init__(self):
        self.str1 = ""
    def getinput(self):
        self.str1 = input("Enter a word:")
    def display(self):
        print("upper case:",self.str1.upper())


x = IOstring()
x.getinput()
x.display()