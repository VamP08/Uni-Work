import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 50]

# Line plot
plt.plot(x, y, marker='o', linestyle='-', color='b', label='Line Graph')
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Sample Plot")
plt.legend()
plt.show()
