class myclass:
    __intvar=26;
    def __method(self):
        print("i am inside myclass")
    def meth(self):
        print("private variable=",myclass.__intvar)
obj=myclass()
obj.meth()
obj.__method