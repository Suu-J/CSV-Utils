import pandas as pd

s3_file_list_df = pd.read_csv('s3_file_list3.csv')
conversation_ids_df = pd.read_csv('testCompare.csv')

# adding a new col
conversation_ids_df['Found'] = 'No'  # filling it with 'No'
counter = 1
# going through each ID in conversation_ids_df and check against s3_file_list_df
for index, row in conversation_ids_df.iterrows():
    print(counter)
    counter+=1
    # this is some n^2 logic lol
    if any(s3_file_list_df['Filename'].str.contains(row['Conversation ID'])):
        conversation_ids_df.at[index, 'Found'] = 'Yes'

# saving df to any one of the csvs
conversation_ids_df.to_csv('testCompare.csv', index=False)

print("Done")