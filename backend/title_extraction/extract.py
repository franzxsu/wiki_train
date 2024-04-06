# https://data.sciencespo.fr/dataset.xhtml?persistentId=doi:10.21410/7E4/RDAG3O

import pandas as pd

#dataset found in link above (masyado malaki )
df = pd.read_csv('cross-verified-database.csv', encoding='latin-1')
df['name'] = df['name'].str.encode('latin-1').str.decode('utf-8')
filtered_df = df[df['list_wikipedia_editions'].str.contains('ilowiki') & df['list_wikipedia_editions'].str.contains('enwiki')]
selected_columns = ['name']
filtered_df[selected_columns].to_csv('clean_titles.csv', index=False, encoding='utf-8')
