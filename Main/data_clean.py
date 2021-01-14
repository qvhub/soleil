import pandas as pd
import os
from IPython.display import display

def first4(text):
    return text[:4]

my_dir = '../render'
my_files = os.listdir(my_dir)

list_col_cloud = []

# recuperation du premier csv pour récupérer la liste des jours du scraping
df = pd.read_csv(my_dir + '/' + my_files[0], index_col=0)
df = df.drop(['cloud', 'temp_max', 'temp_min'], axis=1)

# Recup des csv dans le dossier render
for i in my_files:
    df_t = pd.read_csv(my_dir + '/' + i, index_col=0)

    # convertion du type de temps en int
    for zero in ['thunderstorm', 'tornado', 'rain snow', 'heavy rain']:
        df_t.loc[df_t['cloud'] == zero, 'cloud'] = 0

    for one in ['cloudy', 'foggy', 'flurries', 'rain']:
        df_t.loc[df_t['cloud'] == one, 'cloud'] = 1

    for two in ['mostly cloudy', 'scattered showers', 'snow']:
        df_t.loc[df_t['cloud'] == two, 'cloud'] = 2

    for three in ['partly cloudy']:
        df_t.loc[df_t['cloud'] == three, 'cloud'] = 3

    for four in ['mostly sunny']:
        df_t.loc[df_t['cloud'] == four, 'cloud'] = 4

    letters = first4(i)

    new_cloud = 'cloud' + '_' + letters
    new_temp_max = 'temp_max' + '_' + letters
    new_temp_min = 'temp_min' + '_' + letters

    list_col_cloud.append(new_cloud)

    df_t = df_t.rename(columns={"cloud": new_cloud})
    df_t = df_t.drop(['temp_max', 'temp_min'], axis=1)
    df = pd.merge(df, df_t, on='current_day', how='left')


df[list_col_cloud] = df[list_col_cloud].apply(pd.to_numeric)
df['clound_min'] = df[list_col_cloud].min(axis=1)
df['clound_max'] = df[list_col_cloud].max(axis=1)
df['clound_std'] = df[list_col_cloud].std(axis=1)
df['clound_median'] = df[list_col_cloud].median(axis=1)

df = df.drop(list_col_cloud, axis=1)

outdir = '../data'
if not os.path.exists(outdir):
    os.mkdir(outdir)

file_name = f"result_data_weather"

fullname = os.path.join(outdir, f"{file_name}.csv")

df.to_csv(fullname)


'''for i in range(0, 731):
    print(df.iloc[i].min())'''


# 0
# thunderstorm, tornado, rain snow, heavy rain

# 1
# cloudy, foggy, flurries, rain

# 2
# # mostly cloudy, scattered showers, snow

# 3
# partly cloudy

# 4
# mostly sunny

# 5
# Il n' a pas de 5

'''
annee_sortie = [int(n) for n in annee_sortie]

metascore = list(map(int, metascore))

'''