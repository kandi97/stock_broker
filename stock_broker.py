import quandl
from datetime import date, timedelta
path = "/Users/Akhil/anaconda/lib/python3.6/site-packages/quandl "
auth_tok = "JMkgHX4qe3vKdhz8s46k"


print("Welcome to Stock Broker")
name= input("Enter the name of the company whose stocks you would like to buy: ")
number_of_shares=input("Enter the number of shares:")
company = "WIKI/"+name
BUYDATE= input("Enter the BUY date in YYYY-MM-DD format ")
SELLDATE= input("Enter the SELL date in YYYY-MM-DD format ")
price_type={'closing':".4", 'low':".3", 'high':".2", 'open':".1"}

key= input("Enter 'closing' for closing price, 'low' for low price, 'high' for high price, 'open' for opening price: ")

#mydata = quandl.get(company+price_type[key], start_date="2017-06-15", end_date="2017-06-27")
mydata1 = quandl.get(company+price_type[key], start_date=BUYDATE, end_date=BUYDATE)
mydata2 = quandl.get(company+price_type[key], start_date=SELLDATE, end_date=SELLDATE)
#mydata1 = mydata1[['Close']]
#mydata2= mydata2[['Close']]
#mydata= [mydata1, mydata2]
#difference =mydata[0]['Close']-mydata1[1]['Close']



#mydata = quandl.get("WIKI/NVDA"+".4", start_date="2017-06-01",end_date="2017-06-27", transformation="diff")
mydata1=mydata1.to_string()
mydata2=mydata2.to_string()


data1_val= mydata1[48:56]
data2_val= mydata2[48:56]

data1_val=float(data1_val)
data2_val=float(data2_val)

difference= float(number_of_shares)*(data2_val-data1_val)
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



		
