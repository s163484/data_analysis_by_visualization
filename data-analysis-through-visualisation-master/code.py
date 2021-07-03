import pandas as pd 
import csv 
import plotly.express as px

df = pd.read_csv("data.csv")
mean = df.groupby(["student_id", "level"], as_index=False)["attempt"].mean()
fig = px.scatter(mean, X="student_id", Y= "level", size = "attempt", color = "attempt")
fig.show()