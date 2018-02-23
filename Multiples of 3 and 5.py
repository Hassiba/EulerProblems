# Problem 1:
#  If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum
# of these multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000.

lower = int(input("Enter lower range: "))
upper = int(input("Enter upper range: "))

total =0
for i in range(lower, upper):
    if i % 3 == 0 or i % 5 == 0:
        total = total + i

print("The sum of all the multiples of 3 or 5 from ", lower, "to", upper, "is:", total)