#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
import re
import sys
from typing import List
import psycopg2
from plaid import Client as PlaidClient
from plaid.errors import APIError, ItemError

#all of these variables need to go into a (secure) non-github file
testenvironment = 'sandbox'
plaidclientid = '60874cba33acxsdf10bedbce'
secretcode = '17555accfsdfakdk4b2f0437be674e'
db = "dbname=FinalProject user=postgres password=admin host=127.0.0.1 port=5432"

class Gamer:
    def __init__(self, clientid):
        
        conn = psycopg2.connect(db)
        cur = conn.cursor()
        cur.execute (f'SELECT * FROM customer WHERE id = {clientid}')
        row = cur.fetchone()
        
        if row == None :
            self.clientid = 0
            return;
        
        self.clientid = int(clientid)
        self.firstname = row[1]
        self.lastname = row[2]
        self.item = row[3]
        self.accessid = row[4]
        
        #establish the connection to Plaid
        self.plaid_client = PlaidClient(client_id=plaidclientid,
                           secret=secretcode,
                           environment = testenvironment)

        self.accounts = self.plaid_client.Auth.get (self.accessid)
        self.acctCnt = 0
        for account in self.accounts ['accounts'] :
            if account['official_name'] != None :
                self.acctCnt += 1
        
        #need to add phone, email, address, verification, etc.
    
    # need to update database with accounts
    def getAccounts (self) -> List[dict]:
        return self.plaid_client.Auth.get (self.accessid)

    #need to update database with txns
    def get_bank_transactions(self, start_date: str, end_date: str) -> List[dict]:
        return self.plaid_client.Transactions.get(self.accessid, start_date, end_date, count = 500)
    

