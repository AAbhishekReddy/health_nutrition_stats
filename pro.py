import pandas as pd
import numpy as np

# Reading the excel files sheet by sheet

data = pd.read_excel('C:/Users/ghost/Desktop/BDANN/Project/x-files/HNP_statsEXCEL.xlsx', sheet_name = 0)
country = pd.read_excel('C:/Users/ghost/Desktop/BDANN/Project/x-files/HNP_statsEXCEL.xlsx', sheet_name = 1)
series = pd.read_excel('C:/Users/ghost/Desktop/BDANN/Project/x-files/HNP_statsEXCEL.xlsx', sheet_name = 2)
c_series = pd.read_excel('C:/Users/ghost/Desktop/BDANN/Project/x-files/HNP_statsEXCEL.xlsx', sheet_name = 3)
series_t = pd.read_excel('C:/Users/ghost/Desktop/BDANN/Project/x-files/HNP_statsEXCEL.xlsx', sheet_name = 5)
foot_note = pd.read_excel('C:/Users/ghost/Desktop/BDANN/Project/x-files/HNP_statsEXCEL.xlsx', sheet_name = 'FootNote')

# Viewing the tables

data.head()
country.head()
series.head()
c_series.head()
series_t.head()
foot_note.head()