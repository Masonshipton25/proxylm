import csv

file_path = 'baseline_experiments_summary\\all_features\\NUSA\\Random\\Random_NLLB\\morph_midas_random_results_spBLEU_nllb_nusa_xgb.csv'

with open(file_path, mode='r') as file:
    reader = csv.reader(file)
    
    headers = next(reader)
    
    second_row = next(reader)
    
    unseen_dict = dict(zip(headers, second_row))

with open('baseline_experiments_summary\\all_features\\NUSA\\Random\\Random_NLLB\\morph_midas_random_nllb.txt', 'w') as f:
    for key, values in unseen_dict.items():
        f.write(f'{key}: {values}\n')