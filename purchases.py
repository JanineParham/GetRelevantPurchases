import pandas as pd
from datetime import datetime

##Import CSV File##
fields = ['Date', 'Transaction', 'Description']
df = pd.read_excel(r'/Users/janineparham/Desktop/purchases_excel/2022Transactions.xls', usecols=fields, index_col=None)
totalSpent = 0
for i in range(len(df.index)):
    #Check if the purchase was during a weekday
    myDate = df.loc[i]['Date']
    day_num = myDate.weekday()
    if day_num < 5:
        #Check if it was a Door dash purchase
        description = df.loc[i]['Description']
        rel_string = 'DOORDASH*'
        if rel_string in description:
            #Check to see if it was a withdrawal
            transaction = df.loc[i]['Transaction']
            if transaction < 0:
                #Add the amount to the total spent
                totalSpent = totalSpent+transaction
print(totalSpent)
    