class NullMeta(type):
    def __instancecheck__(cls, instance):
        return instance is None

class NullType(object):
    __metaclass__ = NullMeta
    def __new__(cls, value, *p, **k):
        return value if value is not None \
            else object.__new__(cls, *p, **k)
    def __call__(self, *arg, **kw): return self
    def __getattr__(self, attr): return self
    def __getitem__(self, item): return self
    def __len__(self): return 0
    def __str__(self): return ''
    def __repr__(self): return 'Null'
    def __nonzero__(self): return False
    def __eq__(self, other): return isinstance(other, NullType)
    def __ne__(self, other): return not isinstance(other, NullType)

Maybe=NullType

def Value(value):
    return None if isinstance(value, NullType) else value
