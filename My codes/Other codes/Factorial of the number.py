#Factorial of a number optimal solution
#suppose 36 
#1 ---- 36  we can see 36/1=36 so 1 and 36 both will be factorial
#2 ---- 18  likewise 36/2=18 so 2 and 18 both will be factorial
#3 ---- 12  simillarly 36/3=12 then 3 and 12 both will be factorial
#4 ---- 9   hence we can say number divisor and qoutient both will be factors of the number
#6 ---- 6   so this will continue till we find the square root of the same number
import math
def print_factors(n):
    factors = []
    for i in range(1, int(math.sqrt(n)) + 1):
        if n% i == 0:
            factors. append (i)
            if n/i !=i:
                factors. append (int(n / i))
    print(factors)
print_factors(21)