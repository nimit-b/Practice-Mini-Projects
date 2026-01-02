import matplotlib.pyplot as plt

days = [1,2,3,4,5]
sales = [200,394,345,995,1050]

plt.plot(days, sales, color = "red", linestyle = "-.", marker = "o")
plt.xlabel("DAYS")
plt.ylabel("SALES")
plt.title("Days and Sales Graph")
plt.show()
