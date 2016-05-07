x = 10
while x > 0:
    print(x)
    x=x-1
print('Done')

input_value = raw_input("Enter: ")
n = int(input_value)
result = 1
while n > 1:
    result = result * n
    n = n - 1
print("Factorial of " + input_value + " is: " )
print(result)
