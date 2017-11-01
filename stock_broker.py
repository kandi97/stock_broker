import quandl
from datetime import date, timedelta

path = "/Users/Akhil/anaconda/lib/python3.6/site-packages/quandl "
auth_tok = "JMkgHX4qe3vKdhz8s46k"

print()
print("Welcome to Stock Broker")
print()
name= input("Enter the name of the company whose stocks you would like to buy: ")
number_of_shares=input("Enter the number of shares:")
company = "WIKI/"+name

curr_date= date.today()
print (curr_date)

BUYDATE= input("Enter the BUY date in YYYY-MM-DD format ")
year, month, day = (int(x) for x in BUYDATE.split('-'))    
day = date(year, month, day).weekday()

while(day==5 or day==6 or day==8):
	print("The date you have entered is either a Saturday or a Sunday. Please enter a different date")
	BUYDATE= input("Enter the BUY date in YYYY-MM-DD format ")
	year, month, day = (int(x) for x in BUYDATE.split('-'))    
	day = date(year, month, day).weekday()



sale=input("Would you like to know the net difference if you sell at current price? (y/n)")
sale=sale.lower()

if sale=="n":
	SELLDATE= input("Enter the SELL date in YYYY-MM-DD format ")
	year, month, day = (int(x) for x in SELLDATE.split('-'))    
	day_sale = date(year, month, day).weekday()

	while (day_sale==5 or day_sale==6):
		print("The date you have entered is either a saturday or a sunday. Pls enter a different date")
		SELLDATE= input("Enter the SELL date in YYYY-MM-DD format ")
		year, month, day = (int(x) for x in SELLDATE.split('-'))    
		day_sale = date(year, month, day).weekday()

elif sale=="y":
	
	SELLDATE= date.today().strftime("20%y-%m-%d")
	year, month, day = (int(x) for x in SELLDATE.split('-'))    
	day_of_week = date(year, month, day).weekday()
	

	if day_of_week==7:
		
		SELLDATE= date.today()-timedelta(2)
		SELLDATE= SELLDATE.strftime("20%y-%m-%d")
		
	
	elif day_of_week==6:
		SELLDATE= date.today()-timedelta(1)
		SELLDATE= SELLDATE.strftime("20%y-%m-%d")
		
		
#price_type={'closing':".4", 'low':".3", 'high':".2", 'open':".1"}


#key= input("Enter 'closing' for closing price, 'low' for low price, 'high' for high price, 'open' for opening price: ")

#mydata = quandl.get(company+price_type[key], start_date="2017-06-15", end_date="2017-06-27")
mydata1 = quandl.get(company+'.4', start_date=BUYDATE, end_date=BUYDATE)
mydata2 = quandl.get(company+'.4', start_date=SELLDATE, end_date=SELLDATE)

i=0
while(mydata2.Close.dtype== object):
	#year, month, day = (int(x) for x in SELLDATE.split(','))    
	i+=1
	SELLDATE= curr_date-timedelta(i)
	SELLDATE= SELLDATE.strftime("20%y-%m-%d")
	mydata2 = quandl.get(company+'.4', start_date=SELLDATE, end_date=SELLDATE)

print("Bought on: ", BUYDATE, "Sold on:  ", SELLDATE)

#mydata1 = mydata1[['Close']]
#mydata2= mydata2[['Close']]
#mydata= [mydata1, mydata2]
#difference =mydata[0]['Close']-mydata1[1]['Close']
#mydata = quandl.get("WIKI/NVDA"+".4", start_date="2017-06-01",end_date="2017-06-27", transformation="diff")
#print("Type of raw data: ", type(mydata1))
#print ("TEST: ",mydata1.Close)

#print (mydata1, mydata2)

#mydata1_str=mydata1.to_string()
#mydata2_str=mydata2.to_string()
#data1_val= mydata1_str[48:56]
#data2_val= mydata2_str[48:56]
data1_val= float(mydata1.Close)
data2_val= float(mydata2.Close)
print("Bought at:  $",data1_val)
print("Sold at:  $",data2_val)



data1_val=float(data1_val)
data2_val=float(data2_val)


difference= float(number_of_shares)*(data2_val-data1_val)
#difference= mydata1.Close- mydata2.Close
percent_change= (data2_val-data1_val)*100/data1_val
print("Number of shares: ", number_of_shares)
print("Net: $", difference, " Net percent change: ", percent_change,"%")
print()
print()

#t=0
#for i in mydata1:
#	t+=1
#	if i =="1" or i=="4" or i=="3" or i=="." or i=="6" or i=="4":
#		print ("index: ", t, "number: ", i)
#		
#print (difference)

#net_diff= mydata1['Adj. Close']-mydata2['Adj. Close']
#rint("Net difference is: ",net_diff)



		


		
