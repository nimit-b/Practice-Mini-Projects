import matplotlib.pyplot as plt

days = ["Mon", "Tue", "wed"]
sales = [500, 200, 900]

plt.bar(days, sales , color = "red")
plt.xlabel("Days")
plt.ylabel("Sales")
plt.title("Sales Per Day")

plt.show()


plt.plot(days, sales, color = "red", marker = "o", linestyle ="--")

plt.xlabel("Days")
plt.ylabel("Sales")
plt.title("Sales Per Day")

plt.show()
