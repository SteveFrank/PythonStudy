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

def log__(func):
    def wrapper(*args, **kvargs):
        print 'before calling ', func.__name__
        print 'args : ' , args , ' , kvargs : ' , kvargs
        func(*args, **kvargs)
        print 'ending calling', func.__name__
    return wrapper

@log
def hello_function_1():
    print 'hello_1'
@log_
def hello_function_2(name):
    print 'hello_2', name
@log__
def hello_function_3(name, age):
    print 'name : ' , name, ' age : ' , age

if __name__ == '__main__':
    # hello_function_1()
    # hello_function_2('input name')
    hello_function_3('nowcoder', 12)
    print '==========================='
    hello_function_3(name='nowcoder', age=12)