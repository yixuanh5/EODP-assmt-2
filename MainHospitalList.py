import pandas as pd
import argparse
import matplotlib.pyplot as plt

#read csv and extract datafram
hospital_data = pd.read_csv('MainHospitalList.csv', encoding = 'ISO-8859-1')
data_body = hospital_data.iloc[:,[3,5,8]]

#delet hospitals which do not have emergency department
data_body = data_body.set_index('Emergency Capable')
data_body = data_body.loc[['YES'],:]
#add a new column of number of hospital
j=1
i=0
number=[]
while i<39:
    i+=1
    number.append(j)

data_body['number'] = number

#count the number of hositipal in diferent suburb.
data_body_number = data_body.groupby(['Suburb']).sum()
data_body_number = data_body_number.reset_index()
#count the number of hosipital in different category
data_body_category = data_body.groupby(['Category']).sum()
data_body_category = data_body_category.reset_index()

#create the lists for plotting
suburb = data_body_number.iloc[:, 0]
number_of_hospital = data_body_number.iloc[:, 1]
category = data_body_category.iloc[:,0]
number_of_category = data_body_category.iloc[:,1]

#plot 
plt.scatter(suburb, number_of_hospital, s=20, color='blue')
plt.xticks(rotation=270)
plt.title('number of hospital in different suburb')
plt.xlabel('suburb')
plt.ylabel('number')
plt.savefig('number of hospital in different suburb.png')
plt.show()

plt.bar(category, number_of_category, width=0.3)
plt.title('number of hospital of different category')
plt.xlabel('category')
plt.ylabel('number')
plt.savefig('number of hospital of different category.png')
plt.show()
