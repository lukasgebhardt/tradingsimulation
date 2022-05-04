# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
url = "https://raw.githubusercontent.com/lukasgebhardt/tradingsimulation/main/HistoricalPrices%20Dow%20Jones.csv"
df = pd.read_csv(url)
i=0
while i < 5:
    i +=1
    print(df.iloc[i][0].split(";")[1])
    
    