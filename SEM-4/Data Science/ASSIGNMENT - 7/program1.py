import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

sns.set_theme()

books = pd.read_csv('ASSIGNMENT - 7/Books Good Reads Dataset.csv')
df = pd.DataFrame(books)
sorted_df = df.sort_values(by='Number of voters', ascending=False)

# Select the top 10 rows
top_10_books = sorted_df.head(10)

# Create a bar plot using Seaborn
plt.figure(figsize=(12, 8))
sns.barplot(x='Number of voters', y='Book', data=top_10_books, palette='viridis')
plt.title('Top 10 Books Based on Number of Voters')
plt.xlabel('Number of Voters')
plt.ylabel('Book')
plt.show()
