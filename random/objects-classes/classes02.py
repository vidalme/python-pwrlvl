class ITpro:
    def __init__(self,name,age,current_employed,seniority):
        self.name = name
        self.age = age
        self.current_employed = current_employed
        self.seniority = seniority

class Developer(ITpro):
    def __init__(self):
        pass

class Operational(ITpro):
    def __init__(self):
        pass

class DevOps(ITpro):
    def __init__(self, name,age,current_employed,seniority,current_task):
        super().__init__(name,age,current_employed,seniority)
        self.current_task = current_task

class Skill:
    def iac(self):
        print('this dude can Infra as code!')
    def  linux(self):
        print('i can linux all day!')
    def cicd(self):
        print('i can do such a nasty pipeline')


do1 = DevOps('Andre',29,False,'Jr', Skill().iac)
print(vars(do1))
do1.current_task()
print()
