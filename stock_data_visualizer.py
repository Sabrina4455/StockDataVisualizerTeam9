import requests
import json
import midtermstruct4320
import pygal
from datetime import datetime, timedelta
def main():
    x1()
#calls all the main functions
def x1():
    symbol,chart,function,bd,ed,apikey=questions()
    data=apiRequest(function,symbol,apikey)
    data1=(data['Time Series (Daily)'])
    test=json.dumps(data1)
    test2=json.loads(test)
    data6=structmaker(test2)
    graph1=makeGraph(chart,data6,bd,ed,symbol)
    
#makes graph option two supposed to be bar graph
#this function doesn't work right yet
#the line line_chart.x_labels.... is wrong needs to be changed to get correct date ranges
def makeGraph(choice,data6,lowDate,highDate,symbol):
    open2=[]
    high1=[]
    low1=[]
    close1=[]
    volume1=[]
    date1=[]
    if choice == "1":
        for item in data6:
            temp = item.getOpen()
            open2.append(temp)
            temp = item.getHigh()
            high1.append(temp)
            temp = item.getLow()
            low1.append(temp)
            temp=item.getClose()
            close1.append(temp)
            temp=item.getVolume()
            volume1.append(temp)
            temp=item.getDate()
            date1.append(temp)
        line_chart = pygal.Line()
        line_chart.title = ''+symbol+' stock data from'+lowDate+' to ' +highDate+''
        #The line below is incorrect
        line_chart.x_labels =map(lambda d: d.strftime('%Y-%m-%d'), [ datetime(2013,1,2)])                                                                       
        line_chart.add('Open',open2)
        line_chart.add('High',high1)
        line_chart.add('Low',low1)
        line_chart.add('Close',close1)
        line_chart.add('Volume',volume1)
        line_chart.render()
    
    
#Creates a structure of all the data points needed and saves it in list1  
def structmaker(data):
    list1=[]
    for i in data:
        open1=data[i]['1. open']
        high=data[i]['2. high']
        low=data[i]['3. low']
        close=data[i]['4. close']
        volume=data[i]['5. volume']
        date=i
        temp = midtermstruct4320.midtermstruct(open1,high,low,close,volume,date)
        list1.append(temp)
    return list1
"""
#unused function to convert json string to dictionary
def jsonDictionaryConvert(data):
    data_dict = json.load(data)
    print(data_dict)
"""  

#user chooses time series returns 1,2,3, or 4 checks if user chose 1,2,3, or 4
def timeSeriesSelect():
    check=False
    while check==False:
        answer = input("Enter the time series function you want the api to use: \n------------\n1.Intraday\n2.Daily\n3.Weekly\n4.Monthly\n------------\n:")
        if answer == "1" or answer == "2" or answer == "3" or answer == "4":
            check=True
        else:
            check=False
    return answer

#user chooses chart type returns 1 or 2 checks if user chose 1 or 2
def chartTypeSelect():
    check=False
    while check==False:
        answer = input("Enter the time series function you want the api to use: \n------------\n1.line\n2.bar\n------------\n:")
        if answer == "1" or answer == "2":
            check=True
        else:
            check=False
    return answer

#user chooses dates, checks to make sure second is not before first, returns dates still in string
def datesSelect():
    check=False
    while check==False:
        answer1 = input("Enter the beginning date (Format:YYYY-MM-DD): ")
        answer2 = input("Enter the end date (Format:YYYY-MM-DD): ")
        x = int(answer1[0:4])
        x1 = int(answer1[6:7])
        x2 = int(answer1[8:10])
        x3 = int(answer2[0:4])
        x4 = int(answer2[6:7])
        x5 = int(answer2[8:10])
        years = x3-x
        months = x4-x1
        days = x5-x2
        #print(days,months,years)
        if years >= 0 and months >= 0 and days >= 0:
            check=True
        else:
            check=False
    return answer1,answer2

#general question function returns user answers calls datesSelect, chartTypeSelect, and timeSeriesSelect
def questions():
    a1 = input("Enter the stock symbol for the company: ")
    a2 = chartTypeSelect()
    a3 = timeSeriesSelect()
    a4,a5=datesSelect()
    a6 = "R6OMMN6KY7H6OUY7"
    return a1,a2,a3,a4,a5,a6

#function that makes api request based on choice. Returns a nested dict of data in json format
def apiRequest(function,symbol,apikey):
    if function == "1":
        url= 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol='+symbol+'&interval=30mins&apikey=('+apikey+')'
        r = requests.get(url)
        data = r.json()
        return data
    if function == "2":
        url= 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol='+symbol+'&apikey=('+apikey+')'
        r = requests.get(url)
        data = r.json()
        return data
    if function == "3":
        url = 'https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY&symbol='+symbol+'&apikey=('+apikey+')'
        r = requests.get(url)
        data = r.json()
        return data
    if function == "4":
        url = 'https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol='+symbol+'&apikey=('+apikey+')'
        r = requests.get(url)
        data = r.json()
        return data
    
main()

