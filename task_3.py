def my_func(arg1, arg2, arg3):
    print(f'Summ of 2 biggest arg is: {arg1 + arg2 + arg3 - min([arg1, arg2, arg3])}')
my_func(
    int(input('arg 1:')),
    int(input('arg 2:')),
    int(input('arg 3:')),
)