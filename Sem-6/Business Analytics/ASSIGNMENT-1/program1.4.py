import sqlite3
import pandas as pd

conn = sqlite3.connect("company.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS employees (
    EmployeeID TEXT PRIMARY KEY,
    Name TEXT,
    Department TEXT,
    Salary INTEGER
)
""")
conn.commit()

csv_file_path = "employee_data.csv"
df = pd.read_csv(csv_file_path)

df.to_sql("employees", conn, if_exists="replace", index=False)

print("Data successfully exported to the SQLite database.")

query = "SELECT * FROM employees LIMIT 10"
df_sql = pd.read_sql_query(query, conn)
print("\nSample Data from Database:")
print(df_sql)

conn.close()
