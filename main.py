def calc(num, *args):
    if not args:
        return num
    else:
        z = ''
        if '+' in args:
            z = '+'
        elif '-' in args:
            z = '-'
        elif '*' in args:
            z = '*'
        elif '/' in args:
            z = '/'
        rez = int(eval(f'{num} {z} {args[0][0]}'))
        return rez
def zero(*args):
    if not args:
        return '0'
    return calc(0, args)
def one(*args):
    if not args:
        return '1'
    return calc(1, args)
def two(*args):
    if not args:
        return '2'
    return calc(2, args)
def three(*args):
    if not args:
        return '3'
    return calc(3, args)
def four(*args):
    if not args:
        return '4'
    return calc(4, args)
def five(*args):
    if not args:
        return '5'
    return calc(5, args)
def six(*args):
    if not args:
        return '6'
    return calc(6, args)
def seven(*args):
    if not args:
        return '7'
    return calc(7, args)
def eight(*args):
    if not args:
        return '8'
    return calc(8, args)
def nine(*args):
    if not args:
        return '9'
    return calc(9, args)
def plus(*args):
    d = f'+ {args[0]}'
    return d
def minus(*args):
    d = f'- {args[0]}'
    return d
def times(*args):
    d = f'* {args[0]}'
    return d
def divided_by(*args):
    d = f'/ {args[0]}'
    return d
print (eight(divided_by(three())))
print(four(plus(nine())))
print(eight(minus(three())))
print(six(times(two())))

