def calculator(a, b):
    try:
        return a/b
    except ZeroDivisionError as e:
        print(f'error')
print(calculator(int(input('input a: ')), int(input('input b: '))))