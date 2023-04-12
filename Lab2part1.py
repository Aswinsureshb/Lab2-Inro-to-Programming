year = int(input("Enter the number of years: "))


for i in range(1,year+1):
 yearlytotal = 0
 for month in range(1,13):
    rainfall = float(input(f"Enter the rainfall in centimetres for month{month}: "))
    yearlytotal += rainfall
    TotalRainfall = 0
    
AverageMonthlyRainfall =  yearlytotal/12
TotalRainfall += yearlytotal
print(f"Total Rainfall:{TotalRainfall:.2f} cm")
print(f"Average Monthly Rainfall:{AverageMonthlyRainfall}")   
print(f"Overall total rainfall: {yearlytotal:.2f} cm")
print(f"Overall average monthly rainfall: {yearlytotal / (year * 12):.2f} cm")  
