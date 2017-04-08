#-*- encoding=UTF-8 -*-

def log(func):
    def wrapper():
        print 'before calling ', func.__name__
        func()
        print 'ending calling', func.__name__
    return wrapper

def hello():
    print 'hello'

if __name__ == '__main__':
    hello()