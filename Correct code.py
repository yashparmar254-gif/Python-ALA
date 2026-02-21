print("Fibonacci Series Analyzer")

n = int(input("Enter limit: "))

a = 0
b = 1
count = 0
sum_total = 0

while count < n:
    print(a)
    sum_total = sum_total + a
    next_term = a + b
    a = b
    b = next_term
    count = count + 1

# Check whether sum is even or odd
if sum_total % 2 == 0:
    print("Even sum")
else:
    print("Odd sum")

print("Total Sum:", sum_total)

# Check size of series
if sum_total > 50:
    print("Large series")
else:
    print("Small series")

OUTPUT:-
Enter limit: 7
Fibonacci Series Analyzer
0
1
1
2
3
5
8
Even sum
Total Sum: 20
Small series
