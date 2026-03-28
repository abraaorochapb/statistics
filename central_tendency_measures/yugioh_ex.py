#%%
import pandas as pd
import matplotlib.pyplot as plt

#%%
df = pd.read_csv('https://raw.githubusercontent.com/fferegrino/yu-gi-oh/refs/heads/main/data/cards.csv')

#%%
# We use the unique() method to get the unique values in the 'type' column.
df['type'].unique()

    #%%
# We filter the DataFrame to include only rows where the 'type' column contains the word 'Monster'.
df_monsters = df[df['type'].str.contains(r'\bMonster\b', na=False)]
df_monsters.head()

# %%
# Here we use the count() method to get the total number of monster cards in the dataset.
df_monsters['type'].count()
# %%
# Here we use the value_counts() method to get the count of each type of monster card in the dataset.
df_monsters['type'].value_counts()

# %%
# Here we use the normalize parameter to get the relative frequencies of each type of monster card
# then we multiply by 100 to convert it to percentages.
df_monsters['type'].value_counts(normalize=True) * 100

# %%
# Here we use the plot() method to create a bar chart of the counts of each type of monster card.
(df_monsters['type'].value_counts(normalize=True) * 100).plot(kind='barh')
plt.xlabel('Percentage of Monster Cards')
plt.xlim(0, 60)
plt.ylabel('Monster Card Type')
plt.title('Distribution of Monster Card Types')
plt.tight_layout()
plt.show()

# %%
# Here we use the groupby() method to group the DataFrame by the 'type' column
# then we use the quantile() method to calculate the median of the 'atk' column for each group.
df_monsters.groupby('type')['atk'].quantile(0.5)
# %%
df_monsters.groupby('type')['atk'].quantile(0.5).plot(kind='barh')
plt.xlabel('Median Attack Points')
plt.ylabel('Monster Card Type')
plt.title('Median Attack Points by Monster Card Type')
plt.tight_layout()
plt.show()