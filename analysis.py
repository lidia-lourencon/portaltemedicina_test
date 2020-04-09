import pandas as pd
import plotly.graph_objects as go
import operator

columns = [
    "age",
    "sex",
    "cp",
    "trestbps",
    "chol",
    "fbs",
    "restecg",
    "thalach",
    "exang",
    "oldpeak",
    "slope",
    "ca",
    "thal",
    "nar",
    "hc",
    "sk",
    "trf",
    "Diagnosis",
]
imported_data = pd.read_csv("test_data_lidia_4.csv", delimiter=";", usecols=columns)

age_ranges = [(20, 29), (30, 39), (40, 59), (60, 110)]

fbs = [0, 0, 0, 0]
exang = [0, 0, 0, 0]
ca = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

for index, row in imported_data.iterrows():
    age = row["age"]

    if age in range(age_ranges[0][0], age_ranges[0][1]):
        fbs[0] += row["fbs"]
        exang[0] += row["exang"]
        ca[0][int(row["ca"])] += 1
    elif age in range(age_ranges[1][0], age_ranges[1][1]):
        fbs[1] += row["fbs"]
        exang[1] += row["exang"]
        ca[1][int(row["ca"])] += 1
    elif age in range(age_ranges[2][0], age_ranges[2][1]):
        fbs[2] += row["fbs"]
        exang[2] += row["exang"]
        ca[2][int(row["ca"])] += 1
    elif age in range(age_ranges[3][0], age_ranges[3][1]):
        fbs[3] += row["fbs"]
        exang[3] += row["exang"]
        ca[3][int(row["ca"])] += 1


graph_colums = ["20 - 29", "30 - 39", "49 - 59", "60 +"]

fig = go.Figure(
    data=[
        go.Bar(name="Fasting blood sugar", x=graph_colums, y=fbs),
        go.Bar(name="Exercice induced agina", x=graph_colums, y=exang),
    ]
)
fig.update_layout(barmode="group")
fig.layout.title.text = "Fasting blood sugar and Exercice induced agina by age range"
fig.write_html("fbs_exang.html", auto_open=True)


fig2 = go.Figure()
fig2.add_trace(go.Bar(name="Level 00", x=graph_colums, y=[item[0] for item in ca]))
fig2.add_trace(go.Bar(name="Level 01", x=graph_colums, y=[item[1] for item in ca]))
fig2.add_trace(go.Bar(name="Level 02", x=graph_colums, y=[item[2] for item in ca]))
fig2.add_trace(go.Bar(name="Level 03", x=graph_colums, y=[item[3] for item in ca]))
fig2.add_trace(go.Bar(name="Level 04", x=graph_colums, y=[item[4] for item in ca]))

fig2.update_layout(barmode="group", title_text="Number of major vessels by age range")
fig2.write_html("ca.html", auto_open=True)
