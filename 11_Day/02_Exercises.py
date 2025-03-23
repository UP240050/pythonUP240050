#1.
def evens_and_odds(n):
    if n < 0:
        return "Please enter a positive integer."
    even_count = 0
    odd_count = 0
    for digit in str(n):
        if int(digit) % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return f"Even digits: {even_count}, Odd digits: {odd_count}"
print(evens_and_odds(100))

#1.1
def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
print(factorial(5))

#1.2
def _is_empty_(param):
    if param is None:
        return True
    if isinstance(param, (str, list, tuple, dict, set)):
        return len(param) == 0
    return False

#1.3
import statistics

def calculate_mean(data):
    """Calculate the mean of a list of numbers."""
    if not data:
        return "List is empty."
    return sum(data) / len(data)

def calculate_median(data):
    """Calculate the median of a list of numbers."""
    if not data:
        return "List is empty."
    return statistics.median(data)

def calculate_mode(data):
    """Calculate the mode of a list of numbers."""
    if not data:
        return "List is empty."
    try:
        return statistics.mode(data)
    except statistics.StatisticsError as e:
        return str(e)  # Handle case where there is no unique mode

def calculate_range(data):
    """Calculate the range of a list of numbers."""
    if not data:
        return "List is empty."
    return max(data) - min(data)

def calculate_variance(data):
    """Calculate the variance of a list of numbers."""
    if not data:
        return "List is empty."
    return statistics.variance(data)

def calculate_std(data):
    """Calculate the standard deviation of a list of numbers."""
    if not data:
        return "List is empty."
    return statistics.stdev(data)

# Example usage:
data = [1, 2, 2, 3, 4]

print("Mean:", calculate_mean(data))          
print("Median:", calculate_median(data))     
print("Mode:", calculate_mode(data))          
print("Range:", calculate_range(data))        
print("Variance:", calculate_variance(data)) 
print("Standard Deviation:", calculate_std(data))  