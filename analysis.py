# importing libraries

import pandas as pd
import matplotlib as plt
import seaborn as sns

# DATA LOADING

# defining the source path to the data
dir = "https://raw.githubusercontent.com/andressaapio/pythontutorials/main/data/olist/"

# dataset com informações sobre PEDIDOS: olist_orders_dataset.csv

orders = pd.read_csv(dir + 'olist_orders_dataset.csv')

print(orders.head())