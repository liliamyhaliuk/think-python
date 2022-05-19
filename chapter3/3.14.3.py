'''
Exercises of the book "Think python"
3.14.3 Exercises:
'''
# 1. Write a function that draws a grid like the following:
# + - - - - + - - - - +
# |         |         |
# |         |         |
# |         |         |
# |         |         |
# + - - - - + - - - - +
# |         |         |
# |         |         |
# |         |         |
# |         |         |
# + - - - - + - - - - +

def draw_plus_dash():
    print('+ - - - - ', end='')

def draw_slash_blank():
    print('|         ', end='')

def do_twice(func, arg1='', arg2=''):
    '''Do function twice (depends on the amount of arguments)'''
    if arg1:
        func(arg1)
        func(arg1)
    else:
        func()
        func()

def make_line(func, end_sign=''):
    '''Do function twice and put the sign in the end'''
    do_twice(func)
    if end_sign:
        print(end_sign)

def do_four(f, arg1, arg2=''):
    '''Do function four times'''
    f(arg1, arg2)
    f(arg1, arg2)
    f(arg1, arg2)
    f(arg1, arg2)

def draw_graph():
    '''Draw a graph with 2 rows and 2 columns'''
    make_line(draw_plus_dash, '+')
    do_four(make_line, draw_slash_blank, '|')
    make_line(draw_plus_dash, '+')
    do_four(make_line, draw_slash_blank, '|')
    make_line(draw_plus_dash, '+')

draw_graph()

# 2. Write a function that draws a similar grid with four rows and four columns.

def draw_4_graphs():
    '''Draw a graph with 4 rows and 4 columns'''
    do_twice(make_line, draw_plus_dash)
    print('+')
    do_twice(make_line, draw_slash_blank)
    print('|')
    do_twice(make_line, draw_slash_blank)
    print('|')
    do_twice(make_line, draw_slash_blank)
    print('|')
    do_twice(make_line, draw_slash_blank)
    print('|')
    
    do_twice(make_line, draw_plus_dash)
    print('+')
    do_twice(make_line, draw_slash_blank)
    print('|')
    do_twice(make_line, draw_slash_blank)
    print('|')
    do_twice(make_line, draw_slash_blank)
    print('|')
    do_twice(make_line, draw_slash_blank)
    print('|')
    do_twice(make_line, draw_plus_dash)
    print('+')

draw_4_graphs()
