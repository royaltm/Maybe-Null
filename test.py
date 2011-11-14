from maybe import Maybe, NullType, Value

class User(object):
    def __init__(self, name):
        self.name = name

    def fname(self):
        return self.name.split()[0]

users = { 1: User('Haskell Curry') }

def test(user):
    print
    for expr in ['repr(user)',
        'Maybe(user).name.capitalize()',
        'len(Maybe(user).name.capitalize())',
        'repr(Maybe(user).fname().capitalize())',
        'repr(unicode(Maybe(user).fname().capitalize()))', 
        'repr(not user)',
        'repr(bool(user))', 
        'repr(Value(Maybe(user)))',
        'repr(Value(Maybe(user).name) is None)',
        'repr(isinstance(user, NullType))',
        'repr(isinstance(Maybe(user), NullType))',
        'repr(isinstance(Maybe(user).name, NullType))',
        'repr(user==None)',
        'repr(Maybe(user)==None)',
        'repr(Maybe(user).name==None)',
        ]:
            print expr, ':=', eval(expr)

test(users.get(1))
test(users.get(2))
