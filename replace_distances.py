import pandas as pd
from collections import Counter

# # Dropping MT560 and NUSA Columns
# # Load the CSV file
# df = pd.read_csv('src\\proxy_regressor\\csv_datasets\\nusa_experiments.csv')

# # Drop the columns
# columns_to_drop = ['phonological']  # replace with the columns you want to drop
# df = df.drop(columns=columns_to_drop)

# # Save the updated dataframe to a new CSV file
# df.to_csv('no_imputed_nusa_experiments.csv', index=False)

#MT560
# Specify the columns you want (by index or name)
columns_to_extract = [0, 1]  # For example, to extract the first and third columns (0-based index)

# Read the CSV file without headers
df = pd.read_csv('src\\proxy_regressor\\csv_datasets\\no_imputed_mt560_experiments.csv', header=None, usecols=columns_to_extract)

#89:95

# Convert specified columns to lists
langs = {f'Column_{i}': df[i].tolist() for i in range(df.shape[1])}

# Access the lists using the correct keys
source_langs = langs['Column_0'][1:]
target_langs = langs['Column_1'][1:]

distances = []
for i in range(len(source_langs)):
    distances.append([source_langs[i], target_langs[i]])

# Count occurrences of each pair
pair_counts = Counter(tuple(pair) for pair in distances)

# Print counts
pairs = []
for pair, count in pair_counts.items():
    pairs.append(pair)

# Specify the columns you want (by index or name)
columns_to_extract = [2, 3, 4, 5, 6]  # For example, to extract the first and third columns (0-based index)

# Read the CSV file without headers
df2 = pd.read_csv('mt560_distances.csv', header=None, usecols=columns_to_extract)

# Skip the first row if it contains headers
df2 = df2.iloc[1:]

# Convert specified columns to lists
distances = {
    f'Column_{i}': [float(item.strip('[]')) for item in df2.iloc[:, i].tolist()]
    for i in range(df2.shape[1])
}
 
distances_dict = {}
counter = 0
for pair in pairs:
    print(pair)
    distances_dict[pair] = [distances['Column_0'][counter], distances['Column_1'][counter], distances['Column_2'][counter], distances['Column_3'][counter], distances['Column_4'][counter]]
    counter += 1

# Read the CSV file without headers
df3 = pd.read_csv('src\\proxy_regressor\\csv_datasets\\no_imputed_mt560_experiments.csv')

# morphological_column = []
for index, row in df3.iterrows():
    counter = 0
    for pair in pairs:
        replacement_values = distances_dict.get(pair, [])

        if row[0] == pair[0] and row[1] == pair[1]:
            start_col = 89
            end_col = 89 + len(replacement_values)

            if end_col <= len(df3.columns):
                df3.loc[index, df3.columns[start_col:end_col]] = replacement_values
                # morphological_column.append(distances['Column_5'][counter])
                break
            else:
                print(f"Warning: Column slice {df3.columns[start_col:end_col]} is out of bounds for index {index}")
        counter += 1

# df3['morphological'] = morphological_column

# Save the modified DataFrame back to a CSV file
df3.to_csv('no_imputed_mt560_experiments', index=False)








# # Specify the columns you want (by index)
# columns_to_extract = [1, 2]  # For example, to extract the first and second columns (0-based index)

# # Read the CSV file without headers
# df = pd.read_csv('update_URIEL/uriel_glottocode_map.csv', header=None, usecols=columns_to_extract)

# # Convert specified columns to lists
# languages = {f'Column_{i}': df.iloc[:, i].tolist() for i in range(len(columns_to_extract))}

# # # Access the lists using the correct keys
# iso_codes = [l[0:3] if isinstance(l, str) and len(l) > 2 else '' for l in languages['Column_0']]
# glottocodes = [l[0:8] if isinstance(l, str) and len(l) > 2 else '' for l in languages['Column_1']]

# MT560_langs = [['sinh1246', 'stan1293'], ['stan1293', 'cebu1242'], ['stan1293', 'amha1245'], ['faro1244', 'stan1293'], ['stan1293', 'nucl1235'], ['stan1293', 'kirg1245'], ['stan1293', 'haus1257'], ['amha1245', 'stan1293'], ['stan1293', 'sind1272'], ['taga1270', 'stan1293'], ['stan1293', 'nucl1417'], ['stan1293', 'cent1989'], ['lomb1257', 'stan1293'], ['stan1293', 'ewee1241'], ['stan1293', 'sinh1246'], ['stan1293', 'tami1289'], ['egyp1253', 'stan1293'], ['stan1293', 'plat1254'], ['stan1293', 'luxe1241'], ['stan1293', 'mara1378'], ['kaza1248', 'stan1293'], ['stan1293', 'xhos1239'], ['zulu1248', 'stan1293'], ['mara1378', 'stan1293'], ['stan1293', 'kaza1248'], ['stan1293', 'panj1256'], ['nucl1235', 'stan1293'], ['xhos1239', 'stan1293'], ['nucl1305', 'stan1293'], ['stan1293', 'egyp1253'], ['nucl1310', 'stan1293'], ['java1254', 'stan1293'], ['stan1293', 'nucl1310'], ['tami1289', 'stan1293'], ['tata1255', 'stan1293'], ['stan1293', 'nucl1302'], ['stan1293', 'yoru1245'], ['stan1293', 'tata1255'], ['stan1293', 'taga1270'], ['stan1293', 'indo1316'], ['afri1274', 'stan1293'], ['indo1316', 'stan1293'], ['soma1255', 'stan1293'], ['yoru1245', 'stan1293'], ['stan1293', 'guja1252'], ['nucl1347', 'stan1293'], ['stan1293', 'wels1247'], ['bela1254', 'stan1293'], ['stan1293', 'occi1239'], ['wels1247', 'stan1293'], ['stan1293', 'nucl1305'], ['swat1243', 'stan1293'], ['stan1293', 'lomb1257'], ['guja1252', 'stan1293'], ['stan1293', 'afri1274'], ['stan1293', 'swat1243'], ['stan1293', 'zulu1248'], ['stan1293', 'bash1264'], ['ewee1241', 'stan1293'], ['cent1989', 'stan1293'], ['bash1264', 'stan1293'], ['stan1293', 'java1254'], ['stan1293', 'soma1255'], ['stan1293', 'sout2832'], ['plat1254', 'stan1293'], ['nucl1302', 'stan1293'], ['haus1257', 'stan1293'], ['stan1293', 'chha1249'], ['panj1256', 'stan1293'], ['stan1293', 'faro1244'], ['stan1293', 'turk1304'], ['cebu1242', 'stan1293'], ['stan1293', 'bela1254'], ['stan1293', 'kiny1244'], ['occi1239', 'stan1293'], ['sind1272', 'stan1293'], ['stan1293', 'maor1246'], ['kiny1244', 'stan1293'], ['shon1251', 'stan1293'], ['maor1246', 'stan1293'], ['turk1304', 'stan1293'], ['chha1249', 'stan1293'], ['sout2832', 'stan1293'], ['luxe1241', 'stan1293'], ['nucl1417', 'stan1293'], ['stan1293', 'shon1251'], ['kirg1245', 'stan1293'], ['stan1293', 'nucl1347']]
# NUSA_langs = [['bew', 'btk'], ['bew', 'ind'], ['bew', 'jav'], ['bew', 'mad'], ['bew', 'mak'], ['bew', 'min'], ['bew', 'sun'], ['btk', 'bew'], ['btk', 'ind'], ['btk', 'jav'], ['btk', 'mad'], ['btk', 'mak'], ['btk', 'min'], ['btk', 'sun'], ['ind', 'bew'], ['ind', 'btk'], ['ind', 'jav'], ['ind', 'mad'], ['ind', 'mak'], ['ind', 'min'], ['ind', 'sun'], ['jav', 'bew'], ['jav', 'btk'], ['jav', 'ind'], ['jav', 'mad'], ['jav', 'mak'], ['jav', 'min'], ['jav', 'sun'], ['mad', 'bew'], ['mad', 'btk'], ['mad', 'ind'], ['mad', 'jav'], ['mad', 'mak'], ['mad', 'min'], ['mad', 'sun'], ['mak', 'bew'], ['mak', 'btk'], ['mak', 'ind'], ['mak', 'jav'], ['mak', 'mad'], ['mak', 'min'], ['mak', 'sun'], ['min', 'bew'], ['min', 'btk'], ['min', 'ind'], ['min', 'jav'], ['min', 'mad'], ['min', 'mak'], ['min', 'sun'], ['sun', 'bew'], ['sun', 'btk'], ['sun', 'ind'], ['sun', 'jav'], ['sun', 'mad'], ['sun', 'mak'], ['sun', 'min']]

# for langs in MT560_langs:
#     list_index = MT560_langs.index(langs)
#     for lang in langs:
#         lang_index = langs.index(lang)
#         map_index = iso_codes.index(lang)
#         MT560_langs[list_index][lang_index] = glottocodes[map_index]

# for langs in NUSA_langs:
#     list_index = NUSA_langs.index(langs)
#     for lang in langs:
#         lang_index = langs.index(lang)
#         if lang == 'btk':
#             NUSA_langs[list_index][lang_index] = 'bima1247'
#         else:
#             map_index = iso_codes.index(lang)
#             NUSA_langs[list_index][lang_index] = glottocodes[map_index]

# NUSA
# # Specify the columns you want (by index or name)
# columns_to_extract = [2,3, 4, 5, 6, 7, 8]  # For example, to extract the first and third columns (0-based index)

# # Read the CSV file without headers
# df = pd.read_csv('nusa_midas_distances.csv', header=None, usecols=columns_to_extract)

# # Skip the first row if it contains headers
# df = df.iloc[1:]

# # Convert specified columns to lists
# distances = {
#     f'Column_{i}': [float(item.strip('[]')) for item in df.iloc[:, i].tolist()]
#     for i in range(df.shape[1])
# }
 
# distances_dict = {}
# counter = 0
# for category in ['genetic', 'geographic', 'syntactic', 'inventory', 'phonological', 'morphological', 'featural']:
#     specific_distances = []
#     for distance in distances['Column_' + str(counter)]:
#         for i in range(4):
#             specific_distances.append(distance)
#     distances_dict[category] = specific_distances
#     counter += 1

# df2 = pd.read_csv('src\proxy_regressor\csv_datasets\old_nusa_experiments.csv')

# for key in distances_dict:
#     df2[key] = distances_dict[key]

# # Save the modified DataFrame back to a CSV file
# df2.to_csv('nusa_experiments.csv', index=False)


#Removing Morphological Data from NUSA
# # Load the CSV file into a DataFrame
# df = pd.read_csv('src\proxy_regressor\csv_datasets\imputed_nusa_experiments_with_morphological.csv')

# # Drop the column(s) by name or index
# # To drop by column name
# df = df.drop(columns=['morphological'])

# # To drop by column index (e.g., remove the third column)
# # df = df.drop(df.columns[2], axis=1)

# # Save the modified DataFrame back to a CSV file
# df.to_csv('imputed_nusa_experiments_without_morphological.csv', index=False)