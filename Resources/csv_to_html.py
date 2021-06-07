import pandas as pd

city_data = pd.read_csv("cities.csv")

city_data.to_html("output.html", index=False)
