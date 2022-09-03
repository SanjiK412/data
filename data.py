import pandas as pd 
import plotly.express as px
import csv
data=pd.read_csv("data.csv")
mean=data.groupby(["student_id", "level"])["attempt"].mean()
fig=px.scatter(mean, x="student_id", y="level", size="attempt")
fig.show()



