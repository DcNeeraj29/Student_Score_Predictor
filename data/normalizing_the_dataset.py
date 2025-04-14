import pandas as pd

df = pd.read_csv("student_dataset_100.csv")

normalized = (df['FinalScore']-df['FinalScore'].min()) / (df['FinalScore'].max()-df['FinalScore'].min())

df['FinalScore'] = (normalized*(98-28))+28
df['FinalScore'] = df['FinalScore'].round(2)

df.to_csv('student_dataset_1002.csv')
