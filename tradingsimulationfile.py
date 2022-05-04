# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
url = "https://raw.githubusercontent.com/lukasgebhardt/tradingsimulation/main/HistoricalPrices%20Dow%20Jones.csv"
df = pd.read_csv(url)
print(df.head(5))