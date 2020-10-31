# Create a function named divisors/Divisors that takes an integer n > 1 and returns an array with all of the integer's
# divisors(except for 1 and the number itself), from smallest to largest. If the number is prime return the string
# (integer) is prime' (null in C#) (use Either String a in Haskell and Result<Vec<u32>, String> in Rust).

def divisors(integer):
    array1 = []
    y = 2
    for y in range(2, integer):
        if integer % y == 0 and y < integer:
            array1.append(y)
            y += 1
        else:
            y += 1
    if len(array1) == 0:
        return f"{integer} is prime"
    return array1

divisors(13)


