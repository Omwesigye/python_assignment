while True:
    try:

        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        result = num1 / num2
      
    except ValueError:
        print("Error: Please enter valid numbers .")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
        
    else:
        print("successful. ",result)
        break
    finally:
         print('run completed.\n')