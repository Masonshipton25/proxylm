import pandas as pd

# Specify the columns you want (by index or name)
columns_to_extract = [0, 1]  # For example, to extract the first and third columns (0-based index)
# or use column names: ['ColumnName1', 'ColumnName2']

# Read the CSV file without headers
df = pd.read_csv('src\\proxy_regressor\\csv_datasets\\nusa_experiments.csv', header=None, usecols=columns_to_extract)

# Convert specified columns to lists
langs = {f'Column_{i}': df[i].tolist() for i in range(df.shape[1])}

# Access the lists using the correct keys
source_langs = langs['Column_0'][1:]
target_langs = langs['Column_1'][1:]

distances = []
for i in range(len(source_langs)):
    distances.append([source_langs[i], target_langs[i]])

# Remove duplicates while preserving order
seen = set()
unique_distances = []
for item in distances:
    tuple_item = tuple(item)  # Convert list to tuple for hashability
    if tuple_item not in seen:
        seen.add(tuple_item)
        unique_distances.append(item)

print(unique_distances)