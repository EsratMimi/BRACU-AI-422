# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
examinee = {'name':['Anastasia','Dima','Katherine','James','Emily','Micheal','Matthew','Laura','Kevin','Jonas'],
            'scores':[12.5,9,16.5,2.3,9,20,14.5,4.5,8,19],
            'attempts':[1,3,2,3,2,3,1,1,2,1],
            'qualified':['yes','no','yes','no','no','yes','yes','no','no','yes']}

data=pd.DataFrame(examinee)
#print(data.attempts)

data2=pd.Series(data.qualified)
#print(data2.dtype)
#print(d)
#data2=data.map(d) 

data2=data2.replace(to_replace='yes',
             value=1)
data2=data2.replace(to_replace='no',
             value=0)
"""i=0 
while i<data.qualified.size :
    
    if data.qualified[i] is 'yes' :
        data.qualified[i]=1
    else:
        data.qualified[i]=0
    i+=1
"""    
print(data2)