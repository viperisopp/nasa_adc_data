import pandas as pd

df = pd.read_excel("adc-2025-data-bonus.xlsx")

df.to_csv("nasa_adc_2025_bonus.csv",index=False)