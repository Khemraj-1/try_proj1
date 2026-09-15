def find_smallest(numbers):
    """Returns the smallest number from a list of numbers."""
    if not numbers:
        raise ValueError("List cannot be empty")
    return min(numbers)

# Example Usage
my_list = [41, 12, 3, 74, 15]
smallest = find_smallest(my_list)
print(smallest)  # Output: 3   
