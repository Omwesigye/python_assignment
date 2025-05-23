def add_numbers(x,y):
    result = x+y
    print('sum: ',result)
add_numbers(15,30)
    
def product_of_three(a, b, c):
    result = a*b*c
    print("The product is:", result)
product_of_three(5,6,7)

def get_stats(a,b):
    return a+b, a-b
sum_value, subtract_value = get_stats(20,12)

print('sum : ',sum_value)
print('subtract',subtract_value)


def divide_numbers(x, y):
    return(x/y)
result = divide_numbers(10, 2)
print("Result:", result)

def square(x): return x*x
print(square(5))

numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x* x, numbers))
print(squares)
