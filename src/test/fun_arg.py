def func(name, age, sex=1, *args, **kargs):
    print(name, age, sex, args, kargs)


dic = {'a'}
func('tanggu', 25, 111, x=99, y=100)


# tanggu 25 1 ('music', 'sport') {'class'=2}


def t(a, *args, b=99, **kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)


# t(1, *(2, 3, 4), **{'x': 11, 'y': 22})
# t(1, *(2, 3, 4), b=000,x=11, y=22)
t(1, *(tuple('5,6,7'.split(','))), x=100, y=200)
