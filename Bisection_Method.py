import math

def evaluate_function(func_str, x):
    return eval(func_str)

def bisection_method(func_str, a, b, tol=0.0100):
    if evaluate_function(func_str, a) * evaluate_function(func_str, b) >= 0:
        print("The function must have different signs at the endpoints a and b.")
        return None 

    # Initialize midpoint
    midpoint = (a + b) / 2.0
    Counter = 0
    
    while abs(evaluate_function(func_str, midpoint)) > tol:
        f_a = evaluate_function(func_str, a)
        f_b = evaluate_function(func_str, b)
        f_mid = evaluate_function(func_str, midpoint)
        
        # Print current state
        print(f"Counter {Counter}: a = {a:.4f}, b = {b:.4f}, c = {midpoint:.4f}, f(a) = {f_a:.4f}, f(b) = { f_b:.4f}, f(c) = {f_mid:.4f} ")
        
        if f_mid == 0:
            return midpoint  
        elif f_a * f_mid < 0:
            b = midpoint  # Update b to midpoint
        else:
            a = midpoint  # Update a to midpoint
        
        # Update midpoint for next Counter
        midpoint = (a + b) / 2.0
        Counter += 1

    # Final output of the Counter
    print(f"Final Counter: a = {a:.4f}, b = {b:.4f}, c = {midpoint:.4f}, f(a) = {f_a:.4f}, f(b) = { f_b:.4f}, f(c) = {f_mid:.4f} ")
    
    return midpoint  

# Input function from user
func_input = input("Enter a function of x : ")
a = float(input("Enter the left endpoint of the interval (a): "))
b = float(input("Enter the right endpoint of the interval (b): "))

root = bisection_method(func_input, a, b)
print(f"Root found: {root:.4f}")