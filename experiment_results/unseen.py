import csv

file_path = 'experiment_results\mf_nusa_imputated_unseen_nllb.csv'

with open(file_path, mode='r') as file:
    reader = csv.reader(file)
    
    headers = next(reader)
    
    # Skip the second row
    next(reader)
    
    third_row = next(reader)
    
    unseen_dict = dict(zip(headers, third_row))

with open('mf_nusa_imputated_unseen_nllb.txt', 'w') as f:
    sum_se = 0
    size = 0
    for key, values in unseen_dict.items():
        if 'rmse_se' in key and key != 'cv_rmse_se' and values != '':
            sum_se += float(values)
            size += 1
            print(key)
        f.write(f'{key}: {values}\n')
    average_se = 0
    if size > 0:
        average_se = sum_se/size
    print(f'Average se: {average_se}')