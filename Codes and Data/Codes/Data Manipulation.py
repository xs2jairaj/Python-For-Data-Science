# -*- coding: utf-8 -*-
"""
Created on Wed May 04 12:45:21 2016

@author: Gunnvant
"""
## Test comment now
import pandas as pd
from pandas import DataFrame,Series
import numpy as np

import os
os.chdir('\')

data=pd.read_csv('oj.csv')

print data.head()
print data.shape

print type(data['brand'])
print type(data[['brand']])
print type(data.brand)

## Data Manipulation tasks:
# Filtering data
# Selecting columns 
# Sorting data
# Adding new columns
# Group By aggregations
# Handling dates
# Handling text
# Merging dataframes
# Treating Missing Values


#### Filtering data
# Using logical subsets
# Using query to subset


# All rows corresponding to brand tropicana
FLT1= data[data.brand=='tropicana']
print FLT1.shape

# Multiple subsets: Or and AND conditions
FLT2=data.query("brand=='tropicana' or brand=='minute.maid'")
FLT2.shape

FLT3=data.query("brand=='tropicana' & feat==1")
print FLT3.head()
print FLT3.shape

FLT2=data[(data['brand']=='tropicana') |  (data['brand']=='minute.maid') ]
FLT2.shape

#### Selecting Columns
# Selecting columns corresponding to brand and feat
SEL1=data[['brand','feat']]
SEL1.shape

#### Selecting Rows
# Selecting rows numbered 3,9,8
SEL2=data.ix[[3,9,8]]
SEL2.shape

#### Sorting data
SOR=data.sort_values('INCOME')
SOR.head()

SOR1=data.sort_values('INCOME',ascending=False)
SOR1.head()

SOR2=data.sort_values(['INCOME',"AGE60"],ascending=[False,True])
SOR2.head()

SOR3=data.sort_values(['brand','week'],ascending=[True,False])
SOR3.head()

#### Adding new columns to the data
#log of income
data=data.assign(log_inc=np.log(data.INCOME))
data['new_col']=np.log(data.HHLARGE)
data=data.assign(new_col1=np.log(data.INCOME),new_col2=np.log(data.INCOME))
#### Group by aggregations
# Grouping by one or more variable(s) and aggregating one column
# Grouping by one or more variable(s) and aggregating multiple columns in same way
# Grouping by one or more variable(s) and aggregating multiple columns differently
#Finding average price across brands
data.groupby('brand',as_index=False)['price'].mean()

#Finding average age, price across brands
data.groupby('brand',as_index=False)[['price','AGE60']].mean()

# Finding average age, total price across brands
data.groupby('brand',as_index=False).agg({'price':np.sum,'AGE60':np.mean}).rename(columns={'price':'Mean_price','AGE60':'Total_Age'})

# What if we want the names of new columns to be also changed
data.groupby('brand',as_index=False).agg({'price':{'Total_Price':np.sum},'AGE60':{'Mean_age':np.mean}})

a=data.groupby('brand',as_index=False).agg({'price':{'Total_Price':np.sum},'AGE60':{'Mean_age':np.mean}})
a.columns

# Finding average age, total price across brands and feature advertisements run
data.groupby(['brand','feat'],as_index=False).agg({'price':np.mean,'AGE60':np.sum}).rename(columns={'price':'Mean_price','AGE60':'Total_Age'})

###Window functions using transform
#Sorting data within group
data['logmove']=data.groupby('brand')['logmove'].transform(lambda x:x.sort_values(ascending=False))
data[['logmove','brand','price']].groupby('brand').head(5)

#### Handling dates
flt=pd.read_csv('Fd.csv')
print flt.dtypes

flt['FlightDate'].head(2)

flt['FlightDate']=pd.to_datetime(flt['FlightDate'],format="%d-%b-%y")
print flt.dtypes

m=flt.FlightDate.dt.month

m.head(2)

w=flt.FlightDate.dt.dayofweek #0=Monday,6=Sunday
print w.head(3)

#Generic Time classes in pandas
pd.to_datetime('15-06-16')
pd.Timestamp('15-06-16')

# Time stamps are different from time intervals
pd.to_datetime('15-06-16')-pd.to_datetime('14-06-16')

a=pd.to_datetime('15-06-16')-pd.to_datetime('14-06-16')

a/365

a/pd.to_timedelta(365,unit='D')
#If time interval is added to a timestamp we will get a future timestamp

pd.Timestamp('15-06-16')+pd.to_timedelta(365,unit='D')

#String manipulations
st=pd.read_csv("\")

print st.head()

st['Income_M'].mean()

st['Income_M']=st['Income_M'].str.replace("Rs","")
print st.head()

st['Income_M']=st['Income_M'].str.replace("/-","")
print st.head()

st['Income_M'].mean()

st.Income_M=st.Income_M.astype('float32')
st.Income_M.mean()

## Handling missing values
# Counting the number of missing values in each column
dat_m=pd.read_csv('\Credit.csv',na_values=['Missing',""])
# Number of missing values
dat_m.isnull().sum()

#Subsetting by missing values
dat_m[dat_m['MonthlyIncome'].isnull()]['DebtRatio']

#Replacing missing values
dat_m['age']=dat_m['age'].fillna(20)

## Joining data frames

dat1=data[['store','brand']]
dat2=data[['week','feat']]

pd.concat([dat1,dat2],axis=1)

dat3=dat1.ix[0:150]
dat4=dat1.ix[151:300]

pd.concat([dat3,dat4],axis=0)
pd.concat([dat3,dat4],axis=1)

## Merging DataFrames
df1=DataFrame({'CustomerID':[1,2,3,4,5,6],'Product':['Toaster','Toaster','Toaster','Radio','Radio','Radio']})
df2=DataFrame({'CustomerID':[2,4,6],'State':['Alabama','Alabama','Ohio']})

pd.merge(df1,df2,how='outer',on='CustomerID')

pd.merge(df1,df2,how='inner',on='CustomerID')

pd.merge(df1,df2,how='left',on='CustomerID')

pd.merge(df1,df2,how='right',on='CustomerID')

df1=DataFrame({'CustomerId':[1,2,3,4,5,6],'Product':['Toaster','Toaster','Toaster','Radio','Radio','Radio']})
df2=DataFrame({'CustomerID':[2,4,6],'State':['Alabama','Alabama','Ohio']})

pd.merge(df1,df2,how='inner',left_on='CustomerId',right_on='CustomerID').drop('CustomerID',axis=1)


