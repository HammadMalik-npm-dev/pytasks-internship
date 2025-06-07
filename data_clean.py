import pandas as pd

# Sample data
data = {
    'Name': ['Ali', 'Hammad', None, 'Zara'],
    'Age': [22, 24, None, 21]
}

df = pd.DataFrame(data)

# Clean data
df_clean = df.dropna()

print("Cleaned Data:")
print(df_clean)
