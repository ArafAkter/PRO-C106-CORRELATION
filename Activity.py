import plotly.express as px
import csv
import numpy as np
def getData(data_path):
     iceCreamSales = []
     ColdDrinkSales = []
     with open(data_path) as csv_file:
         csvReader = csv.DictReader(csv_file)
         for row in csvReader:
             iceCreamSales.append(float(row["Marks In Percentage"]))
             ColdDrinkSales.append(float(row["Days Present"]))
     return {"x":iceCreamSales,"y":ColdDrinkSales}


def find(dataSource):
    correlation = np.corrcoef(dataSource["x"],dataSource["y"])
    print(correlation[0,1])

def setup():
    data_path = "Ice-Cream vs Cold-Drink vs Temperature - Ice Cream Sale vs Temperature data.csv"
    dataSource = getData(data_path)
    find(dataSource)

setup()