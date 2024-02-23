def addf(a,b):
    return a+b

class Test:
    def __init__(self,som_fun):
        self.funs = som_fun


testing = Test(addf)

print(testing.funs(2,2))