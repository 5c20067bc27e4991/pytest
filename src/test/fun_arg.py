def func(name, age, sex=1, *args, **kargs):
    print(name, age, sex, args, kargs)


dic={'a'}
func('tanggu', 25,  'music', 'sport',x=99,y=100)
# tanggu 25 1 ('music', 'sport') {'class'=2}
