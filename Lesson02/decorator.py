#-*- encoding=UTF-8 -*-

def log(func):
    def wrapper():
        print 'before calling ', func.__name__
        func()
        print 'ending calling', func.__name__
    return wrapper

def log_(func):
    def wrapper(name):
        print 'before calling ', func.__name__
        func(name)
        print 'ending calling', func.__name__
    return wrapper

@log
def hello_function_1():
    print 'hello_1'
@log_
def hello_function_2(name):
    print 'hello_2', name


if __name__ == '__main__':
    # hello_function_1()
    hello_function_2('input name')