def calculate_average(numbers):
    if not numbers:  # Handle empty list case
        return 0  # Or raise an exception: raise ValueError("List cannot be empty")

    total = sum(numbers)
    average = total / len(numbers)
    return average

my_list = []
result = calculate_average(my_list)
print(f"The average is: {result}") #This will print 0

my_list = [1,2,3,4,5]
result = calculate_average(my_list)
print(f"The average is: {result}") #This will print 3.0