#%%
import pandas as pd
import matplotlib.pyplot as plt

#%%
df = pd.read_csv('https://raw.githubusercontent.com/fferegrino/yu-gi-oh/refs/heads/main/data/cards.csv')

#%%
df['type'].unique()

#%%
df_monsters = df[df['type'].str.contains(r'\bMonster\b', na=False)]
df_monsters.head()
