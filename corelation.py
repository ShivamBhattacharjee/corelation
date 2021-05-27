import plotly.express as px 
import csv
import numpy as np 

def getDataSource(dataPath,xValues,yValues):
    xValue=[]
    yValue=[]
    with open (dataPath) as file:
        csvReader=csv.DictReader(file)
        for row in csvReader:
            xValue.append(float(row[xValues]))
            yValue.append(float(row[yValues]))

    return{"x":xValue,"y":yValue}

def findCorelation(dataSource):
    corelation=np.corrcoef(dataSource["x"],dataSource["y"])
    print("corelation=\t",corelation[0,1])

def setup():
    dataPath="student.csv"
    xValue="Marks"
    yValue="Days Present"
    dataSource=getDataSource(dataPath,xValue,yValue)
    findCorelation(dataSource)

setup()

def setup():
    dataPath="coffee.csv"
    xValue="Coffee"
    yValue="sleep"
    dataSource=getDataSource(dataPath,xValue,yValue)
    findCorelation(dataSource)

setup()

with open("student.csv") as f:
    df=csv.DictReader(f)
    fig=px.scatter(df,x="Marks",y="Days Present")
    fig.show()

with open("coffee.csv") as h:
    df2=csv.DictReader(h)
    fig1=px.scatter(df2,x="Coffee",y="sleep")
    fig1.show()



