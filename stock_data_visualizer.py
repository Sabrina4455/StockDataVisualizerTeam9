import requests
import json
import midtermstruct4320
import pygal
import datetime
def main():
    x1()
#calls all the main functions
def x1():
    symbol,chart,function,bd,ed,apikey=questions()
    data=apiRequest(function,symbol,apikey)
    timeSeries=timeSeriesCheck(function)
    data1=(data[timeSeries])
    test=json.dumps(data1)
    test2=json.loads(test)
    data7=refineData(test2,bd,ed,function)
    graph1=makeGraph(chart,data7,bd,ed,symbol,function)
    
    
#makes graph option two supposed to be bar graph
#this function doesn't work right yet
#the line line_chart.x_labels.... is wrong needs to be changed to get correct date ranges
def refineData(data,bd,ed,function):
    list1=[]
    format1=""
    if function == "1":
        format1= '%Y-%m-%d %H:%M:%S'
        bd=bd+' 00:00:00'
        ed=ed+' 00:00:00'
    else:
        format1 = '%Y-%m-%d'
    for item in data:
        x = datetime.datetime.strptime(item, format1)
        x1 = datetime.datetime.strptime(bd, format1)
        x2 = datetime.datetime.strptime(ed, format1)
        #print(item)
        if (x < x2 or x == x2) and( x > x1 or x == x1):
            open1=float(data[item]['1. open'])
            high=float(data[item]['2. high'])
            low=float(data[item]['3. low'])
            close=float(data[item]['4. close'])
            volume=float(data[item]['5. volume'])
            date=item
            #print(date)
            temp = midtermstruct4320.midtermstruct(open1,high,low,close,volume,date)
            list1.append(temp)
        else:
            continue
    return list1
        
def makeGraph(choice,data6,lowDate,highDate,symbol,function):
    open2=[]
    high1=[]
    low1=[]
    close1=[]
    volume1=[]
    date1=[]
    if choice == "1":
        chart=pygal.Line(x_label_rotation=45)
    if choice == "2":
        chart=pygal.Bar(x_label_rotation=45)
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
    chart.title = ''+symbol+' stock data from '+lowDate+' to ' +highDate+''
    temp10=date1
    temp10.reverse()
    if function == "1":
        lowDate = lowDate + ' 00:00:00'
    if choice != "1":
        lowDate = lowDate
    temp10.insert(0,lowDate)
    chart.x_labels = temp10                                                                      
    chart.add('Open',open2)
    chart.add('High',high1)
    chart.add('Low',low1)
    chart.add('Close',close1)
    chart.render_in_browser()
        
    
    
#Creates a structure of all the data points needed and saves it in list1
"""
def structmaker(data):
    list1=[]
    for i in data:
        open1=float(data[i]['1. open'])
        high=float(data[i]['2. high'])
        low=float(data[i]['3. low'])
        close=float(data[i]['4. close'])
        volume=float(data[i]['5. volume'])
        date=i
        temp = midtermstruct4320.midtermstruct(open1,high,low,close,volume,date)
        list1.append(temp)
    return list1

#unused function to convert json string to dictionary
def jsonDictionaryConvert(data):
    data_dict = json.load(data)
    print(data_dict)
"""  
def timeSeriesCheck(function):
    timeSeries=''
    if function == "1":
        timeSeries = 'Time Series (60min)'
    if function == "2":
        timeSeries = 'Time Series (Daily)'
    if function == "3":
        timeSeries = 'Weekly Time Series'
    if function == "4":
        timeSeries = 'Monthly Time Series'
    return timeSeries

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
        answer = input("Enter the chart type you want the api to use: \n------------\n1.line\n2.bar\n------------\n:")
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
        x1 = int(answer1[5:7])
        x2 = int(answer1[8:10])
        x3 = int(answer2[0:4])
        x4 = int(answer2[5:7])
        x5 = int(answer2[8:10])
        #print(x,x1,x2,x3,x4,x5)
        years = x3-x
        months = x4-x1
        days = x5-x2
        #print(days,months,years)
        total=((years*365)+(months*30)+(days))
        if total>=0:
            check=True
        else:
            print("\nStart date must be before end date, try again: \n")
            check=False
    return answer1,answer2

#general question function returns user answers calls datesSelect, chartTypeSelect, and timeSeriesSelect
def questions():
    a1 = input("Enter the stock symbol for the company: ")
    a2 = chartTypeSelect()
    a3 = timeSeriesSelect()
    a4,a5=datesSelect()
    a6 = "HUU48H4FRECOJIM7"
    return a1,a2,a3,a4,a5,a6

#function that makes api request based on choice. Returns a nested dict of data in json format
def apiRequest(function,symbol,apikey):
    if function == "1":
        url= 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol='+symbol+'&interval=60min&outputsize=full&apikey=('+apikey+')'
        r = requests.get(url)
        data = r.json()
        return data
    if function == "2":
        url= 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol='+symbol+'&outputsize=full&apikey=('+apikey+')'
        r = requests.get(url)
        data = r.json()
        return data
    if function == "3":
        url = 'https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY&symbol='+symbol+'&outputsize=full&apikey=('+apikey+')'
        r = requests.get(url)
        data = r.json()
        return data
    if function == "4":
        url = 'https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol='+symbol+'&outputsize=full&apikey=('+apikey+')'
        r = requests.get(url)
        data = r.json()
        return data
    
    
main()

