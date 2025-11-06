def add_complex(num1, num2):

    return (num1[0] + num2[0], num1[1] + num2[1])

def multiply_complex(num1, num2):
    x1 = num1[0]
    y1 = num1[1]
    x2 = num2[0]
    y2 = num2[1]

    new_x= x1 * x2 - y1 * y2
    new_y= x1 * y2 + y1 * x2

    return (new_x, new_y)

def divide_complex(num1, num2):
    x1 = num1[0]
    y1 = num1[1]
    x2 = num2[0]
    y2 = num2[1]

    new_x = x1 // x2
    new_y = y1 // y2

    return (new_x, new_y)

def calculate_result(A):
    R = (0,0)
    for i in range(3):
        R = multiply_complex (R,R)
        R = divide_complex(R, (10,10))
        R = add_complex(R, A)
    return R

A = (152, 57)
result = calculate_result(A)
print(result)
        
