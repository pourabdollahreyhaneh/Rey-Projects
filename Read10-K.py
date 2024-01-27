#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install xlrd


# In[2]:


import numpy as np
import pandas as pd
import xlrd
#Give the location of the file
#Consolidated Statements of Oper index1 & Consolidated Balance Sheets index3 & Consolidated Statements of Cash index5
loc = (r"C:\Users\reyha\Desktop\American Airlines Group Inc_05-07-2021.xlsx")
#To open workbook & For row-1 , and column-1 as consider indexes
wb = xlrd.open_workbook (loc)


# In[3]:


#Liquidity Ratios:

#Current ratio= current assets - current liabilities
sheet = wb.sheet_by_index(3)
current_assets=sheet.cell_value(8,1)
current_liabilities=sheet.cell_value(30,1)
current_ratio=current_assets/current_liabilities
print("Current Ratio 2020: {:,.2f}".format(current_ratio))


# In[4]:


sheet = wb.sheet_by_index(3)
current_assets=sheet.cell_value(8,2)
current_liabilities=sheet.cell_value(30,2)
current_ratio=current_assets/current_liabilities
print("Current Ratio 2019: {:,.2f}".format(current_ratio))


# In[5]:


#quick ratio= cash+ account receivable +short term investment   / current liabilities

sheet = wb.sheet_by_index(3)
cash=sheet.cell_value(2,1)
account_receivable=sheet.cell_value(5,1)
short_term_investment= sheet.cell_value(3,1)
current_liabilities=sheet.cell_value(30,1)
quick_ratio=(cash + account_receivable + short_term_investment )/current_liabilities
print("Quick Ratio 2020: {:,.2f}".format(quick_ratio))


# In[6]:


sheet = wb.sheet_by_index(3)
cash=sheet.cell_value(2,2)
account_receivable=sheet.cell_value(5,2)
short_term_investment= sheet.cell_value(3,2)
current_liabilities=sheet.cell_value(30,2)
quick_ratio=(cash + account_receivable + short_term_investment )/current_liabilities
print("Quick Ratio 2019: {:,.2f}".format(quick_ratio))


# In[7]:


# Activity Ratios:

#Sales to Assets=Sales / Total Assets
sheet1 = wb.sheet_by_index(3)
sheet2 = wb.sheet_by_index(1)
total_assets=sheet1.cell_value(23,1)
sales=sheet2.cell_value(3,1)
Sales_to_assets=sales/total_assets
print("Sales to Assets 2020: {:,.2f}".format(Sales_to_assets))


# In[8]:


sheet1 = wb.sheet_by_index(3)
sheet2 = wb.sheet_by_index(1)
total_assets=sheet1.cell_value(23,2)
sales=sheet2.cell_value(3,2)
Sales_to_assets=sales/total_assets
print("Sales to Assets 2019: {:,.2f}".format(Sales_to_assets))


# In[9]:


#Accounts Receivable Turnover= Sales / Trade Accounts Receivable   

sheet1 = wb.sheet_by_index(3)
sheet2 = wb.sheet_by_index(1)
account_receivable=sheet.cell_value(5,1)
sales=sheet2.cell_value(3,1)
Turnover_Sales_to_Trade_Accounts_Receivable=sales/account_receivable
print("Turnover Sales to Trade Accounts Receivable 2020: {:,.2f}".format(Turnover_Sales_to_Trade_Accounts_Receivable))


# In[10]:


sheet1 = wb.sheet_by_index(3)
sheet2 = wb.sheet_by_index(1)
account_receivable=sheet.cell_value(5,2)
sales=sheet2.cell_value(3,2)
Turnover_Sales_to_Trade_Accounts_Receivable=sales/account_receivable
print("Turnover Sales to Trade Accounts Receivable 2019: {:,.2f}".format(Turnover_Sales_to_Trade_Accounts_Receivable))


# In[11]:


#Sales to Net Fixed Assets =Sales / (Total property and equipment,net=Property and Equipment - Accumulated Depreciation)

sheet2 = wb.sheet_by_index(1)
Total_property_and_equipment_net=sheet1.cell_value(15,1)
sales=sheet2.cell_value(3,1)
Sales_to_Net_Fixed_Assets =sales/Total_property_and_equipment_net
print("Sales to Net Fixed Assets  2020: {:,.2f}".format(Sales_to_Net_Fixed_Assets))


# In[12]:


sheet1 = wb.sheet_by_index(3)
sheet2 = wb.sheet_by_index(1)
Total_property_and_equipment_net=sheet1.cell_value(15,2)
sales=sheet2.cell_value(3,2)
Sales_to_Net_Fixed_Assets =sales/Total_property_and_equipment_net
print("Sales to Net Fixed Assets  2019: {:,.2f}".format(Sales_to_Net_Fixed_Assets))


# In[13]:


# Net Fixed Assets to Equity = (Total property and equipment,net=Property and Equipment - Accumulated Depreciation) / Total Equity 

sheet = wb.sheet_by_index(3)
Total_property_and_equipment_net=sheet.cell_value(15,1)
Total_equity=sheet.cell_value(96,1)
Net_Fixed_Assets_to_Equity=Total_property_and_equipment_net/Total_equity
print("Net Fixed Assets to Equity 2020: {:,.2f}".format(Net_Fixed_Assets_to_Equity))


# In[14]:


sheet = wb.sheet_by_index(3)
Total_property_and_equipment_net=sheet.cell_value(15,2)
Total_equity=sheet.cell_value(96,2)
Net_Fixed_Assets_to_Equity=Total_property_and_equipment_net/Total_equity
print("Net Fixed Assets to Equity 2019: {:,.2f}".format(Net_Fixed_Assets_to_Equity))


# In[15]:


#Profitability Ratios:

# EBIT margin(operating margin) = (EBIT or operating income / sales )*100

sheet = wb.sheet_by_index(1)
sales=sheet.cell_value(3,1)
operating_income_or_loss=sheet.cell_value(16,1)
EBIT_margin=(operating_income_or_loss/sales)*100
print("EBIT Margin 2020: %{:,.2f}".format(EBIT_margin))


# In[16]:


sheet = wb.sheet_by_index(1)
sales=sheet.cell_value(3,2)
operating_income_or_loss=sheet.cell_value(16,2)
EBIT_margin=(operating_income_or_loss/sales)*100
print("EBIT Margin 2019: %{:,.2f}".format(EBIT_margin))


# In[17]:


sheet = wb.sheet_by_index(1)
sales=sheet.cell_value(3,3)
operating_income_or_loss=sheet.cell_value(16,3)
Percent_Gross_Profit=(operating_income_or_loss/sales)*100
print("Percent Gross Profit 2018: %{:,.2f}".format(Percent_Gross_Profit))


# In[18]:


# Percent Rate of Return on Assets = (Net income / Total assets)*100

sheet1 = wb.sheet_by_index(3)
sheet2 = wb.sheet_by_index(1)
Total_assets=sheet1.cell_value(75,1)
Net_income=sheet2.cell_value(24,1)
Percent_Rate_of_Return_on_Assets = (Net_income/Total_assets)*100
print("Percent Rate of Return on Assets 2020: %{:,.2f}".format(Percent_Rate_of_Return_on_Assets))


# In[19]:


sheet1 = wb.sheet_by_index(3)
sheet2 = wb.sheet_by_index(1)
Total_assets=sheet1.cell_value(75,2)
Net_income=sheet2.cell_value(24,2)
Percent_Rate_of_Return_on_Assets = (Net_income/Total_assets)*100
print("Percent Rate of Return on Assets 2019: %{:,.2f}".format(Percent_Rate_of_Return_on_Assets))


# In[20]:


# Percent Profit Margin on Sales (PM) = (Net income / Sales) * 100
sheet = wb.sheet_by_index(1)
sales=sheet.cell_value(3,1)
Net_income=sheet.cell_value(24,1)
Percent_Profit_Margin_on_Sales = (Net_income/sales)*100
print("Percent Profit Margin on Sales 2020: %{:,.2f}".format(Percent_Profit_Margin_on_Sales))


# In[21]:


sheet = wb.sheet_by_index(1)
sales=sheet.cell_value(3,2)
Net_income=sheet.cell_value(24,2)
Percent_Profit_Margin_on_Sales = (Net_income/sales)*100
print("Percent Profit Margin on Sales 2019: %{:,.2f}".format(Percent_Profit_Margin_on_Sales))


# In[22]:


# Percent Rate of Return on Equity (ROE) = (Earnings before Taxes / Total Equity )* 100
sheet1 = wb.sheet_by_index(3)
sheet2 = wb.sheet_by_index(1)
shareholder_equity=sheet1.cell_value(96,1)
Net_income=sheet2.cell_value(24,1)
ROE = (Net_income/shareholder_equity)*100
print("Percent Rate of Return on Equity (ROE) 2020: %{:,.2f}".format(ROE))


# In[23]:


sheet1 = wb.sheet_by_index(3)
sheet2 = wb.sheet_by_index(1)
shareholder_equity=sheet1.cell_value(96,2)
Net_income=sheet2.cell_value(24,2)
ROE = (Net_income/shareholder_equity)*100
print("Percent Rate of Return on Equity (ROE) 2019: %{:,.2f}".format(ROE))


# In[28]:


#Coverage Ratios

#Debt to Total Assets = Total Liabilities / Total Assets
sheet = wb.sheet_by_index(3)
Total_assets=sheet.cell_value(75,1)
Current_liabilities=sheet.cell_value(82,1)
Uncurrent_liabilities=sheet.cell_value(89,1)
Debt_to_Total_Assets = (Current_liabilities + Uncurrent_liabilities)/Total_assets
print("Debt to Total Assets 2020: {:,.2f}".format(Debt_to_Total_Assets))


# In[29]:


sheet = wb.sheet_by_index(3)
Total_assets=sheet.cell_value(75,2)
Current_liabilities=sheet.cell_value(82,2)
Uncurrent_liabilities=sheet.cell_value(89,2)
Debt_to_Total_Assets = (Current_liabilities + Uncurrent_liabilities)/Total_assets
print("Debt to Total Assets 2019: {:,.2f}".format(Debt_to_Total_Assets))


# In[30]:


#Percent Owners Equity = (Total Equity / Total Assets) * 100
sheet = wb.sheet_by_index(3)
Total_assets=sheet.cell_value(75,1)
Total_equity=sheet.cell_value(96,1)
Percent_Owners_Equity = (Total_equity/Total_assets)*100
print("Percent Owners Equity 2020: %{:,.2f}".format(Percent_Owners_Equity ))


# In[31]:


sheet = wb.sheet_by_index(3)
Total_assets=sheet.cell_value(75,2)
Total_equity=sheet.cell_value(96,2)
Percent_Owners_Equity = (Total_equity/Total_assets)*100
print("Percent Owners Equity 2019: %{:,.2f}".format(Percent_Owners_Equity ))


# In[ ]:




