def do_twice(f, s):
    f(s)
    f(s)

def print_spam(x):
    print(x)

do_twice(print_spam, 'spam')
