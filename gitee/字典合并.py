a = {"aaa":111,"bbb":222,"ccc":333}
b = {"ddd":444,"eee":555,"fff":666}

c = {**a,**b}

print(c)

class Cat:
    def __init__(self, name=None):
        self.name = name
    def __str__(self):
        return self.name
    def drink(self):
        print('drink')
cat = Cat('tom')
# cat.name = 'Jack'
print(f'我是小猫{cat},我的id是{id(cat)}',cat,cat.name)
cat.drink()


