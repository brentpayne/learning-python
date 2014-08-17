class A(object):
    def __init__(self, v, *args, **kwargs):
        print "A:init:v[{0}]".format(v)
        kwargs['v']=v
        super(A, self).__init__(*args, **kwargs)
        self.v = v


class MixInF(object):
    def __init__(self, *args, **kwargs):
        print "IObject:init"
    def f(self, y):
        print "IObject:y[{0}]".format(y)


class B(MixInF):
    def __init__(self, v, *args, **kwargs):
        print "B:init:v[{0}]".format(v)
        kwargs['v']=v
        super(B, self).__init__(*args, **kwargs)
        self.v = v
    def f(self, y):
        print "B:f:v[{0}]:y[{1}]".format(self.v, y)
        super(B, self).f(y)


class C(MixInF):
    def __init__(self, w, *args, **kwargs):
        print "C:init:w[{0}]".format(w)
        kwargs['w']=w
        super(C, self).__init__(*args, **kwargs)
        self.w = w
    def f(self, y):
        print "C:f:w[{0}]:y[{1}]".format(self.w, y)
        super(C, self).f(y)


class Q(C,B,A):
    def __init__(self, v, w):
        super(Q, self).__init__(v=v, w=w)
    def f(self, y):
        print "Q:f:y[{0}]".format(y)
        super(Q, self).f(y)


class Q1(A,B,C):
    def __init__(self, v, w):
        super(Q1, self).__init__(v=v, w=w)
    def f(self, y):
        print "Q1:f:y[{0}]".format(y)
        super(Q1, self).f(y)


class Q2(C,A,B):
    def __init__(self, v, w):
        super(Q2,self).__init__(v=v, w=w)
    def f(self, y):
        print "Q2:f:y[{0}]".format(y)
        super(Q2,self).f(y)

q = Q(5,6)
q.f(7)

q1 = Q1(5,6)
q1.f()

q2 = Q2(5,6)
q2.f()
