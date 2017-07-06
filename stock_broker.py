import quandl
import datetime

path = "/Users/Akhil/anaconda/lib/python3.6/site-packages/quandl "
auth_tok = "JMkgHX4qe3vKdhz8s46k"

print()
print()
name= input("Enter the name of the company: ")
number_of_shares=input("Enter the number of shares:")
company = "WIKI/"+name

curr_date= datetime.date.today().strftime("20%y-%m-%d")
print (curr_date)

BUYDATE= input("Enter the BUY date in YYYY-MM-DD format ")
year, month, day = (int(x) for x in BUYDATE.split('-'))    
day = datetime.date(year, month, day).weekday()

while(day==5 or day==6 or day==8):
	print("The date you have entered is either a Saturday or a Sunday. Please enter a different date")
	BUYDATE= input("Enter the BUY date in YYYY-MM-DD format ")
	year, month, day = (int(x) for x in BUYDATE.split('-'))    
	day = datetime.date(year, month, day).weekday()



sale=input("Would you like to know the net difference if you sell at current price? (y/n)")
sale=sale.lower()

if sale=="n":
	SELLDATE= input("Enter the SELL date in YYYY-MM-DD format ")
	year, month, day = (int(x) for x in SELLDATE.split('-'))    
	day_sale = datetime.date(year, month, day).weekday()

	while (day_sale==5 or day_sale==6):
		print("The date you have entered is either a saturday or a sunday. Pls enter a different date")
		SELLDATE= input("Enter the SELL date in YYYY-MM-DD format ")
		year, month, day = (int(x) for x in SELLDATE.split('-'))    
		day_sale = datetime.date(year, month, day).weekday()

elif sale=="y":
	
	SELLDATE= datetime.date.today().strftime("20%y-%m-%d")
	year, month, day = (int(x) for x in SELLDATE.split('-'))    
	day = datetime.date(year, month, day).weekday()
	

	if day==7: 
		day= int(SELLDATE[9:10])
		day = day -2
		
		if day<10:
			day="0"+str(day)
		
		SELLDATE= SELLDATE[0:8]+str(day)
	
	elif day==6:
	
		day= int(SELLDATE[9:10])
		day= day-1
		if day<10:
			day="0"+str(day)
		SELLDATE= SELLDATE[0:8]+str(day)
#price_type={'closing':".4", 'low':".3", 'high':".2", 'open':".1"}

print("buydate: ", BUYDATE, "Selldate:  ", SELLDATE)

#key= input("Enter 'closing' for closing price, 'low' for low price, 'high' for high price, 'open' for opening price: ")

#mydata = quandl.get(company+price_type[key], start_date="2017-06-15", end_date="2017-06-27")
mydata1 = quandl.get(company+'.4', start_date=BUYDATE, end_date=BUYDATE)
mydata2 = quandl.get(company+'.4', start_date=SELLDATE, end_date=SELLDATE)
#mydata1 = mydata1[['Close']]
#mydata2= mydata2[['Close']]
#mydata= [mydata1, mydata2]
#difference =mydata[0]['Close']-mydata1[1]['Close']
#mydata = quandl.get("WIKI/NVDA"+".4", start_date="2017-06-01",end_date="2017-06-27", transformation="diff")
print("Type of raw data: ", type(mydata1))
print ("TEST: ",mydata1.Close)
mydata1_str=mydata1.to_string()
mydata2_str=mydata2.to_string()
#print (mydata1, mydata2)

data1_val= mydata1_str[48:56]
data2_val= mydata2_str[48:56]
print("Bought at:  ",data1_val)
print("Sold at:  ",data2_val)

if data2_val=="   ":
	print("IDGAF")

data1_val=float(data1_val)
data2_val=float(data2_val)


difference= float(number_of_shares)*(data2_val-data1_val)
#difference= mydata1.Close- mydata2.Close
percent_change= (data2_val-data1_val)*100/data1_val
print("Buy: $",data1_val, "Sell: $",data2_val, "Number of shares: ", number_of_shares)
print("Net: $", difference, "Net percent change: ", percent_change,"%")
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



		


		
