import pandas as pd
import csv

# Load the CSV file into a DataFrame
df = pd.read_csv('distances\\nusa_imputed_distances_cleaned.csv')

# Extract the first and second columns as lists
cleaned_source_langs = df.iloc[:, 0].tolist()
cleaned_target_langs = df.iloc[:, 1].tolist()

df2 = pd.read_csv("uriel_glottocode_map.csv")
mapping = dict(zip(df2.iloc[:, 2], df2.iloc[:, 1]))

for i, cleaned_source_lang in enumerate(cleaned_source_langs):
    if cleaned_source_lang in mapping:
        cleaned_source_langs[i] = mapping[cleaned_source_lang]

for i, cleaned_target_lang in enumerate(cleaned_target_langs):
    if cleaned_target_lang in mapping:
        cleaned_target_langs[i] = mapping[cleaned_target_lang]
        
cleaned_langs = []
for l in range(len(cleaned_source_langs)):
    cleaned_langs.append([cleaned_source_langs[l], cleaned_target_langs[l]])

# print(cleaned_langs[0])

input_file = 'experiment_csvs\with_SoftImpute\\new\\nusa_imputed_experiments.csv'
output_file = 'nusa_imputated_cleaned_experiments.csv'

# Open the input file for reading and the output file for writing
with open(input_file, mode='r', newline='') as infile, \
     open(output_file, mode='w', newline='') as outfile:
    
    reader = csv.reader(infile)
    writer = csv.writer(outfile)
    
    # Read the header and write it to the output file
    header = next(reader)
    writer.writerow(header)
    
    # Filter and write rows based on allowed entries
    for row in reader:
        if [row[0], row[1]] in cleaned_langs:
            writer.writerow(row)