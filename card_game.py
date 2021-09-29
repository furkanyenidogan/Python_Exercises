class A:
    def __init__(self):
        print('A.__init__')


class B(A):
    def __init__(self):
        super(B, self).__init__()
        print('B.__init__')

class C(A):
    def __init__(self):
        super(C, self).__init__()
        print('C.__init__')

class D(B, C):
    def __init__(self):
        super(D, self).__init__()
        print('D.__init__')

d = D()
