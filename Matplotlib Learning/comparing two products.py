import matplotlib.pyplot as plt

days = [1,2,3,4,5]
product_a = [230,190,203,100,198]
product_b = [233,188,103,293,109]

plt.plot(days, product_a, label = "Product A")
plt.plot(days, product_b, label = "Product B")


plt.xlabel("Day")
plt.ylabel("Sales")
plt.title("Sales Comparison")
plt.legend()
plt.show()
