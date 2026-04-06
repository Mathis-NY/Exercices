import pandas as pd

df = pd.read_csv('population9.csv')

df21 = df[df['year'] == 2021]
df22 = df[df['year'] == 2022]
#here state
pop21 = df21.groupby('state')['population'].sum()
mean21 = df21.groupby('state')['population'].mean()

pop22 = df22.groupby('state')['population'].sum()
mean22 = df22.groupby('state')['population'].mean()


result = pd.DataFrame({
    '21 state pop': pop21,
    '21 county mean': mean21,
    '22 state pop': pop22,
    '22 county mean': mean22
})

# %
result['21 to 22 % pop change'] = (
    (result['22 state pop'] - result['21 state pop']) /
    result['21 state pop']
) * 100
result = result.round(2)


print(result.to_string())

# les augmentations et les diminutions
max_increase_state = result['21 to 22 % pop change'].idxmax()
max_increase_value = result['21 to 22 % pop change'].max()

max_decline_state = result['21 to 22 % pop change'].idxmin()
max_decline_value = result['21 to 22 % pop change'].min()

print(f"\n{max_decline_state} had the greatest population decline between 2021 and 2022 with {round(max_decline_value, 2)} percent.")
print(f"{max_increase_state} had the greatest population increase between 2021 and 2022 with {round(max_increase_value, 2)} percent.")
