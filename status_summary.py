# Import pandas package
import pandas as pd

df = pd.read_csv('dhabstracts_status.csv')

value_counts = df['status_code'].value_counts()

value_counts_df = value_counts.to_frame()

# Export to CSV
value_counts_df.to_csv('value_counts.csv')