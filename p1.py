# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


#IMPORTING THE LIBRARIES
import pandas as pd
import matplotlib.pyplot as plt



#READING THE DATA FROM YOUR FILES
data=pd.read_csv("advertising.csv")
data.head()



# TO VISUALISE DATA
fig  ,axs = plt.subplots(1, 3,sharey=True)
data.plot(kind='scatter',x='TV',y='Sales',ax=axs[0],figsize=(14,7))
data.plot(kind='scatter',x='Radio',y='Sales',ax=axs[1])
data.plot(kind='scatter',x='Newspaper',y='Sales',ax=axs[2])



#CREATING X&Y FOR LINEAR REGRESSION
feature_cols =['TV']
X=data[feature_cols]
y=data.Sales


#IMPORTING LINEAR REGRESSION ALGO
from sklearn.linear_model import LinearRegression
lr=LinearRegression()
lr.fit(X, y)

print(lr.intercept_)
print(lr.coef_)





y=6.97+0.05546477*50
print(result)


#CREATE A DATAFRAM WITH MIN AND MAX VALUE OF THE TABLE
X_new=pd.DataFrame({'TV':[data.TV.min(),data.tv.max()]})
X_new.head()



preds = lr.predict(X_new)
preds


data.plot(kind='scatter',x='TV',y='Sales')

plt.plot(X_new,preds,c='red',linewidth=3)



import statsmodels.formula.api as smf
lr=smf.ols(formula='Sales ~ TV',data=data.fit())
lr.conf_int()



#FINDING THE PROBABLITY VALUES
lm.pvalues



#FINDING THE R-SQUARED VALUES
lm.rsquare



#muliti LINEAR REGRESSION
feature_cols=['TV','Radio','Newspaper']
X=data[feature_cols]
y=data.Sales


lr=LinearRegression()
lr.fit(X,y)


print(lr.intercept_)
print(lr.coef_)



lm =smf.ols(formul='Sales ~ TV+Radio+Newspaper',data=data).fit()
lm.conf_int()
lm.summary()