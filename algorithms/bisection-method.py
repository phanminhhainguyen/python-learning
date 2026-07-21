def square_root_bisection(number, tolerance = 0.01, max_iterations = 100):
    if number < 0:
        raise ValueError("Square root of negative number is not defined in real numbers")
    if number == 0 or number == 1:
        print(f"The square root of {number} is {number}")
        return number
    low = 0
    high = max(1, number)
    for _ in range(max_iterations):
        midpoint = (low + high) / 2
        square = midpoint*midpoint
        if (high - low) < tolerance:
            print(f"The square root of {number} is approximately {midpoint}")
            return midpoint 
        if square < number:
            low = midpoint
        else:
            high = midpoint
        

    print(f"Failed to converge within {max_iterations} iterations")
    return None

        