# smol script to do an A-B set operation
# converting things into a set and just subtracting the ids
import pandas as pd

opus_files_df = pd.read_csv('opus_files_list.csv')
test_ids_df = pd.read_csv('test_ids.csv')

test_ids_set = set(test_ids_df['id_list'].str.strip(','))

opus_file_names = set(opus_files_df['File Name'])

missing_files = opus_file_names - test_ids_set

missing_files_df = pd.DataFrame({'Missing File Name': list(missing_files)})

missing_files_df.to_csv('missing_files2.csv', index=False)