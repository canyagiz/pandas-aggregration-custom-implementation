import numpy as np
import pandas as pd
import seaborn as sns

# Load the dataset
df = sns.load_dataset("car_crashes")


attributes = ["mean", "min", "max", "var"]

num_columns = [column for column in df.columns if df[column].dtype == np.number]

df_num = df[num_columns]

# Dictionary comprehension
stats = {
    column: {
        "mean": df_num[column].sum() / len(df_num[column]),
        "min": df_num[column].min(),
        "max": df_num[column].max(),
        "var": sum((x - (df_num[column].sum() / len(df_num[column])))**2 for x in df_num[column]) / (len(df_num[column]) - 1)
    }
    for column in df_num.columns
}

df2 = pd.DataFrame(stats)
