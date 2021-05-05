#!/usr/bin/env python
# coding: utf-8

# In[1]:


from GamerLib import Gamer

def login () :

    custst = input ("Please enter your customer ID:")
    gamer = Gamer (custst)
    
    if gamer.clientid != 0 :
        firstname = input ("Please enter your first name:")
        if (firstname.upper() != gamer.firstname.upper()) :
            print ("First name does not match our records")
            gamer.clientid = 0
        else :
            lastname = input ("Please enter your last name:")
            if (lastname.upper() != gamer.lastname.upper()) :
                print ("Last name does not match our records")
                gamer.clientid = 0
        
    return gamer

def showhelp() :
    print ('\n')
    print ('List - List all of your accounts')
    print ('Bal  - Get current balances for all your accounts')
    print ('Txn  - List all transactions as of input date for a given account')
    print ('Exit - To exit the application')
    print ('\n')
    
def listaccounts (gamer) :
    accounts = gamer.accounts
    n = 0
    for account in accounts ['accounts'] :
        if account['official_name'] != None :
            n += 1
            print (f"{n}  {account['official_name'].ljust(60)}  {account['subtype']}")
            
    print ("\n")
        
def getbalances (gamer) :
    accounts = gamer.accounts
    n = 0
    for account in accounts ['accounts'] :
        if account['official_name'] != None :
            n += 1
            s = account['balances']['current']
            bal = float(s)
            s = "${:,.2f}".format(bal)
            print (f"{n}  {account['official_name'].ljust(60)}  {s.rjust(15)}")
            
    print ("\n")
    
    
def gettxns (gamer) :
    accounts = gamer.accounts
    n = 0    
    acctnum = input (f"Which account would you like transactions for (1-{gamer.acctCnt})? ")
    
    if int(acctnum) < 1 or int(acctnum) > gamer.acctCnt :
        print ("Valid account not specified")
        return
    
    acctsonly = accounts ['accounts']
    account = acctsonly [int(acctnum)-1]
    acctid = account ['account_id']
    acctname = account ['official_name']
    
    
    startdate = input ("From date: ")
    enddate = input ("To date: ")
    
    #startdate = '2020-01-01'
    #enddate = '2021-05-01'

    print ("\n")
    print (acctname)
    
    transactions = gamer.get_bank_transactions (startdate, enddate)

    for txn in transactions ['transactions'] :        
        if txn['account_id'] == acctid :
            s = txn['amount']
            amount = float(s)
            s = "${:,.2f}".format(amount)
            desc = txn['merchant_name']
            if desc == None :
                desc = txn['name']
                #print (txn)
            desc = desc.ljust(30)
            print (f"{txn['date']} {desc} {s.rjust(15)}")

    print ("\n")
    
    # main program
print ("Welcome to my Final Project\n")

x = 0
while x == 0 :
    gamer1 = login()
    x = gamer1.clientid
    if x == 0 :
        s = input ("Not Found.  Would you like to try again? (Y/N) ")
        if s.upper() != "Y" :
            x = -1
        else :
            print ("\n")
    
if x > 0 :
    print ("You are logged in!\n")
    keeprunning = True
    while keeprunning == True :
        dothis = input ('What would you like to do? (type help if clueless) ')
        if dothis.upper() == 'HELP' :
            showhelp()
        elif dothis.upper() == 'EXIT' :
            keeprunning = False
        elif dothis.upper() == 'LIST' :
            listaccounts(gamer1)
        elif dothis.upper() == 'BAL' :
            getbalances(gamer1)
        elif dothis.upper() == 'TXN' :
            gettxns(gamer1)            
            


# In[ ]:




