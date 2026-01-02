import matplotlib.pyplot as plt
import numpy as np

days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
sales = [2200, 2039, 1099, 1983, 1934, 2928, 3029]
color = []
print(np.mean(sales))
for i in range(0,len(sales)):
    if np.mean(sales) < sales[i]:
                     color.append("Green")
    elif np.mean(sales) >= sales[i]:
                     color.append("yellow")
    else:
        color.append("red")
plt.bar(days, sales, color = color)
plt.xlabel("Sales")
plt.ylabel("Days")
plt.show()
