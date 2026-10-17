import mysql.connector
import pandas as pd
import numpy as np
import random
from pandas.core.interchange import dataframe
from sqlalchemy import create_engine

np.random.seed(23)
connection = mysql.connector.connect(
    host='127.0.0.1',
    user='pricing_app',
    password='your_secure_password',
    database='economic_db'
)
cursor = connection.cursor()
cursor.execute("SELECT VERSION();")
print(cursor.fetchone())

engine = create_engine(

"mysql+mysqlconnector://pricing_app:your_secure_password@127.0.0.1/economic_db"
)

#create appropriate columns
print("Number of years:")
year = int(input())
print("Number of products:")
product = int(input())

data = {
    #LHS is the columns
    "Product": [],
    "Base Quantity": [],
    #price(1) is the base price
    #there are i columns following these 3
}

for k in range(1, year + 1):
    #add new columns
    data[f"Price {k}"]= []

#create data for rows
for k in range(1, product+ 1):
    data["Product"].append(k)

# quantity rand(100,10000)
for j in range(1,product+1):
    x = random.randint(100,10000)
    data["Base Quantity"].append(x)

for i in range(1,product+1):
    decision = random.randint(1, 10)
    for j in range(1,year+1):
        if decision < 5:
            price = round(random.uniform(1,3),2)
            data[f"Price {j}"].append(price)
        elif decision == 5 or decision < 8:
            price = round(random.uniform(5, 7),2)
            data[f"Price {j}"].append(price)
        else:
            price = round(random.uniform(25000, 32000),2)
            data[f"Price {j}"].append(price)


    #create rows for the base quantity column (int)
print(data)

dataframe = pd.DataFrame(data)

print(dataframe)

#bring to sql

dataframe.to_sql(

    name = "products",
    con= engine,
    if_exists='append',
    index=False,
)

#base price is the first price (3rd column)
#sum all price columns * base quantity

#CPI for every year is a new column
for i in range(1,year+1):








