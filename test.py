from maybe import Maybe, NullType, Value

def test_maybe():
    someobj = "Some String"
    assert Maybe(someobj) is someobj
    assert Maybe(someobj).split()[0] == "Some"
    assert str(Maybe(someobj).split()[0]) == "Some"
    assert len(Maybe(someobj).split()[0]) == 4
    someobj = None
    assert Maybe(someobj) == None
    assert Value(Maybe(someobj)) is None
    assert Maybe(someobj).split()[0] == None
    assert len(Maybe(someobj).split()[0]) == 0
    assert str(Maybe(someobj).split()[0]) == ''
    assert (Maybe(someobj).split()[0] or 'default') == 'default'
    assert bool(Maybe(someobj).split()[0]) == False
    assert (not Maybe(someobj).split()[0]) == True
    print 'ok'

class User(object):
    def __init__(self, name):
        self.name = name

    def fname(self):
        return self.name.split()[0]

users = { 1: User('Haskell Curry') }

def info(user):
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

test_maybe()
info(users.get(1))
info(users.get(2))
