import pandas as pd

# Load the CSV files
df1 = pd.read_csv('experiment_csvs\\with_SoftImpute\\new\\nusa_imputed_experiments.csv')  # The CSV file where you want to replace a column
df2 = pd.read_csv('experiment_csvs\\with_SoftImpute\\orig\\old_nusa_experiments.csv')  # The CSV file with the new column

# Replace the column (example: 'Column_to_replace' in df1 with 'New_column' in df2)
df1['genetic'] = df2['genetic']

# Save the updated DataFrame to a new CSV file
df1.to_csv('nusa_imputed_old_genetic_experiments.csv', index=False)