import json
import pandas as pd

with open("movies.json", "r") as file:
    movies_data = json.load(file)
    print(movies_data)

movies_df = pd.DataFrame(movies_data)
print(movies_df.head())

output_file_path = "movies_table.csv"
movies_df.to_csv(output_file_path, index=False)

print(f"Movies table saved to '{output_file_path}' successfully!")