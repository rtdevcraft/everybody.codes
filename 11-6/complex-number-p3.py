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

    new_x = int(x1 / x2)
    new_y = int(y1 / y2) 

    return (new_x, new_y)

def calculate_result(A):
    R = (0,0)
    for i in range(3):
        R = multiply_complex (R,R)
        R = divide_complex(R, (10,10))
        R = add_complex(R, A)
    return R

def generate_grid(A):
    points = []
    step = 10

    for row in range(101):
        y = A[1] + (row *step)

        for col in range(101):
            x = A[0] + (col * step)

            point = (x, y)
            points.append(point)

    return points

def visualize_grid(A):
    step = 10
    grid= []

    for row in range(101):
        row_chars = []
        y = A[1] + (row *step)

        for col in range(101):
            x = A[0] + (col * step)

            point = (x, y)

            if should_engrave(point):
                row_chars.append("#")
            else:
                row_chars.append(".")

        grid.append("".join(row_chars))

    for line in grid:
        print(line)
     
    



def should_engrave(point):
    R = (0, 0)
    
    for cycle in range(100):
        R = multiply_complex(R, R)
        R = divide_complex(R, (100000, 100000))
        R = add_complex(R, point)
        
        if abs(R[0]) > 1000000 or abs(R[1]) > 1000000:
            return False
    
   
    return True

# def count_engraved_points(A):
#     grid = generate_grid(A)
#     return sum(1 for point in grid if should_engrave(point))

def count_engraved_points(A):
    grid = generate_grid(A)
    count = 0
    
    for i, point in enumerate(grid):
        if should_engrave(point):
            count += 1
        
        
        if (i + 1) % 1000 == 0:
            print(f"Checked {i+1}/10201 points, engraved so far: {count}")
    
    return count

def count_engraved_points_large(A):
    step = 1  
    count = 0
    
    for row in range(1001):  
        y = A[1] + (row * step)
        
        for col in range(1001):  
            x = A[0] + (col * step)
            point = (x, y)
            
            if should_engrave(point):
                count += 1
        
        
        if (row + 1) % 100 == 0:
            print(f"Checked row {row + 1}/1001, engraved so far: {count}")
    
    return count

A = [-79745, -16616]
total = count_engraved_points_large(A)
print(f"\nFinal answer: {total}")
