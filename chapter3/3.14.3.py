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


def draw_graph(row1, row2, end_row1, end_row2, q_rows, q_columns):
    """Draw a graph
    
    row1: function that draws 1 type of line
    row2: function that draws 2 type of line
    end_row1: sign that ends the first type of line
    end_row2: sign that ends the second type of line
    q_rows: quatntity of rows in the graph
    q_columns: quantity of columns in the graph
    """
    for j in range(q_rows):
        # Draw a line by running function row1 "q_columns" times
        for i in range(q_columns):
            row1()
        print(end_row1)

        # Draw a line 4 times
        for i in range(4):
            # Draw a line by running function row2 "q_columns" times
            for k in range(q_columns):
                row2()
            print(end_row2)
    # Draw end line of the graph by running function row1 "q_columns" times
    for y in range(q_columns):
        row1()
    print(end_row1)

draw_graph(draw_plus_dash, draw_slash_blank, '+', '|', 2, 2)
# 2. Write a function that draws a similar grid with four rows and four columns.

draw_graph(draw_plus_dash, draw_slash_blank, '+', '|', 4, 4)
