class test():
    def __init__(self):
        self.a = 0

    def aa(self,par1):
        self.a += 1
    def bb(self):
        self.a += 2

num = test()
print(num.a)
num.aa(3)
print(num.a)
num.bb()
print(num.a)