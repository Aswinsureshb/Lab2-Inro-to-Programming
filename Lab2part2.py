organism = int(input("Starting number of organisms:"))
percentage = float(input("Average daily percentage increase:"))
days = int(input("Enter the number of days to display the final data:"))
print("Day Approximate Population")
for days in range(organism, days + 2):
    add = organism * percentage/100
    organism = organism + add
    print(days-1, ' ', organism)

    # please enter small values as input like, organism = 2
    # percentage = 30
    # no: of days = 10