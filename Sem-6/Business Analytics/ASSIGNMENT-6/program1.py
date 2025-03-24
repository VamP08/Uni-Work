import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Line Plot
def line_plot():
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", 
             "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    sales = np.random.randint(5000, 20000, size=12)
    plt.figure(figsize=(10, 5))
    plt.plot(months, sales, marker='o', linestyle='-', color='b')
    plt.xlabel("Month")
    plt.ylabel("Sales (USD)")
    plt.title("Monthly Sales")
    plt.grid()
    plt.show()

# 2. Bar Chart
def bar_chart():
    subjects = ["Math", "Science", "English", "History", "Art"]
    scores = np.random.randint(50, 100, size=5)
    df = pd.DataFrame({"Subjects": subjects, "Scores": scores})
    plt.figure(figsize=(8, 5))
    sns.barplot(x="Subjects", y="Scores", data=df, palette="viridis")
    plt.title("Student Grades")
    plt.show()

# 3. Scatter Plot
def scatter_plot():
    height = np.random.randint(150, 200, 50)
    weight = np.random.randint(50, 100, 50)
    plt.figure(figsize=(8, 5))
    plt.scatter(height, weight, c='r', marker='x')
    plt.xlabel("Height (cm)")
    plt.ylabel("Weight (kg)")
    plt.title("Height vs Weight")
    plt.grid()
    plt.show()

# 4. Histogram
def histogram():
    salaries = np.random.randint(30000, 100000, 100)
    pd.Series(salaries).hist(bins=10, color='c', edgecolor='black')
    plt.xlabel("Salary")
    plt.ylabel("Frequency")
    plt.title("Salary Distribution")
    plt.show()

# 5. Pie Chart
def pie_chart():
    categories = ["Rent", "Food", "Transport", "Entertainment", "Savings"]
    expenses = [40, 20, 15, 10, 15]
    plt.figure(figsize=(7, 7))
    plt.pie(expenses, labels=categories, autopct="%.1f%%", 
            colors=["r", "g", "b", "y", "c"])
    plt.title("Expense Distribution")
    plt.show()

# Run all
if __name__ == "__main__":
    line_plot()
    bar_chart()
    scatter_plot()
    histogram()
    pie_chart()