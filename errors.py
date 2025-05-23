try:
    result = 5/0
except ZeroDivisionError:
    print('cannt divide by zero')
else:
    print('division successful', result)
finally:
    print('run completed')
    
    
class  NotPositive(Exception):
    pass
def check_positive(num):
    if num<= 0:
        raise NotPositive('number must be positive')
    return num
try:
    print(check_positive(5))
    print(check_positive(-3))
except NotPositive as e:
    print('error',e)