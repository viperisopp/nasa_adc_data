import pandas as pd

df = pd.read_excel("adc-2025-data.xlsx")

df.to_csv("nasa_adc_2025.csv",index=False)