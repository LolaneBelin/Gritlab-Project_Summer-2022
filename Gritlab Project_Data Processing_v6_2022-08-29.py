# -*- coding: utf-8 -*-


"""
Created on Tue Jul 12 20:53:44 2022

@author: Lolane Belin

Data processing of the bed and weather data of the Gritlab Project from Juy 7th 2022 to August XXth 2022

"""


# 0/ Importing the necessary librairies for our code to run

import pandas as pd
import datetime
import numpy as np
import matplotlib.pyplot as plt
from math import *
import statistics

#Data presentation :
#
#
# At the end, there is 13 data tables (july_11, july_15, july_18, july_22, july_25, july_29, aug_1, aug_5, aug_8, aug_12, aug_15, aug_19, aug _, aug_26),
# (for example, july_22 contains the data from july 17 to july 22)
# and 1 data table containing all data from july 6 to august 26 : full_data


# 1/ Importing data :
    
july_18 = pd.read_csv(r"C:/Users/lolan/OneDrive/Bureau/Gritlab data/2022-07-18/18_july DATA PROCESSED.csv", sep = ";", header = None)
aug_29  = pd.read_csv(r"C:/Users/lolan/OneDrive/Bureau/Gritlab data/2022-08-29/29_aug DATA PROCESSED.csv", sep = ";", header = None)
july_11 = pd.read_csv(r"C:/Users/lolan/OneDrive/Bureau/Gritlab data/2022-07-11/11_july DATA PROCESSED.csv", sep = ";", header = None)


# 2/ Creatint lists of raw data manipulable through python

def temp_list(data_table):
    
    Time = []
    Temp_CntrlRoof = []
    Temp_UnderBed_GBR2 = []
    Temp_InSoil_GBR2 = []
    Temp_15AboveBed_GBR2 = []
    Temp_60AboveBed_GBR2 = []
    Temp_UnderBed_GBR1 = []
    Temp_InSoil_GBR1 = []
    Temp_15AboveBed_GBR1 = []
    Temp_60AboveBed_GBR1 = []
    Temp_UnderBed_GR2 = []
    Temp_InSoil_GR2 = []
    Temp_15AboveBed_GR2 = []
    Temp_60AboveBed_GR2 = []
    Temp_UnderBed_GR1 = []
    Temp_InSoil_GR1 = []
    Temp_15AboveBed_GR1 = []
    Temp_60AboveBed_GR1 = []
 
# Then we transform the data into float so that we can manipulate it with Python and put it in the right list


    for i in range (1,len(data_table)-1):
        
        Time.append(datetime.datetime(2022,int(data_table[0][i][3:5]),int(data_table[0][i][0:2]),int(data_table[0][i][11:13]),int(data_table[0][i][14:16])))
            
        Temp_CntrlRoof.append(float(data_table[5][i]))
            
        Temp_UnderBed_GBR2.append(float(data_table[6][i]))
        Temp_InSoil_GBR2.append(float(data_table[7][i]))
        Temp_15AboveBed_GBR2.append(float(data_table[8][i]))
        Temp_60AboveBed_GBR2.append(float(data_table[9][i]))
            
        Temp_UnderBed_GBR1.append(float(data_table[10][i]))
        Temp_InSoil_GBR1.append(float(data_table[11][i]))
        Temp_15AboveBed_GBR1.append(float(data_table[12][i]))
        Temp_60AboveBed_GBR1.append(float(data_table[13][i]))
            
        Temp_UnderBed_GR2.append(float(data_table[14][i]))
        Temp_InSoil_GR2.append(float(data_table[15][i]))
        Temp_15AboveBed_GR2.append(float(data_table[16][i]))
        Temp_60AboveBed_GR2.append(float(data_table[17][i]))
            
        Temp_UnderBed_GR1.append(float(data_table[18][i]))
        Temp_InSoil_GR1.append(float(data_table[19][i]))
        Temp_15AboveBed_GR1.append(float(data_table[20][i]))
        Temp_60AboveBed_GR1.append(float(data_table[21][i]))
           
#Fianly we return the lists

    return (Time,
                    Temp_CntrlRoof,
                    Temp_UnderBed_GBR2,
                    Temp_InSoil_GBR2,
                    Temp_15AboveBed_GBR2,
                    Temp_60AboveBed_GBR2,
                    Temp_UnderBed_GBR1,
                    Temp_InSoil_GBR1,
                    Temp_15AboveBed_GBR1,
                    Temp_60AboveBed_GBR1,
                    Temp_UnderBed_GR2,
                    Temp_InSoil_GR2,
                    Temp_15AboveBed_GR2,
                    Temp_60AboveBed_GR2,
                    Temp_UnderBed_GR1,
                    Temp_InSoil_GR1,
                    Temp_15AboveBed_GR1,
                    Temp_60AboveBed_GR1)
    

# 3/ Visualisating raw data

# 3/a) Visualisation of the temperatures of each bed

def temp_visu(data_table,n):
    
#Fisrt we import the lists we want to visualise 
    
    Time = temp_list(data_table)[0]
    Temp_CntrlRoof = temp_list(data_table)[1]
    Temp_UnderBed_GBR2 = temp_list(data_table)[2]
    Temp_InSoil_GBR2 = temp_list(data_table)[3]
    Temp_15AboveBed_GBR2 = temp_list(data_table)[4]
    Temp_60AboveBed_GBR2 = temp_list(data_table)[5]
    Temp_UnderBed_GBR1 = temp_list(data_table)[6]
    Temp_InSoil_GBR1 = temp_list(data_table)[7]
    Temp_15AboveBed_GBR1 = temp_list(data_table)[8]
    Temp_60AboveBed_GBR1 = temp_list(data_table)[9]
    Temp_UnderBed_GR2 = temp_list(data_table)[10]
    Temp_InSoil_GR2 = temp_list(data_table)[11]
    Temp_15AboveBed_GR2 = temp_list(data_table)[12]
    Temp_60AboveBed_GR2 = temp_list(data_table)[13]
    Temp_UnderBed_GR1 = temp_list(data_table)[14]
    Temp_InSoil_GR1 = temp_list(data_table)[15]
    Temp_15AboveBed_GR1 = temp_list(data_table)[16]
    Temp_60AboveBed_GR1 = temp_list(data_table)[17]
 

# Then we visualize the temperature according to the bed we are interested in

    if n==1 :
        plt.plot_date(Time, Temp_60AboveBed_GBR1,"-", label = 'Temperature 60cm Above Bed_GBR1')
        plt.plot_date(Time, Temp_15AboveBed_GBR1,"-", label = 'Temperature 15cm Above Bed_GBR1')
        plt.plot_date(Time, Temp_InSoil_GBR1,"-", label = 'Temperature of Soil_GBR1')
        plt.plot_date(Time, Temp_UnderBed_GBR1,"-", label = 'Temperature under the bed_GBR1')
        plt.plot_date(Time, Temp_CntrlRoof,"-", label = 'Temperature of Control Roof')
        plt.legend()
        plt.title("Temperatures of the GRB1")
        plt.show()
        
    elif n==2 :
        plt.plot_date(Time, Temp_60AboveBed_GBR2,"-", label = 'Temperature 60cm Above Bed_GBR2')
        plt.plot_date(Time, Temp_15AboveBed_GBR2,"-", label = 'Temperature 15cm Above Bed_GBR2')
        plt.plot_date(Time, Temp_InSoil_GBR2,"-", label = 'Temperature of Soil_GBR2')
        plt.plot_date(Time, Temp_UnderBed_GBR2,"-", label = 'Temperature under the bed_GBR2')
        plt.plot_date(Time, Temp_CntrlRoof,"-", label = 'Temperature of Control Roof')
        plt.legend()
        plt.title("Temperatures of the GRB2")
        plt.show()
        
    elif n==3 :
        plt.plot_date(Time, Temp_60AboveBed_GR1,"-", label = 'Temperature 60cm Above Bed_GR1')
        plt.plot_date(Time, Temp_15AboveBed_GR1,"-", label = 'Temperature 15cm Above Bed_GR1')
        plt.plot_date(Time, Temp_InSoil_GR1,"-", label = 'Temperature of Soil_GR1')
        plt.plot_date(Time, Temp_UnderBed_GR1,"-", label = 'Temperature under the bed_GR1')
        plt.plot_date(Time, Temp_CntrlRoof,"-", label = 'Temperature of Control Roof')
        plt.legend()
        plt.title("Temperatures of the GR1")
        plt.show()
        
    elif n==4 :
        plt.plot_date(Time, Temp_60AboveBed_GR2,"-", label = 'Temperature 60cm Above Bed_GR2')
        plt.plot_date(Time, Temp_15AboveBed_GR2,"-", label = 'Temperature 15cm Above Bed_GR2')
        plt.plot_date(Time, Temp_InSoil_GR2,"-", label = 'Temperature of Soil_GR2')
        plt.plot_date(Time, Temp_UnderBed_GR2,"-", label = 'Temperature under the bed_GR2')
        plt.plot_date(Time, Temp_CntrlRoof,"-", label = 'Temperature of Control Roof')
        plt.legend()
        plt.title("Temperatures of the GR2")
        plt.show()
    
# 3/b) Visualisation of the raingauge of each bed

def rain_visu(data_table):
    
    Time = []
    RainGauge_GBR2 = []
    RainGauge_GBR1 = []
    RainGauge_GR2 = []
    RainGauge_GR1 = []
    Rain = []
    
    for i in range (1,len(data_table)-1):
            Time.append(datetime.datetime(2022,int(data_table[0][i][3:5]),int(data_table[0][i][0:2]),int(data_table[0][i][11:13]),int(data_table[0][i][14:16]))) 
            RainGauge_GBR2.append(float(data_table[1][i])*0.01)
            RainGauge_GBR1.append(float(data_table[2][i])*0.01)
            RainGauge_GR2.append(float(data_table[3][i])*0.01)
            RainGauge_GR1.append(float(data_table[4][i])*0.01)
            Rain.append(float(data_table[22][i]))
#the raingauge from the test beds are on an area of 2m^2 when the area of the weather station is around 0.02m^2, so I put a coefficient to the test beds raingauge 
            
    plt.plot_date(Time, Rain,"-", label = 'Rainfall')
    plt.plot_date(Time, RainGauge_GR2,"-", label = 'Rain Gauge of GR2')
    plt.plot_date(Time, RainGauge_GR1,"-", label = 'Rain Gauge of GR1')
    plt.plot_date(Time, RainGauge_GBR2,"-", label = 'Rain Gauge of GBR2')
    plt.plot_date(Time, RainGauge_GBR1,"-", label = 'Rain Gauge of GBR1')
    
    plt.legend()
    plt.title("Raingauge of the GBR1,GBR2,GR1 and GR2")
    plt.show()
  

# 3/c) Visualisation of the solar radiation (hard to use in our case)

def solar_visu(data_table) :
    
    Time = []
    Solar_Radiation = []
    
    for i in range (1,len(data_table)-1):
        Time.append(datetime.datetime(2022,int(data_table[0][i][3:5]),int(data_table[0][i][0:2]),int(data_table[0][i][11:13]),int(data_table[0][i][15:17]))) 
        Solar_Radiation.append(float(data_table[23][i])/30)
    
    plt.plot_date(Time, Solar_Radiation,"-", label = 'Solar Radiation')
    plt.legend()
    plt.title("Solar Radiation")
    plt.show()
        
              
# 4/ Improving the readibility of the data

# Here I propose you different filters to denoise the data : averaging, moving average, the exponential moving average (or EMA), the Gaussian Kernel smoother, the nearest neighbour smoother, the local regression (or LOESS) and the and the Kalman filter (not used here)

# 4/a) exponential smoothing


def exponential_smoothing(data_table,n,k):
    
    a=exp(-(1/k))
    
    Time = temp_list(data_table)[0]
    Temp_CntrlRoof = temp_list(data_table)[1]
    Temp_UnderBed_GBR2 = temp_list(data_table)[2]
    Temp_InSoil_GBR2 = temp_list(data_table)[3]
    Temp_15AboveBed_GBR2 = temp_list(data_table)[4]
    Temp_60AboveBed_GBR2 = temp_list(data_table)[5]
    Temp_UnderBed_GBR1 = temp_list(data_table)[6]
    Temp_InSoil_GBR1 = temp_list(data_table)[7]
    Temp_15AboveBed_GBR1 = temp_list(data_table)[8]
    Temp_60AboveBed_GBR1 = temp_list(data_table)[9]
    Temp_UnderBed_GR2 = temp_list(data_table)[10]
    Temp_InSoil_GR2 = temp_list(data_table)[11]
    Temp_15AboveBed_GR2 = temp_list(data_table)[12]
    Temp_60AboveBed_GR2 = temp_list(data_table)[13]
    Temp_UnderBed_GR1 = temp_list(data_table)[14]
    Temp_InSoil_GR1 = temp_list(data_table)[15]
    Temp_15AboveBed_GR1 = temp_list(data_table)[16]
    Temp_60AboveBed_GR1 = temp_list(data_table)[17]
    
   
    Avg_Temp_CntrlRoof = []
    Avg_Temp_UnderBed_GBR2 = []
    Avg_Temp_InSoil_GBR2 = []
    Avg_Temp_15AboveBed_GBR2 = []
    Avg_Temp_60AboveBed_GBR2 = []
    Avg_Temp_UnderBed_GBR1 = []
    Avg_Temp_InSoil_GBR1 = []
    Avg_Temp_15AboveBed_GBR1 = []
    Avg_Temp_60AboveBed_GBR1 = []
    Avg_Temp_UnderBed_GR2 = []
    Avg_Temp_InSoil_GR2 = []
    Avg_Temp_15AboveBed_GR2 = []
    Avg_Temp_60AboveBed_GR2 = []
    Avg_Temp_UnderBed_GR1 = []
    Avg_Temp_InSoil_GR1 = []
    Avg_Temp_15AboveBed_GR1 = []
    Avg_Temp_60AboveBed_GR1 = []
    
   
    Avg_Temp_CntrlRoof.append(Temp_CntrlRoof[0])
    Avg_Temp_UnderBed_GBR2.append(Temp_UnderBed_GBR2[0])
    Avg_Temp_InSoil_GBR2.append(Temp_InSoil_GBR2[0])
    Avg_Temp_15AboveBed_GBR2.append(Temp_15AboveBed_GBR2[0])
    Avg_Temp_60AboveBed_GBR2.append(Temp_60AboveBed_GBR2[0])
    Avg_Temp_UnderBed_GBR1.append(Temp_UnderBed_GBR1[0])
    Avg_Temp_InSoil_GBR1.append(Temp_InSoil_GBR1[0])
    Avg_Temp_15AboveBed_GBR1.append(Temp_15AboveBed_GBR1[0])
    Avg_Temp_60AboveBed_GBR1.append(Temp_60AboveBed_GBR1[0])
    Avg_Temp_UnderBed_GR2.append(Temp_UnderBed_GR2[0])
    Avg_Temp_InSoil_GR2.append(Temp_InSoil_GR2[0])
    Avg_Temp_15AboveBed_GR2.append(Temp_15AboveBed_GR2[0])
    Avg_Temp_60AboveBed_GR2.append(Temp_60AboveBed_GR2[0])
    Avg_Temp_UnderBed_GR1.append(Temp_UnderBed_GR1[0])
    Avg_Temp_InSoil_GR1.append(Temp_InSoil_GR1[0])
    Avg_Temp_15AboveBed_GR1.append(Temp_15AboveBed_GR1[0])
    Avg_Temp_60AboveBed_GR1.append(Temp_60AboveBed_GR1[0])
    
    for p in range (1, len(data_table)-1):
        
        Avg_Temp_CntrlRoof.append(a*(Temp_CntrlRoof[p])+(1-a)*(Avg_Temp_CntrlRoof[p-1]))
        Avg_Temp_UnderBed_GBR2.append(a*(Temp_UnderBed_GBR2[p])+(1-a)*(Avg_Temp_UnderBed_GBR2[p-1]))
        Avg_Temp_InSoil_GBR2.append(a*(Temp_InSoil_GBR2[p])+(1-a)*(Avg_Temp_InSoil_GBR2[p-1]))
        Avg_Temp_15AboveBed_GBR2.append(a*(Temp_15AboveBed_GBR2[p])+(1-a)*(Avg_Temp_15AboveBed_GBR2[p-1]))
        Avg_Temp_60AboveBed_GBR2.append(a*(Temp_60AboveBed_GBR2[p])+(1-a)*(Avg_Temp_60AboveBed_GBR2[p-1]))
        Avg_Temp_UnderBed_GBR1.append(a*(Temp_UnderBed_GBR1[p])+(1-a)*(Avg_Temp_UnderBed_GBR1[p-1]))
        Avg_Temp_InSoil_GBR1.append(a*(Temp_InSoil_GBR1[p])+(1-a)*(Avg_Temp_InSoil_GBR1[p-1]))
        Avg_Temp_15AboveBed_GBR1.append(a*(Temp_15AboveBed_GBR1[p])+(1-a)*(Avg_Temp_15AboveBed_GBR1[p-1]))
        Avg_Temp_60AboveBed_GBR1.append(a*(Temp_60AboveBed_GBR1[p])+(1-a)*(Avg_Temp_60AboveBed_GBR1[p-1]))
        Avg_Temp_UnderBed_GR2.append(a*(Temp_UnderBed_GR2[p])+(1-a)*(Avg_Temp_UnderBed_GR2[p-1]))
        Avg_Temp_InSoil_GR2.append(a*(Temp_InSoil_GR2[p])+(1-a)*(Avg_Temp_InSoil_GR2[p-1]))
        Avg_Temp_15AboveBed_GR2.append(a*(Temp_15AboveBed_GR2[p])+(1-a)*(Avg_Temp_15AboveBed_GR2[p-1]))
        Avg_Temp_60AboveBed_GR2.append(a*(Temp_60AboveBed_GR2[p])+(1-a)*(Avg_Temp_60AboveBed_GR2[p-1]))
        Avg_Temp_UnderBed_GR1.append(a*(Temp_UnderBed_GR1[p])+(1-a)*(Avg_Temp_UnderBed_GR1[p-1]))
        Avg_Temp_InSoil_GR1.append(a*(Temp_InSoil_GR1[p])+(1-a)*(Avg_Temp_InSoil_GR1[p-1]))
        Avg_Temp_15AboveBed_GR1.append(a*(Temp_15AboveBed_GR1[p])+(1-a)*(Avg_Temp_15AboveBed_GR1[p-1]))
        Avg_Temp_60AboveBed_GR1.append(a*(Temp_60AboveBed_GR1[p])+(1-a)*(Avg_Temp_60AboveBed_GR1[p-1]))
        
    
    if n==1 :
        plt.plot_date(Time, Avg_Temp_60AboveBed_GBR1,"-", label = 'Temperature 60cm Above Bed_GBR1')
        plt.plot_date(Time, Avg_Temp_15AboveBed_GBR1,"-", label = 'Temperature 15cm Above Bed_GBR1')
        plt.plot_date(Time, Avg_Temp_InSoil_GBR1,"-", label = 'Temperature of Soil_GBR1')
        plt.plot_date(Time, Avg_Temp_UnderBed_GBR1,"-", label = 'Temperature under the bed_GBR1')
        plt.plot_date(Time, Avg_Temp_CntrlRoof,"-", label = 'Temperature of Control Roof')
        plt.legend()
        plt.title("Temperatures of the GRB1")
        plt.show()
        
    elif n==2 :
        plt.plot_date(Time, Avg_Temp_60AboveBed_GBR2,"-", label = 'Temperature 60cm Above Bed_GBR2')
        plt.plot_date(Time, Avg_Temp_15AboveBed_GBR2,"-", label = 'Temperature 15cm Above Bed_GBR2')
        plt.plot_date(Time, Avg_Temp_InSoil_GBR2,"-", label = 'Temperature of Soil_GBR2')
        plt.plot_date(Time, Avg_Temp_UnderBed_GBR2,"-", label = 'Temperature under the bed_GBR2')
        plt.plot_date(Time, Avg_Temp_CntrlRoof,"-", label = 'Temperature of Control Roof')
        plt.legend()
        plt.title("Temperatures of the GRB2")
        plt.show()
        
    elif n==3 :
        plt.plot_date(Time, Avg_Temp_60AboveBed_GR1,"-", label = 'Temperature 60cm Above Bed_GR1')
        plt.plot_date(Time, Avg_Temp_15AboveBed_GR1,"-", label = 'Temperature 15cm Above Bed_GR1')
        plt.plot_date(Time, Avg_Temp_InSoil_GR1,"-", label = 'Temperature of Soil_GR1')
        plt.plot_date(Time, Avg_Temp_UnderBed_GR1,"-", label = 'Temperature under the bed_GR1')
        plt.plot_date(Time, Avg_Temp_CntrlRoof,"-", label = 'Temperature of Control Roof')
        plt.legend()
        plt.title("Temperatures of the GR1")
        plt.show()
        
    elif n==4 :
        plt.plot_date(Time, Avg_Temp_60AboveBed_GR2,"-", label = 'Temperature 60cm Above Bed_GR2')
        plt.plot_date(Time, Avg_Temp_15AboveBed_GR2,"-", label = 'Temperature 15cm Above Bed_GR2')
        plt.plot_date(Time, Avg_Temp_InSoil_GR2,"-", label = 'Temperature of Soil_GR2')
        plt.plot_date(Time, Avg_Temp_UnderBed_GR2,"-", label = 'Temperature under the bed_GR2')
        plt.plot_date(Time, Avg_Temp_CntrlRoof,"-", label = 'Temperature of Control Roof')
        plt.legend()
        plt.title("Temperatures of the GR2")
        plt.show()

# 4/b) Comparing lists to see if using all of them is relevant

def correlation(data_table,n):
    

# First we name the Sum we are gonna use in the code to access the average (sum(data)/numb(data))
    
    Sum_Temp_UnderBed_GBR2 = 0
    Sum_Temp_InSoil_GBR2 = 0
    Sum_Temp_15AboveBed_GBR2 = 0
    Sum_Temp_60AboveBed_GBR2 = 0
    Sum_Temp_UnderBed_GBR1 = 0
    Sum_Temp_InSoil_GBR1 = 0
    Sum_Temp_15AboveBed_GBR1 = 0
    Sum_Temp_60AboveBed_GBR1 = 0
    Sum_Temp_UnderBed_GR2 = 0
    Sum_Temp_InSoil_GR2 = 0
    Sum_Temp_15AboveBed_GR2 = 0
    Sum_Temp_60AboveBed_GR2 = 0
    Sum_Temp_UnderBed_GR1 = 0
    Sum_Temp_InSoil_GR1 = 0
    Sum_Temp_15AboveBed_GR1 = 0
    Sum_Temp_60AboveBed_GR1 = 0
    S=0
 
# Then we sum up each data in each list to get the average of each list

    for i in range (1,len(data_table)-1):
            
            Sum_Temp_UnderBed_GBR2+=float(data_table[6][i])
            Sum_Temp_InSoil_GBR2+=float(data_table[7][i])
            Sum_Temp_15AboveBed_GBR2+=float(data_table[8][i])
            Sum_Temp_60AboveBed_GBR2+=float(data_table[9][i])
            
            Sum_Temp_UnderBed_GBR1+=float(data_table[10][i])
            Sum_Temp_InSoil_GBR1+=float(data_table[11][i])
            Sum_Temp_15AboveBed_GBR1+=float(data_table[12][i])
            Sum_Temp_60AboveBed_GBR1+=float(data_table[13][i])
            
            Sum_Temp_UnderBed_GR2+=float(data_table[14][i])
            Sum_Temp_InSoil_GR2+=float(data_table[15][i])
            Sum_Temp_15AboveBed_GR2+=float(data_table[16][i])
            Sum_Temp_60AboveBed_GR2+=float(data_table[17][i])
            
            Sum_Temp_UnderBed_GR1+=float(data_table[18][i])
            Sum_Temp_InSoil_GR1+=float(data_table[19][i])
            Sum_Temp_15AboveBed_GR1+=float(data_table[20][i])
            Sum_Temp_60AboveBed_GR1+=float(data_table[21][i])
            
            S+=1
    
#Then we calculate the average of each list :
    
    
    Avg_Temp_UnderBed_GBR2=Sum_Temp_UnderBed_GBR2/S
    Avg_Temp_InSoil_GBR2=Sum_Temp_InSoil_GBR2/S
    Avg_Temp_15AboveBed_GBR2=Sum_Temp_15AboveBed_GBR2/S
    Avg_Temp_60AboveBed_GBR2=Sum_Temp_60AboveBed_GBR2/S

    Avg_Temp_UnderBed_GBR1=Sum_Temp_UnderBed_GBR1/S
    Avg_Temp_InSoil_GBR1=Sum_Temp_15AboveBed_GBR1/S
    Avg_Temp_15AboveBed_GBR1=Sum_Temp_15AboveBed_GBR1/S
    Avg_Temp_60AboveBed_GBR1=Sum_Temp_60AboveBed_GBR1/S
    
    Avg_Temp_UnderBed_GR2=Sum_Temp_UnderBed_GR2/S
    Avg_Temp_InSoil_GR2=Sum_Temp_InSoil_GR2/S
    Avg_Temp_15AboveBed_GR2=Sum_Temp_15AboveBed_GR2/S
    Avg_Temp_60AboveBed_GR2=Sum_Temp_60AboveBed_GR2/S
    
    Avg_Temp_UnderBed_GR1=Sum_Temp_UnderBed_GR1/S
    Avg_Temp_InSoil_GR1=Sum_Temp_InSoil_GR1/S
    Avg_Temp_15AboveBed_GR1=Sum_Temp_15AboveBed_GR1/S
    Avg_Temp_60AboveBed_GR1=Sum_Temp_60AboveBed_GR1/S
    
#Then we calculate the variance and covariance of the list we are interested in 
    
    
    Variance_Sum_Temp_UnderBed_GBR2 = 0
    Variance_Sum_Temp_InSoil_GBR2 = 0
    Variance_Sum_Temp_15AboveBed_GBR2 = 0
    Variance_Sum_Temp_60AboveBed_GBR2 = 0
    Covariance_Sum_Und_InS_GBR2 = 0
    Covariance_Sum_Und_15A_GBR2 = 0
    Covariance_Sum_Und_60A_GBR2 = 0
    Covariance_Sum_InS_15A_GBR2 = 0
    Covariance_Sum_InS_60A_GBR2 = 0
    Covariance_Sum_15A_60A_GBR2 = 0
    
    Variance_Sum_Temp_UnderBed_GBR1 = 0
    Variance_Sum_Temp_InSoil_GBR1 = 0
    Variance_Sum_Temp_15AboveBed_GBR1 = 0
    Variance_Sum_Temp_60AboveBed_GBR1 = 0
    Covariance_Sum_Und_InS_GBR1 = 0
    Covariance_Sum_Und_15A_GBR1 = 0
    Covariance_Sum_Und_60A_GBR1 = 0
    Covariance_Sum_InS_15A_GBR1 = 0
    Covariance_Sum_InS_60A_GBR1 = 0
    Covariance_Sum_15A_60A_GBR1 = 0
    
    Variance_Sum_Temp_UnderBed_GR2 = 0
    Variance_Sum_Temp_InSoil_GR2 = 0
    Variance_Sum_Temp_15AboveBed_GR2 = 0
    Variance_Sum_Temp_60AboveBed_GR2 = 0
    Covariance_Sum_Und_InS_GR2 = 0
    Covariance_Sum_Und_15A_GR2 = 0
    Covariance_Sum_Und_60A_GR2 = 0
    Covariance_Sum_InS_15A_GR2 = 0
    Covariance_Sum_InS_60A_GR2 = 0
    Covariance_Sum_15A_60A_GR2 = 0
    
    Variance_Sum_Temp_UnderBed_GR1 = 0
    Variance_Sum_Temp_InSoil_GR1 = 0
    Variance_Sum_Temp_15AboveBed_GR1 = 0
    Variance_Sum_Temp_60AboveBed_GR1 = 0
    Covariance_Sum_Und_InS_GR1 = 0
    Covariance_Sum_Und_15A_GR1 = 0
    Covariance_Sum_Und_60A_GR1 = 0
    Covariance_Sum_InS_15A_GR1 = 0
    Covariance_Sum_InS_60A_GR1 = 0
    Covariance_Sum_15A_60A_GR1 = 0

    if n==2:
        for i in range (1,len(data_table)-1) :
            
            Variance_Sum_Temp_UnderBed_GBR2 += (float(data_table[6][i])-Avg_Temp_UnderBed_GBR2)**2
            Variance_Sum_Temp_InSoil_GBR2 += (float(data_table[7][i])-Avg_Temp_InSoil_GBR2)**2
            Variance_Sum_Temp_15AboveBed_GBR2 += (float(data_table[8][i])-Avg_Temp_15AboveBed_GBR2)**2
            Variance_Sum_Temp_60AboveBed_GBR2 += (float(data_table[9][i])-Avg_Temp_60AboveBed_GBR2)**2
            Covariance_Sum_Und_InS_GBR2 += (float(data_table[6][i])-Avg_Temp_UnderBed_GBR2)*(float(data_table[7][i])-Avg_Temp_InSoil_GBR2)
            Covariance_Sum_Und_15A_GBR2 += (float(data_table[6][i])-Avg_Temp_UnderBed_GBR2)*(float(data_table[8][i])-Avg_Temp_15AboveBed_GBR2)
            Covariance_Sum_Und_60A_GBR2 += (float(data_table[6][i])-Avg_Temp_UnderBed_GBR2)*(float(data_table[9][i])-Avg_Temp_60AboveBed_GBR2)
            Covariance_Sum_InS_15A_GBR2 += (float(data_table[7][i])-Avg_Temp_InSoil_GBR2)*(float(data_table[8][i])-Avg_Temp_15AboveBed_GBR2)
            Covariance_Sum_InS_60A_GBR2 += (float(data_table[7][i])-Avg_Temp_InSoil_GBR2)*(float(data_table[9][i])-Avg_Temp_60AboveBed_GBR2)
            Covariance_Sum_15A_60A_GBR2 += (float(data_table[8][i])-Avg_Temp_15AboveBed_GBR2)*(float(data_table[9][i])-Avg_Temp_60AboveBed_GBR2)
    
        Variance_Temp_UnderBed_GBR2 = Variance_Sum_Temp_UnderBed_GBR2/S
        Variance_Temp_InSoil_GBR2 = Variance_Sum_Temp_InSoil_GBR2/S
        Variance_Temp_15AboveBed_GBR2 = Variance_Sum_Temp_15AboveBed_GBR2/S
        Variance_Temp_60AboveBed_GBR2 = Variance_Sum_Temp_60AboveBed_GBR2/S
        Covariance_Und_InS_GBR2 = Covariance_Sum_Und_InS_GBR2/S
        Covariance_Und_15A_GBR2 = Covariance_Sum_Und_15A_GBR2/S
        Covariance_Und_60A_GBR2 = Covariance_Sum_Und_60A_GBR2/S
        Covariance_InS_15A_GBR2 = Covariance_Sum_InS_15A_GBR2/S
        Covariance_InS_60A_GBR2 = Covariance_Sum_InS_60A_GBR2/S
        Covariance_15A_60A_GBR2 = Covariance_Sum_15A_60A_GBR2/S
        
        Correlation_Und_InS_GBR2 = Covariance_Und_InS_GBR2*100/(((Variance_Temp_UnderBed_GBR2)**(1/2))*((Variance_Temp_InSoil_GBR2)**(1/2)))
        Correlation_Und_15A_GBR2 = Covariance_Und_15A_GBR2*100/(((Variance_Temp_UnderBed_GBR2)**(1/2))*((Variance_Temp_15AboveBed_GBR2)**(1/2)))
        Correlation_Und_60A_GBR2 = Covariance_Und_60A_GBR2*100/(((Variance_Temp_UnderBed_GBR2)**(1/2))*((Variance_Temp_60AboveBed_GBR2)*(1/2)))
        Correlation_InS_15A_GBR2 = Covariance_InS_15A_GBR2*100/(((Variance_Temp_InSoil_GBR2)**(1/2))*((Variance_Temp_15AboveBed_GBR2)**(1/2)))
        Correlation_InS_60A_GBR2 = Covariance_InS_60A_GBR2*100/(((Variance_Temp_InSoil_GBR2)**(1/2))*((Variance_Temp_60AboveBed_GBR2)**(1/2)))
        Correlation_15A_60A_GBR2 = Covariance_15A_60A_GBR2*100/(((Variance_Temp_15AboveBed_GBR2)**(1/2))*((Variance_Temp_60AboveBed_GBR2)**(1/2)))
        
        print('In the bed GBR2, \n the correlation between the temperature under the bed and in the soil is r=',round(Correlation_Und_InS_GBR2,2),'% \n the correlation between the temperature under the bed and 15cm above it is r=',round(Correlation_Und_15A_GBR2,2),'% \n the correlation between the temperature under the bed and 60cm above it is r=',round(Correlation_Und_60A_GBR2,2),'% \n the correlation between the temperature in the soil and 15cm above the bed is r=',round(Correlation_InS_15A_GBR2,2),'% \n the correlation between the temperature in the soil and 60cm above th bed is r=',round(Correlation_InS_60A_GBR2,2),'% \n the correlation between the temperature 15cm above the bed and 60cm above it r=',round(Correlation_15A_60A_GBR2,2),'%')
    
    if n==1:
        for i in range (1,len(data_table)-1) :
            
            Variance_Sum_Temp_UnderBed_GBR1 += (float(data_table[10][i])-Avg_Temp_UnderBed_GBR1)**2
            Variance_Sum_Temp_InSoil_GBR1 += (float(data_table[11][i])-Avg_Temp_InSoil_GBR1)**2
            Variance_Sum_Temp_15AboveBed_GBR1 += (float(data_table[12][i])-Avg_Temp_15AboveBed_GBR1)**2
            Variance_Sum_Temp_60AboveBed_GBR1 += (float(data_table[13][i])-Avg_Temp_60AboveBed_GBR1)**2
            Covariance_Sum_Und_InS_GBR1 += (float(data_table[10][i])-Avg_Temp_UnderBed_GBR1)*(float(data_table[11][i])-Avg_Temp_InSoil_GBR1)
            Covariance_Sum_Und_15A_GBR1 += (float(data_table[10][i])-Avg_Temp_UnderBed_GBR1)*(float(data_table[12][i])-Avg_Temp_15AboveBed_GBR1)
            Covariance_Sum_Und_60A_GBR1 += (float(data_table[10][i])-Avg_Temp_UnderBed_GBR1)*(float(data_table[13][i])-Avg_Temp_60AboveBed_GBR1)
            Covariance_Sum_InS_15A_GBR1 += (float(data_table[11][i])-Avg_Temp_InSoil_GBR1)*(float(data_table[12][i])-Avg_Temp_15AboveBed_GBR1)
            Covariance_Sum_InS_60A_GBR1 += (float(data_table[11][i])-Avg_Temp_InSoil_GBR1)*(float(data_table[13][i])-Avg_Temp_60AboveBed_GBR1)
            Covariance_Sum_15A_60A_GBR1 += (float(data_table[12][i])-Avg_Temp_15AboveBed_GBR1)*(float(data_table[13][i])-Avg_Temp_60AboveBed_GBR1)
         
        Variance_Temp_UnderBed_GBR1 = Variance_Sum_Temp_UnderBed_GBR1/S
        Variance_Temp_InSoil_GBR1 = Variance_Sum_Temp_InSoil_GBR1/S
        Variance_Temp_15AboveBed_GBR1 = Variance_Sum_Temp_15AboveBed_GBR1/S
        Variance_Temp_60AboveBed_GBR1 = Variance_Sum_Temp_60AboveBed_GBR1/S
        Covariance_Und_InS_GBR1 = Covariance_Sum_Und_InS_GBR1/S
        Covariance_Und_15A_GBR1 = Covariance_Sum_Und_15A_GBR1/S
        Covariance_Und_60A_GBR1 = Covariance_Sum_Und_60A_GBR1/S
        Covariance_InS_15A_GBR1 = Covariance_Sum_InS_15A_GBR1/S
        Covariance_InS_60A_GBR1 = Covariance_Sum_InS_60A_GBR1/S
        Covariance_15A_60A_GBR1 = Covariance_Sum_15A_60A_GBR1/S
        
        Correlation_Und_InS_GBR1 = Covariance_Und_InS_GBR1*100/(((Variance_Temp_UnderBed_GBR1)**(1/2))*((Variance_Temp_InSoil_GBR1)**(1/2)))
        Correlation_Und_15A_GBR1 = Covariance_Und_15A_GBR1*100/(((Variance_Temp_UnderBed_GBR1)**(1/2))*((Variance_Temp_15AboveBed_GBR1)**(1/2)))
        Correlation_Und_60A_GBR1 = Covariance_Und_60A_GBR1*100/(((Variance_Temp_UnderBed_GBR1)**(1/2))*((Variance_Temp_60AboveBed_GBR1)*(1/2)))
        Correlation_InS_15A_GBR1 = Covariance_InS_15A_GBR1*100/(((Variance_Temp_InSoil_GBR1)**(1/2))*((Variance_Temp_15AboveBed_GBR1)**(1/2)))
        Correlation_InS_60A_GBR1 = Covariance_InS_60A_GBR1*100/(((Variance_Temp_InSoil_GBR1)**(1/2))*((Variance_Temp_60AboveBed_GBR1)**(1/2)))
        Correlation_15A_60A_GBR1 = Covariance_15A_60A_GBR1*100/(((Variance_Temp_15AboveBed_GBR1)**(1/2))*((Variance_Temp_60AboveBed_GBR1)**(1/2)))
        
        print('In the bed GBR1, \n the correlation between the temperature under the bed and in the soil is r=',round(Correlation_Und_InS_GBR1,2),'% \n the correlation between the temperature under the bed and 15cm above it is r=',round(Correlation_Und_15A_GBR1,2),'% \n the correlation between the temperature under the bed and 60cm above it is r=',round(Correlation_Und_60A_GBR1,2),'% \n the correlation between the temperature in the soil and 15cm above the bed is r=',round(Correlation_InS_15A_GBR1,2),'% \n the correlation between the temperature in the soil and 60cm above th bed is r=',round(Correlation_InS_60A_GBR1,2),'% \n the correlation between the temperature 15cm above the bed and 60cm above it r=',round(Correlation_15A_60A_GBR1,2),'%')
        
    if n==4:
        for i in range (1,len(data_table)-1) :
            
            Variance_Sum_Temp_UnderBed_GR2 += (float(data_table[14][i])-Avg_Temp_UnderBed_GR2)**2
            Variance_Sum_Temp_InSoil_GR2 += (float(data_table[15][i])-Avg_Temp_InSoil_GR2)**2
            Variance_Sum_Temp_15AboveBed_GR2 += (float(data_table[16][i])-Avg_Temp_15AboveBed_GR2)**2
            Variance_Sum_Temp_60AboveBed_GR2 += (float(data_table[17][i])-Avg_Temp_60AboveBed_GR2)**2
            Covariance_Sum_Und_InS_GR2 += (float(data_table[14][i])-Avg_Temp_UnderBed_GR2)*(float(data_table[15][i])-Avg_Temp_InSoil_GR2)
            Covariance_Sum_Und_15A_GR2 += (float(data_table[14][i])-Avg_Temp_UnderBed_GR2)*(float(data_table[16][i])-Avg_Temp_15AboveBed_GR2)
            Covariance_Sum_Und_60A_GR2 += (float(data_table[14][i])-Avg_Temp_UnderBed_GR2)*(float(data_table[17][i])-Avg_Temp_60AboveBed_GR2)
            Covariance_Sum_InS_15A_GR2 += (float(data_table[15][i])-Avg_Temp_InSoil_GR2)*(float(data_table[16][i])-Avg_Temp_15AboveBed_GR2)
            Covariance_Sum_InS_60A_GR2 += (float(data_table[15][i])-Avg_Temp_InSoil_GR2)*(float(data_table[17][i])-Avg_Temp_60AboveBed_GR2)
            Covariance_Sum_15A_60A_GR2 += (float(data_table[16][i])-Avg_Temp_15AboveBed_GR2)*(float(data_table[17][i])-Avg_Temp_60AboveBed_GR2)
    
        Variance_Temp_UnderBed_GR2 = Variance_Sum_Temp_UnderBed_GR2/S
        Variance_Temp_InSoil_GR2 = Variance_Sum_Temp_InSoil_GR2/S
        Variance_Temp_15AboveBed_GR2 = Variance_Sum_Temp_15AboveBed_GR2/S
        Variance_Temp_60AboveBed_GR2 = Variance_Sum_Temp_60AboveBed_GR2/S
        Covariance_Und_InS_GR2 = Covariance_Sum_Und_InS_GR2/S
        Covariance_Und_15A_GR2 = Covariance_Sum_Und_15A_GR2/S
        Covariance_Und_60A_GR2 = Covariance_Sum_Und_60A_GR2/S
        Covariance_InS_15A_GR2 = Covariance_Sum_InS_15A_GR2/S
        Covariance_InS_60A_GR2 = Covariance_Sum_InS_60A_GR2/S
        Covariance_15A_60A_GR2 = Covariance_Sum_15A_60A_GR2/S
        
        Correlation_Und_InS_GR2 = Covariance_Und_InS_GR2*100/(((Variance_Temp_UnderBed_GR2)**(1/2))*((Variance_Temp_InSoil_GR2)**(1/2)))
        Correlation_Und_15A_GR2 = Covariance_Und_15A_GR2*100/(((Variance_Temp_UnderBed_GR2)**(1/2))*((Variance_Temp_15AboveBed_GR2)**(1/2)))
        Correlation_Und_60A_GR2 = Covariance_Und_60A_GR2*100/(((Variance_Temp_UnderBed_GR2)**(1/2))*((Variance_Temp_60AboveBed_GR2)*(1/2)))
        Correlation_InS_15A_GR2 = Covariance_InS_15A_GR2*100/(((Variance_Temp_InSoil_GR2)**(1/2))*((Variance_Temp_15AboveBed_GR2)**(1/2)))
        Correlation_InS_60A_GR2 = Covariance_InS_60A_GR2*100/(((Variance_Temp_InSoil_GR2)**(1/2))*((Variance_Temp_60AboveBed_GR2)**(1/2)))
        Correlation_15A_60A_GR2 = Covariance_15A_60A_GR2*100/(((Variance_Temp_15AboveBed_GR2)**(1/2))*((Variance_Temp_60AboveBed_GR2)**(1/2)))
        
        print('In the bed GR2, \n the correlation between the temperature under the bed and in the soil is r=',round(Correlation_Und_InS_GR2,2),'% \n the correlation between the temperature under the bed and 15cm above it is r=',round(Correlation_Und_15A_GR2,2),'% \n the correlation between the temperature under the bed and 60cm above it is r=',round(Correlation_Und_60A_GR2,2),'% \n the correlation between the temperature in the soil and 15cm above the bed is r=',round(Correlation_InS_15A_GR2,2),'% \n the correlation between the temperature in the soil and 60cm above th bed is r=',round(Correlation_InS_60A_GR2,2),'% \n the correlation between the temperature 15cm above the bed and 60cm above it r=',round(Correlation_15A_60A_GR2,2),'%')
        
    if n==3:
        for i in range (1,len(data_table)-1) :
            
            Variance_Sum_Temp_UnderBed_GR1 += (float(data_table[18][i])-Avg_Temp_UnderBed_GR1)**2
            Variance_Sum_Temp_InSoil_GR1 += (float(data_table[19][i])-Avg_Temp_InSoil_GR1)**2
            Variance_Sum_Temp_15AboveBed_GR1 += (float(data_table[20][i])-Avg_Temp_15AboveBed_GR1)**2
            Variance_Sum_Temp_60AboveBed_GR1 += (float(data_table[21][i])-Avg_Temp_60AboveBed_GR1)**2
            Covariance_Sum_Und_InS_GR1 += (float(data_table[18][i])-Avg_Temp_UnderBed_GR1)*(float(data_table[19][i])-Avg_Temp_InSoil_GR1)
            Covariance_Sum_Und_15A_GR1 += (float(data_table[18][i])-Avg_Temp_UnderBed_GR1)*(float(data_table[20][i])-Avg_Temp_15AboveBed_GR1)
            Covariance_Sum_Und_60A_GR1 += (float(data_table[18][i])-Avg_Temp_UnderBed_GR1)*(float(data_table[21][i])-Avg_Temp_60AboveBed_GR1)
            Covariance_Sum_InS_15A_GR1 += (float(data_table[19][i])-Avg_Temp_InSoil_GR1)*(float(data_table[20][i])-Avg_Temp_15AboveBed_GR1)
            Covariance_Sum_InS_60A_GR1 += (float(data_table[19][i])-Avg_Temp_InSoil_GR1)*(float(data_table[21][i])-Avg_Temp_60AboveBed_GR1)
            Covariance_Sum_15A_60A_GR1 += (float(data_table[20][i])-Avg_Temp_15AboveBed_GR1)*(float(data_table[21][i])-Avg_Temp_60AboveBed_GR1)
    
        Variance_Temp_UnderBed_GR1 = Variance_Sum_Temp_UnderBed_GR1/S
        Variance_Temp_InSoil_GR1 = Variance_Sum_Temp_InSoil_GR1/S
        Variance_Temp_15AboveBed_GR1 = Variance_Sum_Temp_15AboveBed_GR1/S
        Variance_Temp_60AboveBed_GR1 = Variance_Sum_Temp_60AboveBed_GR1/S
        Covariance_Und_InS_GR1 = Covariance_Sum_Und_InS_GR1/S
        Covariance_Und_15A_GR1 = Covariance_Sum_Und_15A_GR1/S
        Covariance_Und_60A_GR1 = Covariance_Sum_Und_60A_GR1/S
        Covariance_InS_15A_GR1 = Covariance_Sum_InS_15A_GR1/S
        Covariance_InS_60A_GR1 = Covariance_Sum_InS_60A_GR1/S
        Covariance_15A_60A_GR1 = Covariance_Sum_15A_60A_GR1/S
        
        Correlation_Und_InS_GR1 = Covariance_Und_InS_GR1*100/(((Variance_Temp_UnderBed_GR1)**(1/2))*((Variance_Temp_InSoil_GR1)**(1/2)))
        Correlation_Und_15A_GR1 = Covariance_Und_15A_GR1*100/(((Variance_Temp_UnderBed_GR1)**(1/2))*((Variance_Temp_15AboveBed_GR1)**(1/2)))
        Correlation_Und_60A_GR1 = Covariance_Und_60A_GR1*100/(((Variance_Temp_UnderBed_GR1)**(1/2))*((Variance_Temp_60AboveBed_GR1)*(1/2)))
        Correlation_InS_15A_GR1 = Covariance_InS_15A_GR1*100/(((Variance_Temp_InSoil_GR1)**(1/2))*((Variance_Temp_15AboveBed_GR1)**(1/2)))
        Correlation_InS_60A_GR1 = Covariance_InS_60A_GR1*100/(((Variance_Temp_InSoil_GR1)**(1/2))*((Variance_Temp_60AboveBed_GR1)**(1/2)))
        Correlation_15A_60A_GR1 = Covariance_15A_60A_GR1*100/(((Variance_Temp_15AboveBed_GR1)**(1/2))*((Variance_Temp_60AboveBed_GR1)**(1/2)))
        
        print('In the bed GR1, \n the correlation between the temperature under the bed and in the soil is r=',round(Correlation_Und_InS_GR1,2),'% \n the correlation between the temperature under the bed and 15cm above it is r=',round(Correlation_Und_15A_GR1,2),'% \n the correlation between the temperature under the bed and 60cm above it is r=',round(Correlation_Und_60A_GR1,2),'% \n the correlation between the temperature in the soil and 15cm above the bed is r=',round(Correlation_InS_15A_GR1,2),'% \n the correlation between the temperature in the soil and 60cm above th bed is r=',round(Correlation_InS_60A_GR1,2),'% \n the correlation between the temperature 15cm above the bed and 60cm above it r=',round(Correlation_15A_60A_GR1,2),'%')
    
    
def correlation_btw_bed(data_table,n):

# !!!This funtion is not finished!!!
    
# First we name the Sum we are gonna use in the code to access the average (sum(data)/numb(data))
    
    Sum_Temp_UnderBed_GBR2 = 0
    Sum_Temp_InSoil_GBR2 = 0
    Sum_Temp_15AboveBed_GBR2 = 0
    Sum_Temp_60AboveBed_GBR2 = 0
    Sum_Temp_UnderBed_GBR1 = 0
    Sum_Temp_InSoil_GBR1 = 0
    Sum_Temp_15AboveBed_GBR1 = 0
    Sum_Temp_60AboveBed_GBR1 = 0
    Sum_Temp_UnderBed_GR2 = 0
    Sum_Temp_InSoil_GR2 = 0
    Sum_Temp_15AboveBed_GR2 = 0
    Sum_Temp_60AboveBed_GR2 = 0
    Sum_Temp_UnderBed_GR1 = 0
    Sum_Temp_InSoil_GR1 = 0
    Sum_Temp_15AboveBed_GR1 = 0
    Sum_Temp_60AboveBed_GR1 = 0
    S=0
 
# Then we sum up each data in each list to get the average of each list

    for i in range (1,len(data_table)-1):
            
            Sum_Temp_UnderBed_GBR2+=float(data_table[6][i])
            Sum_Temp_InSoil_GBR2+=float(data_table[7][i])
            Sum_Temp_15AboveBed_GBR2+=float(data_table[8][i])
            Sum_Temp_60AboveBed_GBR2+=float(data_table[9][i])
            
            Sum_Temp_UnderBed_GBR1+=float(data_table[10][i])
            Sum_Temp_InSoil_GBR1+=float(data_table[11][i])
            Sum_Temp_15AboveBed_GBR1+=float(data_table[12][i])
            Sum_Temp_60AboveBed_GBR1+=float(data_table[13][i])
            
            Sum_Temp_UnderBed_GR2+=float(data_table[14][i])
            Sum_Temp_InSoil_GR2+=float(data_table[15][i])
            Sum_Temp_15AboveBed_GR2+=float(data_table[16][i])
            Sum_Temp_60AboveBed_GR2+=float(data_table[17][i])
            
            Sum_Temp_UnderBed_GR1+=float(data_table[18][i])
            Sum_Temp_InSoil_GR1+=float(data_table[19][i])
            Sum_Temp_15AboveBed_GR1+=float(data_table[20][i])
            Sum_Temp_60AboveBed_GR1+=float(data_table[21][i])
            
            S+=1
    
#Then we calculate the average of each list :
    
    
    Avg_Temp_UnderBed_GBR2=Sum_Temp_UnderBed_GBR2/S
    Avg_Temp_InSoil_GBR2=Sum_Temp_InSoil_GBR2/S
    Avg_Temp_15AboveBed_GBR2=Sum_Temp_15AboveBed_GBR2/S
    Avg_Temp_60AboveBed_GBR2=Sum_Temp_60AboveBed_GBR2/S

    Avg_Temp_UnderBed_GBR1=Sum_Temp_UnderBed_GBR1/S
    Avg_Temp_InSoil_GBR1=Sum_Temp_15AboveBed_GBR1/S
    Avg_Temp_15AboveBed_GBR1=Sum_Temp_15AboveBed_GBR1/S
    Avg_Temp_60AboveBed_GBR1=Sum_Temp_60AboveBed_GBR1/S
    
    Avg_Temp_UnderBed_GR2=Sum_Temp_UnderBed_GR2/S
    Avg_Temp_InSoil_GR2=Sum_Temp_InSoil_GR2/S
    Avg_Temp_15AboveBed_GR2=Sum_Temp_15AboveBed_GR2/S
    Avg_Temp_60AboveBed_GR2=Sum_Temp_60AboveBed_GR2/S
    
    Avg_Temp_UnderBed_GR1=Sum_Temp_UnderBed_GR1/S
    Avg_Temp_InSoil_GR1=Sum_Temp_InSoil_GR1/S
    Avg_Temp_15AboveBed_GR1=Sum_Temp_15AboveBed_GR1/S
    Avg_Temp_60AboveBed_GR1=Sum_Temp_60AboveBed_GR1/S
    
#Then we calculate the variance and covariance of the list we are interested in 
    
    
    Variance_Sum_Temp_UnderBed_GBR2 = 0
    Variance_Sum_Temp_InSoil_GBR2 = 0
    Variance_Sum_Temp_15AboveBed_GBR2 = 0
    Variance_Sum_Temp_60AboveBed_GBR2 = 0
    Covariance_Sum_Und_InS_GBR2 = 0
    Covariance_Sum_Und_15A_GBR2 = 0
    Covariance_Sum_Und_60A_GBR2 = 0
    Covariance_Sum_InS_15A_GBR2 = 0
    Covariance_Sum_InS_60A_GBR2 = 0
    Covariance_Sum_15A_60A_GBR2 = 0
    
    Variance_Sum_Temp_UnderBed_GBR1 = 0
    Variance_Sum_Temp_InSoil_GBR1 = 0
    Variance_Sum_Temp_15AboveBed_GBR1 = 0
    Variance_Sum_Temp_60AboveBed_GBR1 = 0
    Covariance_Sum_Und_InS_GBR1 = 0
    Covariance_Sum_Und_15A_GBR1 = 0
    Covariance_Sum_Und_60A_GBR1 = 0
    Covariance_Sum_InS_15A_GBR1 = 0
    Covariance_Sum_InS_60A_GBR1 = 0
    Covariance_Sum_15A_60A_GBR1 = 0
    
    Variance_Sum_Temp_UnderBed_GR2 = 0
    Variance_Sum_Temp_InSoil_GR2 = 0
    Variance_Sum_Temp_15AboveBed_GR2 = 0
    Variance_Sum_Temp_60AboveBed_GR2 = 0
    Covariance_Sum_Und_InS_GR2 = 0
    Covariance_Sum_Und_15A_GR2 = 0
    Covariance_Sum_Und_60A_GR2 = 0
    Covariance_Sum_InS_15A_GR2 = 0
    Covariance_Sum_InS_60A_GR2 = 0
    Covariance_Sum_15A_60A_GR2 = 0
    
    Variance_Sum_Temp_UnderBed_GR1 = 0
    Variance_Sum_Temp_InSoil_GR1 = 0
    Variance_Sum_Temp_15AboveBed_GR1 = 0
    Variance_Sum_Temp_60AboveBed_GR1 = 0
    Covariance_Sum_Und_InS_GR1 = 0
    Covariance_Sum_Und_15A_GR1 = 0
    Covariance_Sum_Und_60A_GR1 = 0
    Covariance_Sum_InS_15A_GR1 = 0
    Covariance_Sum_InS_60A_GR1 = 0
    Covariance_Sum_15A_60A_GR1 = 0

    if n==2:
        for i in range (1,len(data_table)-1) :
            
            Variance_Sum_Temp_UnderBed_GBR2 += (float(data_table[6][i])-Avg_Temp_UnderBed_GBR2)**2
            Variance_Sum_Temp_InSoil_GBR2 += (float(data_table[7][i])-Avg_Temp_InSoil_GBR2)**2
            Variance_Sum_Temp_15AboveBed_GBR2 += (float(data_table[8][i])-Avg_Temp_15AboveBed_GBR2)**2
            Variance_Sum_Temp_60AboveBed_GBR2 += (float(data_table[9][i])-Avg_Temp_60AboveBed_GBR2)**2
            Covariance_Sum_Und_InS_GBR2 += (float(data_table[6][i])-Avg_Temp_UnderBed_GBR2)*(float(data_table[7][i])-Avg_Temp_InSoil_GBR2)
            Covariance_Sum_Und_15A_GBR2 += (float(data_table[6][i])-Avg_Temp_UnderBed_GBR2)*(float(data_table[8][i])-Avg_Temp_15AboveBed_GBR2)
            Covariance_Sum_Und_60A_GBR2 += (float(data_table[6][i])-Avg_Temp_UnderBed_GBR2)*(float(data_table[9][i])-Avg_Temp_60AboveBed_GBR2)
            Covariance_Sum_InS_15A_GBR2 += (float(data_table[7][i])-Avg_Temp_InSoil_GBR2)*(float(data_table[8][i])-Avg_Temp_15AboveBed_GBR2)
            Covariance_Sum_InS_60A_GBR2 += (float(data_table[7][i])-Avg_Temp_InSoil_GBR2)*(float(data_table[9][i])-Avg_Temp_60AboveBed_GBR2)
            Covariance_Sum_15A_60A_GBR2 += (float(data_table[8][i])-Avg_Temp_15AboveBed_GBR2)*(float(data_table[9][i])-Avg_Temp_60AboveBed_GBR2)
    
        Variance_Temp_UnderBed_GBR2 = Variance_Sum_Temp_UnderBed_GBR2/S
        Variance_Temp_InSoil_GBR2 = Variance_Sum_Temp_InSoil_GBR2/S
        Variance_Temp_15AboveBed_GBR2 = Variance_Sum_Temp_15AboveBed_GBR2/S
        Variance_Temp_60AboveBed_GBR2 = Variance_Sum_Temp_60AboveBed_GBR2/S
        Covariance_Und_InS_GBR2 = Covariance_Sum_Und_InS_GBR2/S
        Covariance_Und_15A_GBR2 = Covariance_Sum_Und_15A_GBR2/S
        Covariance_Und_60A_GBR2 = Covariance_Sum_Und_60A_GBR2/S
        Covariance_InS_15A_GBR2 = Covariance_Sum_InS_15A_GBR2/S
        Covariance_InS_60A_GBR2 = Covariance_Sum_InS_60A_GBR2/S
        Covariance_15A_60A_GBR2 = Covariance_Sum_15A_60A_GBR2/S
        
        Correlation_Und_InS_GBR2 = Covariance_Und_InS_GBR2*100/(((Variance_Temp_UnderBed_GBR2)**(1/2))*((Variance_Temp_InSoil_GBR2)**(1/2)))
        Correlation_Und_15A_GBR2 = Covariance_Und_15A_GBR2*100/(((Variance_Temp_UnderBed_GBR2)**(1/2))*((Variance_Temp_15AboveBed_GBR2)**(1/2)))
        Correlation_Und_60A_GBR2 = Covariance_Und_60A_GBR2*100/(((Variance_Temp_UnderBed_GBR2)**(1/2))*((Variance_Temp_60AboveBed_GBR2)*(1/2)))
        Correlation_InS_15A_GBR2 = Covariance_InS_15A_GBR2*100/(((Variance_Temp_InSoil_GBR2)**(1/2))*((Variance_Temp_15AboveBed_GBR2)**(1/2)))
        Correlation_InS_60A_GBR2 = Covariance_InS_60A_GBR2*100/(((Variance_Temp_InSoil_GBR2)**(1/2))*((Variance_Temp_60AboveBed_GBR2)**(1/2)))
        Correlation_15A_60A_GBR2 = Covariance_15A_60A_GBR2*100/(((Variance_Temp_15AboveBed_GBR2)**(1/2))*((Variance_Temp_60AboveBed_GBR2)**(1/2)))
        
        print('In the bed GBR2, \n the correlation between the temperature under the bed and in the soil is r=',round(Correlation_Und_InS_GBR2,2),'% \n the correlation between the temperature under the bed and 15cm above it is r=',round(Correlation_Und_15A_GBR2,2),'% \n the correlation between the temperature under the bed and 60cm above it is r=',round(Correlation_Und_60A_GBR2,2),'% \n the correlation between the temperature in the soil and 15cm above the bed is r=',round(Correlation_InS_15A_GBR2,2),'% \n the correlation between the temperature in the soil and 60cm above th bed is r=',round(Correlation_InS_60A_GBR2,2),'% \n the correlation between the temperature 15cm above the bed and 60cm above it r=',round(Correlation_15A_60A_GBR2,2),'%')
    
    if n==1:
        for i in range (1,len(data_table)-1) :
            
            Variance_Sum_Temp_UnderBed_GBR1 += (float(data_table[10][i])-Avg_Temp_UnderBed_GBR1)**2
            Variance_Sum_Temp_InSoil_GBR1 += (float(data_table[11][i])-Avg_Temp_InSoil_GBR1)**2
            Variance_Sum_Temp_15AboveBed_GBR1 += (float(data_table[12][i])-Avg_Temp_15AboveBed_GBR1)**2
            Variance_Sum_Temp_60AboveBed_GBR1 += (float(data_table[13][i])-Avg_Temp_60AboveBed_GBR1)**2
            Covariance_Sum_Und_InS_GBR1 += (float(data_table[10][i])-Avg_Temp_UnderBed_GBR1)*(float(data_table[11][i])-Avg_Temp_InSoil_GBR1)
            Covariance_Sum_Und_15A_GBR1 += (float(data_table[10][i])-Avg_Temp_UnderBed_GBR1)*(float(data_table[12][i])-Avg_Temp_15AboveBed_GBR1)
            Covariance_Sum_Und_60A_GBR1 += (float(data_table[10][i])-Avg_Temp_UnderBed_GBR1)*(float(data_table[13][i])-Avg_Temp_60AboveBed_GBR1)
            Covariance_Sum_InS_15A_GBR1 += (float(data_table[11][i])-Avg_Temp_InSoil_GBR1)*(float(data_table[12][i])-Avg_Temp_15AboveBed_GBR1)
            Covariance_Sum_InS_60A_GBR1 += (float(data_table[11][i])-Avg_Temp_InSoil_GBR1)*(float(data_table[13][i])-Avg_Temp_60AboveBed_GBR1)
            Covariance_Sum_15A_60A_GBR1 += (float(data_table[12][i])-Avg_Temp_15AboveBed_GBR1)*(float(data_table[13][i])-Avg_Temp_60AboveBed_GBR1)
         
        Variance_Temp_UnderBed_GBR1 = Variance_Sum_Temp_UnderBed_GBR1/S
        Variance_Temp_InSoil_GBR1 = Variance_Sum_Temp_InSoil_GBR1/S
        Variance_Temp_15AboveBed_GBR1 = Variance_Sum_Temp_15AboveBed_GBR1/S
        Variance_Temp_60AboveBed_GBR1 = Variance_Sum_Temp_60AboveBed_GBR1/S
        Covariance_Und_InS_GBR1 = Covariance_Sum_Und_InS_GBR1/S
        Covariance_Und_15A_GBR1 = Covariance_Sum_Und_15A_GBR1/S
        Covariance_Und_60A_GBR1 = Covariance_Sum_Und_60A_GBR1/S
        Covariance_InS_15A_GBR1 = Covariance_Sum_InS_15A_GBR1/S
        Covariance_InS_60A_GBR1 = Covariance_Sum_InS_60A_GBR1/S
        Covariance_15A_60A_GBR1 = Covariance_Sum_15A_60A_GBR1/S
        
        Correlation_Und_InS_GBR1 = Covariance_Und_InS_GBR1*100/(((Variance_Temp_UnderBed_GBR1)**(1/2))*((Variance_Temp_InSoil_GBR1)**(1/2)))
        Correlation_Und_15A_GBR1 = Covariance_Und_15A_GBR1*100/(((Variance_Temp_UnderBed_GBR1)**(1/2))*((Variance_Temp_15AboveBed_GBR1)**(1/2)))
        Correlation_Und_60A_GBR1 = Covariance_Und_60A_GBR1*100/(((Variance_Temp_UnderBed_GBR1)**(1/2))*((Variance_Temp_60AboveBed_GBR1)*(1/2)))
        Correlation_InS_15A_GBR1 = Covariance_InS_15A_GBR1*100/(((Variance_Temp_InSoil_GBR1)**(1/2))*((Variance_Temp_15AboveBed_GBR1)**(1/2)))
        Correlation_InS_60A_GBR1 = Covariance_InS_60A_GBR1*100/(((Variance_Temp_InSoil_GBR1)**(1/2))*((Variance_Temp_60AboveBed_GBR1)**(1/2)))
        Correlation_15A_60A_GBR1 = Covariance_15A_60A_GBR1*100/(((Variance_Temp_15AboveBed_GBR1)**(1/2))*((Variance_Temp_60AboveBed_GBR1)**(1/2)))
        
        print('In the bed GBR1, \n the correlation between the temperature under the bed and in the soil is r=',round(Correlation_Und_InS_GBR1,2),'% \n the correlation between the temperature under the bed and 15cm above it is r=',round(Correlation_Und_15A_GBR1,2),'% \n the correlation between the temperature under the bed and 60cm above it is r=',round(Correlation_Und_60A_GBR1,2),'% \n the correlation between the temperature in the soil and 15cm above the bed is r=',round(Correlation_InS_15A_GBR1,2),'% \n the correlation between the temperature in the soil and 60cm above th bed is r=',round(Correlation_InS_60A_GBR1,2),'% \n the correlation between the temperature 15cm above the bed and 60cm above it r=',round(Correlation_15A_60A_GBR1,2),'%')
        
    if n==4:
        for i in range (1,len(data_table)-1) :
            
            Variance_Sum_Temp_UnderBed_GR2 += (float(data_table[14][i])-Avg_Temp_UnderBed_GR2)**2
            Variance_Sum_Temp_InSoil_GR2 += (float(data_table[15][i])-Avg_Temp_InSoil_GR2)**2
            Variance_Sum_Temp_15AboveBed_GR2 += (float(data_table[16][i])-Avg_Temp_15AboveBed_GR2)**2
            Variance_Sum_Temp_60AboveBed_GR2 += (float(data_table[17][i])-Avg_Temp_60AboveBed_GR2)**2
            Covariance_Sum_Und_InS_GR2 += (float(data_table[14][i])-Avg_Temp_UnderBed_GR2)*(float(data_table[15][i])-Avg_Temp_InSoil_GR2)
            Covariance_Sum_Und_15A_GR2 += (float(data_table[14][i])-Avg_Temp_UnderBed_GR2)*(float(data_table[16][i])-Avg_Temp_15AboveBed_GR2)
            Covariance_Sum_Und_60A_GR2 += (float(data_table[14][i])-Avg_Temp_UnderBed_GR2)*(float(data_table[17][i])-Avg_Temp_60AboveBed_GR2)
            Covariance_Sum_InS_15A_GR2 += (float(data_table[15][i])-Avg_Temp_InSoil_GR2)*(float(data_table[16][i])-Avg_Temp_15AboveBed_GR2)
            Covariance_Sum_InS_60A_GR2 += (float(data_table[15][i])-Avg_Temp_InSoil_GR2)*(float(data_table[17][i])-Avg_Temp_60AboveBed_GR2)
            Covariance_Sum_15A_60A_GR2 += (float(data_table[16][i])-Avg_Temp_15AboveBed_GR2)*(float(data_table[17][i])-Avg_Temp_60AboveBed_GR2)
    
        Variance_Temp_UnderBed_GR2 = Variance_Sum_Temp_UnderBed_GR2/S
        Variance_Temp_InSoil_GR2 = Variance_Sum_Temp_InSoil_GR2/S
        Variance_Temp_15AboveBed_GR2 = Variance_Sum_Temp_15AboveBed_GR2/S
        Variance_Temp_60AboveBed_GR2 = Variance_Sum_Temp_60AboveBed_GR2/S
        Covariance_Und_InS_GR2 = Covariance_Sum_Und_InS_GR2/S
        Covariance_Und_15A_GR2 = Covariance_Sum_Und_15A_GR2/S
        Covariance_Und_60A_GR2 = Covariance_Sum_Und_60A_GR2/S
        Covariance_InS_15A_GR2 = Covariance_Sum_InS_15A_GR2/S
        Covariance_InS_60A_GR2 = Covariance_Sum_InS_60A_GR2/S
        Covariance_15A_60A_GR2 = Covariance_Sum_15A_60A_GR2/S
        
        Correlation_Und_InS_GR2 = Covariance_Und_InS_GR2*100/(((Variance_Temp_UnderBed_GR2)**(1/2))*((Variance_Temp_InSoil_GR2)**(1/2)))
        Correlation_Und_15A_GR2 = Covariance_Und_15A_GR2*100/(((Variance_Temp_UnderBed_GR2)**(1/2))*((Variance_Temp_15AboveBed_GR2)**(1/2)))
        Correlation_Und_60A_GR2 = Covariance_Und_60A_GR2*100/(((Variance_Temp_UnderBed_GR2)**(1/2))*((Variance_Temp_60AboveBed_GR2)*(1/2)))
        Correlation_InS_15A_GR2 = Covariance_InS_15A_GR2*100/(((Variance_Temp_InSoil_GR2)**(1/2))*((Variance_Temp_15AboveBed_GR2)**(1/2)))
        Correlation_InS_60A_GR2 = Covariance_InS_60A_GR2*100/(((Variance_Temp_InSoil_GR2)**(1/2))*((Variance_Temp_60AboveBed_GR2)**(1/2)))
        Correlation_15A_60A_GR2 = Covariance_15A_60A_GR2*100/(((Variance_Temp_15AboveBed_GR2)**(1/2))*((Variance_Temp_60AboveBed_GR2)**(1/2)))
        
        print('In the bed GR2, \n the correlation between the temperature under the bed and in the soil is r=',round(Correlation_Und_InS_GR2,2),'% \n the correlation between the temperature under the bed and 15cm above it is r=',round(Correlation_Und_15A_GR2,2),'% \n the correlation between the temperature under the bed and 60cm above it is r=',round(Correlation_Und_60A_GR2,2),'% \n the correlation between the temperature in the soil and 15cm above the bed is r=',round(Correlation_InS_15A_GR2,2),'% \n the correlation between the temperature in the soil and 60cm above th bed is r=',round(Correlation_InS_60A_GR2,2),'% \n the correlation between the temperature 15cm above the bed and 60cm above it r=',round(Correlation_15A_60A_GR2,2),'%')
        
    if n==3:
        for i in range (1,len(data_table)-1) :
            
            Variance_Sum_Temp_UnderBed_GR1 += (float(data_table[18][i])-Avg_Temp_UnderBed_GR1)**2
            Variance_Sum_Temp_InSoil_GR1 += (float(data_table[19][i])-Avg_Temp_InSoil_GR1)**2
            Variance_Sum_Temp_15AboveBed_GR1 += (float(data_table[20][i])-Avg_Temp_15AboveBed_GR1)**2
            Variance_Sum_Temp_60AboveBed_GR1 += (float(data_table[21][i])-Avg_Temp_60AboveBed_GR1)**2
            Covariance_Sum_Und_InS_GR1 += (float(data_table[18][i])-Avg_Temp_UnderBed_GR1)*(float(data_table[19][i])-Avg_Temp_InSoil_GR1)
            Covariance_Sum_Und_15A_GR1 += (float(data_table[18][i])-Avg_Temp_UnderBed_GR1)*(float(data_table[20][i])-Avg_Temp_15AboveBed_GR1)
            Covariance_Sum_Und_60A_GR1 += (float(data_table[18][i])-Avg_Temp_UnderBed_GR1)*(float(data_table[21][i])-Avg_Temp_60AboveBed_GR1)
            Covariance_Sum_InS_15A_GR1 += (float(data_table[19][i])-Avg_Temp_InSoil_GR1)*(float(data_table[20][i])-Avg_Temp_15AboveBed_GR1)
            Covariance_Sum_InS_60A_GR1 += (float(data_table[19][i])-Avg_Temp_InSoil_GR1)*(float(data_table[21][i])-Avg_Temp_60AboveBed_GR1)
            Covariance_Sum_15A_60A_GR1 += (float(data_table[20][i])-Avg_Temp_15AboveBed_GR1)*(float(data_table[21][i])-Avg_Temp_60AboveBed_GR1)
    
        Variance_Temp_UnderBed_GR1 = Variance_Sum_Temp_UnderBed_GR1/S
        Variance_Temp_InSoil_GR1 = Variance_Sum_Temp_InSoil_GR1/S
        Variance_Temp_15AboveBed_GR1 = Variance_Sum_Temp_15AboveBed_GR1/S
        Variance_Temp_60AboveBed_GR1 = Variance_Sum_Temp_60AboveBed_GR1/S
        Covariance_Und_InS_GR1 = Covariance_Sum_Und_InS_GR1/S
        Covariance_Und_15A_GR1 = Covariance_Sum_Und_15A_GR1/S
        Covariance_Und_60A_GR1 = Covariance_Sum_Und_60A_GR1/S
        Covariance_InS_15A_GR1 = Covariance_Sum_InS_15A_GR1/S
        Covariance_InS_60A_GR1 = Covariance_Sum_InS_60A_GR1/S
        Covariance_15A_60A_GR1 = Covariance_Sum_15A_60A_GR1/S
        
        Correlation_Und_InS_GR1 = Covariance_Und_InS_GR1*100/(((Variance_Temp_UnderBed_GR1)**(1/2))*((Variance_Temp_InSoil_GR1)**(1/2)))
        Correlation_Und_15A_GR1 = Covariance_Und_15A_GR1*100/(((Variance_Temp_UnderBed_GR1)**(1/2))*((Variance_Temp_15AboveBed_GR1)**(1/2)))
        Correlation_Und_60A_GR1 = Covariance_Und_60A_GR1*100/(((Variance_Temp_UnderBed_GR1)**(1/2))*((Variance_Temp_60AboveBed_GR1)*(1/2)))
        Correlation_InS_15A_GR1 = Covariance_InS_15A_GR1*100/(((Variance_Temp_InSoil_GR1)**(1/2))*((Variance_Temp_15AboveBed_GR1)**(1/2)))
        Correlation_InS_60A_GR1 = Covariance_InS_60A_GR1*100/(((Variance_Temp_InSoil_GR1)**(1/2))*((Variance_Temp_60AboveBed_GR1)**(1/2)))
        Correlation_15A_60A_GR1 = Covariance_15A_60A_GR1*100/(((Variance_Temp_15AboveBed_GR1)**(1/2))*((Variance_Temp_60AboveBed_GR1)**(1/2)))
        
        print('In the bed GR1, \n the correlation between the temperature under the bed and in the soil is r=',round(Correlation_Und_InS_GR1,2),'% \n the correlation between the temperature under the bed and 15cm above it is r=',round(Correlation_Und_15A_GR1,2),'% \n the correlation between the temperature under the bed and 60cm above it is r=',round(Correlation_Und_60A_GR1,2),'% \n the correlation between the temperature in the soil and 15cm above the bed is r=',round(Correlation_InS_15A_GR1,2),'% \n the correlation between the temperature in the soil and 60cm above th bed is r=',round(Correlation_InS_60A_GR1,2),'% \n the correlation between the temperature 15cm above the bed and 60cm above it r=',round(Correlation_15A_60A_GR1,2),'%')
    

# 5/ First manipulation of data
# 5/a) Average Data on a day

def avg_temp(data_table,a):      
    #Fisrt we name the different lists of data we want to visualize  
    
    Avg_Temp_CntrlRoof = []
    Avg_Temp_UnderBed_GBR2 = []
    Avg_Temp_InSoil_GBR2 = []
    Avg_Temp_15AboveBed_GBR2 = []
    Avg_Temp_60AboveBed_GBR2 = []
    Avg_Temp_UnderBed_GBR1 = []
    Avg_Temp_InSoil_GBR1 = []
    Avg_Temp_15AboveBed_GBR1 = []
    Avg_Temp_60AboveBed_GBR1 = []
    Avg_Temp_UnderBed_GR2 = []
    Avg_Temp_InSoil_GR2 = []
    Avg_Temp_15AboveBed_GR2 = []
    Avg_Temp_60AboveBed_GR2 = []
    Avg_Temp_UnderBed_GR1 = []
    Avg_Temp_InSoil_GR1 = []
    Avg_Temp_15AboveBed_GR1 = []
    Avg_Temp_60AboveBed_GR1 = []
    
    # And we name the table we are gonna use in the code to access the average (sum(data)/numb(data))
    Sum_Temp_CntrlRoof = np.zeros((24,12))
    Sum_Temp_UnderBed_GBR2 = np.zeros((24,12))
    Sum_Temp_InSoil_GBR2 = np.zeros((24,12))
    Sum_Temp_15AboveBed_GBR2 = np.zeros((24,12))
    Sum_Temp_60AboveBed_GBR2 = np.zeros((24,12))
    Sum_Temp_UnderBed_GBR1 = np.zeros((24,12))
    Sum_Temp_InSoil_GBR1 = np.zeros((24,12))
    Sum_Temp_15AboveBed_GBR1 = np.zeros((24,12))
    Sum_Temp_60AboveBed_GBR1 = np.zeros((24,12))
    Sum_Temp_UnderBed_GR2 = np.zeros((24,12))
    Sum_Temp_InSoil_GR2 = np.zeros((24,12))
    Sum_Temp_15AboveBed_GR2 = np.zeros((24,12))
    Sum_Temp_60AboveBed_GR2 = np.zeros((24,12))
    Sum_Temp_UnderBed_GR1 = np.zeros((24,12))
    Sum_Temp_InSoil_GR1 = np.zeros((24,12))
    Sum_Temp_15AboveBed_GR1 = np.zeros((24,12))
    Sum_Temp_60AboveBed_GR1 = np.zeros((24,12))
    S = np.zeros((24,12))
    
    # Then we create the time we use as x lign for our day average plot
    avg_time=[]      
    for i in range (0,24):
        for j in range (0,12):
            avg_time.append((datetime.datetime(2022,1,1,i,j*5)))
    
    # Then sum up the data considering the hour and minutes linked to each lign
    for i in range (1,len(data_table)-1):
        for n in range (0,24):
            if int(data_table[0][i][11:13])==n:
                for m in range (0,12):
                    if int(data_table[0][i][14:16])==(m*5):
                        
                        S[n][m]+=1
                          
                        Sum_Temp_CntrlRoof[n][m]+=float(data_table[5][i])
                        Sum_Temp_UnderBed_GBR2[n][m]+=(float(data_table[6][i]))
                        Sum_Temp_InSoil_GBR2[n][m]+=(float(data_table[7][i]))
                        Sum_Temp_15AboveBed_GBR2[n][m]+=(float(data_table[8][i]))
                        Sum_Temp_60AboveBed_GBR2[n][m]+=(float(data_table[9][i]))
                        Sum_Temp_UnderBed_GBR1[n][m]+=(float(data_table[10][i]))
                        Sum_Temp_InSoil_GBR1[n][m]+=(float(data_table[11][i]))
                        Sum_Temp_15AboveBed_GBR1[n][m]+=(float(data_table[12][i]))
                        Sum_Temp_60AboveBed_GBR1[n][m]+=(float(data_table[13][i]))
                        Sum_Temp_UnderBed_GR2[n][m]+=(float(data_table[14][i]))
                        Sum_Temp_InSoil_GR2[n][m]+=(float(data_table[15][i]))
                        Sum_Temp_15AboveBed_GR2[n][m]+=(float(data_table[16][i]))
                        Sum_Temp_60AboveBed_GR2[n][m]+=(float(data_table[17][i]))
                        Sum_Temp_UnderBed_GR1[n][m]+=(float(data_table[18][i]))
                        Sum_Temp_InSoil_GR1[n][m]+=(float(data_table[19][i]))
                        Sum_Temp_15AboveBed_GR1[n][m]+=(float(data_table[20][i]))
                        Sum_Temp_60AboveBed_GR1[n][m]+=(float(data_table[21][i]))
                    
    # Finaly we put them into the list that we will visualise in the plots
    for n in range (0,24):
        for m in range (0,12):
                Avg_Temp_CntrlRoof.append(Sum_Temp_CntrlRoof[n][m]/S[n][m])
                Avg_Temp_UnderBed_GBR2.append(Sum_Temp_UnderBed_GBR2[n][m]/S[n][m])
                Avg_Temp_InSoil_GBR2.append(Sum_Temp_InSoil_GBR2[n][m]/S[n][m])
                Avg_Temp_15AboveBed_GBR2.append(Sum_Temp_15AboveBed_GBR2[n][m]/S[n][m])
                Avg_Temp_60AboveBed_GBR2.append(Sum_Temp_60AboveBed_GBR2[n][m]/S[n][m])
                Avg_Temp_UnderBed_GBR1.append(Sum_Temp_UnderBed_GBR1[n][m]/S[n][m])
                Avg_Temp_InSoil_GBR1.append(Sum_Temp_15AboveBed_GBR1[n][m]/S[n][m])
                Avg_Temp_15AboveBed_GBR1.append(Sum_Temp_15AboveBed_GBR1[n][m]/S[n][m])
                Avg_Temp_60AboveBed_GBR1.append(Sum_Temp_60AboveBed_GBR1[n][m]/S[n][m])
                Avg_Temp_UnderBed_GR2.append(Sum_Temp_UnderBed_GR2[n][m]/S[n][m])
                Avg_Temp_InSoil_GR2.append(Sum_Temp_InSoil_GR2[n][m]/S[n][m])
                Avg_Temp_15AboveBed_GR2.append(Sum_Temp_15AboveBed_GR2[n][m]/S[n][m])
                Avg_Temp_60AboveBed_GR2.append(Sum_Temp_60AboveBed_GR2[n][m]/S[n][m])
                Avg_Temp_UnderBed_GR1.append(Sum_Temp_UnderBed_GR1[n][m]/S[n][m])
                Avg_Temp_InSoil_GR1.append(Sum_Temp_InSoil_GR1[n][m]/S[n][m])
                Avg_Temp_15AboveBed_GR1.append(Sum_Temp_15AboveBed_GR1[n][m]/S[n][m])
                Avg_Temp_60AboveBed_GR1.append(Sum_Temp_60AboveBed_GR1[n][m]/S[n][m])
                
    # And we visualise the plot 
    if a==1 :
        plt.plot_date(avg_time, Avg_Temp_60AboveBed_GBR1,"-", label = 'Average Temperature 60cm Above Bed_GBR1')
        plt.plot_date(avg_time, Avg_Temp_15AboveBed_GBR1,"-", label = 'Average Temperature 15cm Above Bed_GBR1')
        plt.plot_date(avg_time, Avg_Temp_InSoil_GBR1,"-", label = 'Average Temperature of Soil_GBR1')
        plt.plot_date(avg_time, Avg_Temp_UnderBed_GBR1,"-", label = 'Average Temperature under the bed_GBR1')
        plt.plot_date(avg_time, Avg_Temp_CntrlRoof,"-", label = 'Average Temperature of Control Roof')
        plt.legend()
        plt.title("Average Temperatures of the GRB1")
        plt.show()
        
    elif a==2 :
        plt.plot_date(avg_time, Avg_Temp_60AboveBed_GBR2,"-", label = 'Average Temperature 60cm Above Bed_GBR2')
        plt.plot_date(avg_time, Avg_Temp_15AboveBed_GBR2,"-", label = 'Average Temperature 15cm Above Bed_GBR2')
        plt.plot_date(avg_time, Avg_Temp_InSoil_GBR2,"-", label = 'Average Temperature of Soil_GBR2')
        plt.plot_date(avg_time, Avg_Temp_UnderBed_GBR2,"-", label = 'Average Temperature under the bed_GBR2')
        plt.plot_date(avg_time, Avg_Temp_CntrlRoof,"-", label = 'Average Temperature of Control Roof')
        plt.legend()
        plt.title("Average Temperatures of the GRB2")
        plt.show()
        
    elif a==3 :
        plt.plot_date(avg_time, Avg_Temp_60AboveBed_GR1,"-", label = 'Average Temperature 60cm Above Bed_GR1')
        plt.plot_date(avg_time, Avg_Temp_15AboveBed_GR1,"-", label = 'Average Temperature 15cm Above Bed_GR1')
        plt.plot_date(avg_time, Avg_Temp_InSoil_GR1,"-", label = 'Average Temperature of Soil_GR1')
        plt.plot_date(avg_time, Avg_Temp_UnderBed_GR1,"-", label = 'Average Temperature under the bed_GR1')
        plt.plot_date(avg_time, Avg_Temp_CntrlRoof,"-", label = 'Average Temperature of Control Roof')
        plt.legend()
        plt.title("Average Temperatures of the GR1")
        plt.show()
        
    elif a==4 :
        plt.plot_date(avg_time, Avg_Temp_60AboveBed_GR2,"-", label = 'Average Temperature 60cm Above Bed_GR2')
        plt.plot_date(avg_time, Avg_Temp_15AboveBed_GR2,"-", label = 'Avergae Temperature 15cm Above Bed_GR2')
        plt.plot_date(avg_time, Avg_Temp_InSoil_GR2,"-", label = 'Avergae Temperature of Soil_GR2')
        plt.plot_date(avg_time, Avg_Temp_UnderBed_GR2,"-", label = 'Average Temperature under the bed_GR2')
        plt.plot_date(avg_time, Avg_Temp_CntrlRoof,"-", label = 'AverageTemperature of Control Roof')
        plt.legend()
        plt.title("Average Temperatures of the GR2")
        plt.show()
    
    
# 5/b) Categorising data by temperature blocs (ex: [0:20],[20:25],[25:30],[30:35],+35 C°)

def max_temp_list(data_table) :
    Max_temp=[]
    j=6
    
    MaxT=0
    Time = temp_list(data_table)[0]
    Temp_CntrlRoof = temp_list(data_table)[1]
    
    for i in range (1, len(Temp_CntrlRoof)):
        
        if Time[i].day==j :
            if MaxT<Temp_CntrlRoof[i]:
                MaxT=Temp_CntrlRoof[i]
                
        elif Time[i].day!=j and j!=31 :
            j+=1
            Max_temp.append(MaxT)
            MaxT=0
            
        elif Time[i].day!=j and j==31 :
            j=1
           
            Max_temp.append(MaxT)
            MaxT=0
    Max_temp.append(MaxT)
    return (Max_temp)
        

def cat_list(data_table,a,c,T1,T2,T3) :
    
    Time = temp_list(data_table)[0]
    Temp_CntrlRoof = temp_list(data_table)[1]
    Temp_UnderBed_GBR2 = temp_list(data_table)[2]
    Temp_InSoil_GBR2 = temp_list(data_table)[3]
    Temp_15AboveBed_GBR2 = temp_list(data_table)[4]
    Temp_60AboveBed_GBR2 = temp_list(data_table)[5]
    Temp_UnderBed_GBR1 = temp_list(data_table)[6]
    Temp_InSoil_GBR1 = temp_list(data_table)[7]
    Temp_15AboveBed_GBR1 = temp_list(data_table)[8]
    Temp_60AboveBed_GBR1 = temp_list(data_table)[9]
    Temp_UnderBed_GR2 = temp_list(data_table)[10]
    Temp_InSoil_GR2 = temp_list(data_table)[11]
    Temp_15AboveBed_GR2 = temp_list(data_table)[12]
    Temp_60AboveBed_GR2 = temp_list(data_table)[13]
    Temp_UnderBed_GR1 = temp_list(data_table)[14]
    Temp_InSoil_GR1 = temp_list(data_table)[15]
    Temp_15AboveBed_GR1 = temp_list(data_table)[16]
    Temp_60AboveBed_GR1 = temp_list(data_table)[17]
    
    Max_temp=max_temp_list(data_table)
    
    
    #We create the lists were we gonna categorize our days
    
    Time_c1=[]
    Time_c2=[]
    Time_c3=[]
    Time_c4=[]

    
    inf_T1_Temp_CntrlRoof= []
    inf_T1_Temp_UnderBed_GBR2 = []
    inf_T1_Temp_InSoil_GBR2 = []
    inf_T1_Temp_15AboveBed_GBR2 = []
    inf_T1_Temp_60AboveBed_GBR2 = []
    inf_T1_Temp_UnderBed_GBR1 = []
    inf_T1_Temp_InSoil_GBR1 = []
    inf_T1_Temp_15AboveBed_GBR1 = []
    inf_T1_Temp_60AboveBed_GBR1 = []
    inf_T1_Temp_UnderBed_GR2 = []
    inf_T1_Temp_InSoil_GR2 = []
    inf_T1_Temp_15AboveBed_GR2 = []
    inf_T1_Temp_60AboveBed_GR2 = []
    inf_T1_Temp_UnderBed_GR1 = []
    inf_T1_Temp_InSoil_GR1 = []
    inf_T1_Temp_15AboveBed_GR1 = []
    inf_T1_Temp_60AboveBed_GR1 = []
    
    sup_T3_Temp_CntrlRoof= []
    sup_T3_Temp_UnderBed_GBR2 = []
    sup_T3_Temp_InSoil_GBR2 = []
    sup_T3_Temp_15AboveBed_GBR2 = []
    sup_T3_Temp_60AboveBed_GBR2 = []
    sup_T3_Temp_UnderBed_GBR1 = []
    sup_T3_Temp_InSoil_GBR1 = []
    sup_T3_Temp_15AboveBed_GBR1 = []
    sup_T3_Temp_60AboveBed_GBR1 = []
    sup_T3_Temp_UnderBed_GR2 = []
    sup_T3_Temp_InSoil_GR2 = []
    sup_T3_Temp_15AboveBed_GR2 = []
    sup_T3_Temp_60AboveBed_GR2 = []
    sup_T3_Temp_UnderBed_GR1 = []
    sup_T3_Temp_InSoil_GR1 = []
    sup_T3_Temp_15AboveBed_GR1 = []
    sup_T3_Temp_60AboveBed_GR1 = []
    
    btw_T1T2_Temp_CntrlRoof= []
    btw_T1T2_Temp_UnderBed_GBR2 = []
    btw_T1T2_Temp_InSoil_GBR2 = []
    btw_T1T2_Temp_15AboveBed_GBR2 = []
    btw_T1T2_Temp_60AboveBed_GBR2 = []
    btw_T1T2_Temp_UnderBed_GBR1 = []
    btw_T1T2_Temp_InSoil_GBR1 = []
    btw_T1T2_Temp_15AboveBed_GBR1 = []
    btw_T1T2_Temp_60AboveBed_GBR1 = []
    btw_T1T2_Temp_UnderBed_GR2 = []
    btw_T1T2_Temp_InSoil_GR2 = []
    btw_T1T2_Temp_15AboveBed_GR2 = []
    btw_T1T2_Temp_60AboveBed_GR2 = []
    btw_T1T2_Temp_UnderBed_GR1 = []
    btw_T1T2_Temp_InSoil_GR1 = []
    btw_T1T2_Temp_15AboveBed_GR1 = []
    btw_T1T2_Temp_60AboveBed_GR1 = []
    
    btw_T2T3_Temp_CntrlRoof= []
    btw_T2T3_Temp_UnderBed_GBR2 = []
    btw_T2T3_Temp_InSoil_GBR2 = []
    btw_T2T3_Temp_15AboveBed_GBR2 = []
    btw_T2T3_Temp_60AboveBed_GBR2 = []
    btw_T2T3_Temp_UnderBed_GBR1 = []
    btw_T2T3_Temp_InSoil_GBR1 = []
    btw_T2T3_Temp_15AboveBed_GBR1 = []
    btw_T2T3_Temp_60AboveBed_GBR1 = []
    btw_T2T3_Temp_UnderBed_GR2 = []
    btw_T2T3_Temp_InSoil_GR2 = []
    btw_T2T3_Temp_15AboveBed_GR2 = []
    btw_T2T3_Temp_60AboveBed_GR2 = []
    btw_T2T3_Temp_UnderBed_GR1 = []
    btw_T2T3_Temp_InSoil_GR1 = []
    btw_T2T3_Temp_15AboveBed_GR1 = []
    btw_T2T3_Temp_60AboveBed_GR1 = []
    
    k=0
    
#We create an absiss lign for our plot to show on

    avg_time=[]      
    for i in range (0,24):
        for j in range (0,12):
            avg_time.append((datetime.datetime(2022,1,1,i,j*5)))
    
    # We put the days in the right list 
    
    j=6
    
    for i in range (1, len(Temp_CntrlRoof)):
        
        if Time[i].day==j :
            
            if Max_temp[k]<T1 :
                
                Time_c1.append(Time[i])
                inf_T1_Temp_CntrlRoof.append(Temp_CntrlRoof[i])
                inf_T1_Temp_UnderBed_GBR2.append(Temp_UnderBed_GBR2[i])
                inf_T1_Temp_InSoil_GBR2.append(Temp_InSoil_GBR2[i])
                inf_T1_Temp_15AboveBed_GBR2.append(Temp_15AboveBed_GBR2[i])
                inf_T1_Temp_60AboveBed_GBR2.append(Temp_60AboveBed_GBR2[i])
                inf_T1_Temp_UnderBed_GBR1.append(Temp_UnderBed_GBR1[i])
                inf_T1_Temp_InSoil_GBR1.append(Temp_InSoil_GBR1[i])
                inf_T1_Temp_15AboveBed_GBR1.append(Temp_15AboveBed_GBR1[i])
                inf_T1_Temp_60AboveBed_GBR1.append(Temp_60AboveBed_GBR1[i])
                inf_T1_Temp_UnderBed_GR2.append(Temp_UnderBed_GR2[i])
                inf_T1_Temp_InSoil_GR2.append(Temp_InSoil_GR2[i])
                inf_T1_Temp_15AboveBed_GR2.append(Temp_15AboveBed_GR2[i])
                inf_T1_Temp_60AboveBed_GR2.append(Temp_60AboveBed_GR2[i])
                inf_T1_Temp_UnderBed_GR1.append(Temp_UnderBed_GR1[i])
                inf_T1_Temp_InSoil_GR1.append(Temp_InSoil_GR1[i])
                inf_T1_Temp_15AboveBed_GR1.append(Temp_15AboveBed_GR1[i])
                inf_T1_Temp_60AboveBed_GR1.append(Temp_60AboveBed_GR1[i])
            
            elif Max_temp[k]>=T1 and Max_temp[k]<T2 :
                
                Time_c2.append(Time[i])
                btw_T1T2_Temp_CntrlRoof.append(Temp_CntrlRoof[i])
                btw_T1T2_Temp_UnderBed_GBR2.append(Temp_UnderBed_GBR2[i])
                btw_T1T2_Temp_InSoil_GBR2.append(Temp_InSoil_GBR2[i])
                btw_T1T2_Temp_15AboveBed_GBR2.append(Temp_15AboveBed_GBR2[i])
                btw_T1T2_Temp_60AboveBed_GBR2.append(Temp_60AboveBed_GBR2[i])
                btw_T1T2_Temp_UnderBed_GBR1.append(Temp_UnderBed_GBR1[i])
                btw_T1T2_Temp_InSoil_GBR1.append(Temp_InSoil_GBR1[i])
                btw_T1T2_Temp_15AboveBed_GBR1.append(Temp_15AboveBed_GBR1[i])
                btw_T1T2_Temp_60AboveBed_GBR1.append(Temp_60AboveBed_GBR1[i])
                btw_T1T2_Temp_UnderBed_GR2.append(Temp_UnderBed_GR2[i])
                btw_T1T2_Temp_InSoil_GR2.append(Temp_InSoil_GR2[i])
                btw_T1T2_Temp_15AboveBed_GR2.append(Temp_15AboveBed_GR2[i])
                btw_T1T2_Temp_60AboveBed_GR2.append(Temp_60AboveBed_GR2[i])
                btw_T1T2_Temp_UnderBed_GR1.append(Temp_UnderBed_GR1[i])
                btw_T1T2_Temp_InSoil_GR1.append(Temp_InSoil_GR1[i])
                btw_T1T2_Temp_15AboveBed_GR1.append(Temp_15AboveBed_GR1[i])
                btw_T1T2_Temp_60AboveBed_GR1.append(Temp_60AboveBed_GR1[i])
                
            elif Max_temp[k]>=T2 and Max_temp[k]<T3 :
        
                Time_c3.append(Time[i])
                btw_T2T3_Temp_CntrlRoof.append(Temp_CntrlRoof[i])
                btw_T2T3_Temp_UnderBed_GBR2.append(Temp_UnderBed_GBR2[i])
                btw_T2T3_Temp_InSoil_GBR2.append(Temp_InSoil_GBR2[i])
                btw_T2T3_Temp_15AboveBed_GBR2.append(Temp_15AboveBed_GBR2[i])
                btw_T2T3_Temp_60AboveBed_GBR2.append(Temp_60AboveBed_GBR2[i])
                btw_T2T3_Temp_UnderBed_GBR1.append(Temp_UnderBed_GBR1[i])
                btw_T2T3_Temp_InSoil_GBR1.append(Temp_InSoil_GBR1[i])
                btw_T2T3_Temp_15AboveBed_GBR1.append(Temp_15AboveBed_GBR1[i])
                btw_T2T3_Temp_60AboveBed_GBR1.append(Temp_60AboveBed_GBR1[i])
                btw_T2T3_Temp_UnderBed_GR2.append(Temp_UnderBed_GR2[i])
                btw_T2T3_Temp_InSoil_GR2.append(Temp_InSoil_GR2[i])
                btw_T2T3_Temp_15AboveBed_GR2.append(Temp_15AboveBed_GR2[i])
                btw_T2T3_Temp_60AboveBed_GR2.append(Temp_60AboveBed_GR2[i])
                btw_T2T3_Temp_UnderBed_GR1.append(Temp_UnderBed_GR1[i])
                btw_T2T3_Temp_InSoil_GR1.append(Temp_InSoil_GR1[i])
                btw_T2T3_Temp_15AboveBed_GR1.append(Temp_15AboveBed_GR1[i])
                btw_T2T3_Temp_60AboveBed_GR1.append(Temp_60AboveBed_GR1[i])
    
            else :
                
                Time_c4.append(Time[i])
                sup_T3_Temp_CntrlRoof.append(Temp_CntrlRoof[i])
                sup_T3_Temp_UnderBed_GBR2.append(Temp_UnderBed_GBR2[i])
                sup_T3_Temp_InSoil_GBR2.append(Temp_InSoil_GBR2[i])
                sup_T3_Temp_15AboveBed_GBR2.append(Temp_15AboveBed_GBR2[i])
                sup_T3_Temp_60AboveBed_GBR2.append(Temp_60AboveBed_GBR2[i])
                sup_T3_Temp_UnderBed_GBR1.append(Temp_UnderBed_GBR1[i])
                sup_T3_Temp_InSoil_GBR1.append(Temp_InSoil_GBR1[i])
                sup_T3_Temp_15AboveBed_GBR1.append(Temp_15AboveBed_GBR1[i])
                sup_T3_Temp_60AboveBed_GBR1.append(Temp_60AboveBed_GBR1[i])
                sup_T3_Temp_UnderBed_GR2.append(Temp_UnderBed_GR2[i])
                sup_T3_Temp_InSoil_GR2.append(Temp_InSoil_GR2[i])
                sup_T3_Temp_15AboveBed_GR2.append(Temp_15AboveBed_GR2[i])
                sup_T3_Temp_60AboveBed_GR2.append(Temp_60AboveBed_GR2[i])
                sup_T3_Temp_UnderBed_GR1.append(Temp_UnderBed_GR1[i])
                sup_T3_Temp_InSoil_GR1.append(Temp_InSoil_GR1[i])
                sup_T3_Temp_15AboveBed_GR1.append(Temp_15AboveBed_GR1[i])
                sup_T3_Temp_60AboveBed_GR1.append(Temp_60AboveBed_GR1[i])
    
                
        elif Time[i].day !=j and j!=31 :
           
            j+=1
            k+=1
            
            if Max_temp[k]<T1 :
                
                Time_c1.append(Time[i])
                inf_T1_Temp_CntrlRoof.append(Temp_CntrlRoof[i])
                inf_T1_Temp_UnderBed_GBR2.append(Temp_UnderBed_GBR2[i])
                inf_T1_Temp_InSoil_GBR2.append(Temp_InSoil_GBR2[i])
                inf_T1_Temp_15AboveBed_GBR2.append(Temp_15AboveBed_GBR2[i])
                inf_T1_Temp_60AboveBed_GBR2.append(Temp_60AboveBed_GBR2[i])
                inf_T1_Temp_UnderBed_GBR1.append(Temp_UnderBed_GBR1[i])
                inf_T1_Temp_InSoil_GBR1.append(Temp_InSoil_GBR1[i])
                inf_T1_Temp_15AboveBed_GBR1.append(Temp_15AboveBed_GBR1[i])
                inf_T1_Temp_60AboveBed_GBR1.append(Temp_60AboveBed_GBR1[i])
                inf_T1_Temp_UnderBed_GR2.append(Temp_UnderBed_GR2[i])
                inf_T1_Temp_InSoil_GR2.append(Temp_InSoil_GR2[i])
                inf_T1_Temp_15AboveBed_GR2.append(Temp_15AboveBed_GR2[i])
                inf_T1_Temp_60AboveBed_GR2.append(Temp_60AboveBed_GR2[i])
                inf_T1_Temp_UnderBed_GR1.append(Temp_UnderBed_GR1[i])
                inf_T1_Temp_InSoil_GR1.append(Temp_InSoil_GR1[i])
                inf_T1_Temp_15AboveBed_GR1.append(Temp_15AboveBed_GR1[i])
                inf_T1_Temp_60AboveBed_GR1.append(Temp_60AboveBed_GR1[i])
            
            elif Max_temp[k]>=T1 and Max_temp[k]<T2 :
                
                Time_c2.append(Time[i])
                btw_T1T2_Temp_CntrlRoof.append(Temp_CntrlRoof[i])
                btw_T1T2_Temp_UnderBed_GBR2.append(Temp_UnderBed_GBR2[i])
                btw_T1T2_Temp_InSoil_GBR2.append(Temp_InSoil_GBR2[i])
                btw_T1T2_Temp_15AboveBed_GBR2.append(Temp_15AboveBed_GBR2[i])
                btw_T1T2_Temp_60AboveBed_GBR2.append(Temp_60AboveBed_GBR2[i])
                btw_T1T2_Temp_UnderBed_GBR1.append(Temp_UnderBed_GBR1[i])
                btw_T1T2_Temp_InSoil_GBR1.append(Temp_InSoil_GBR1[i])
                btw_T1T2_Temp_15AboveBed_GBR1.append(Temp_15AboveBed_GBR1[i])
                btw_T1T2_Temp_60AboveBed_GBR1.append(Temp_60AboveBed_GBR1[i])
                btw_T1T2_Temp_UnderBed_GR2.append(Temp_UnderBed_GR2[i])
                btw_T1T2_Temp_InSoil_GR2.append(Temp_InSoil_GR2[i])
                btw_T1T2_Temp_15AboveBed_GR2.append(Temp_15AboveBed_GR2[i])
                btw_T1T2_Temp_60AboveBed_GR2.append(Temp_60AboveBed_GR2[i])
                btw_T1T2_Temp_UnderBed_GR1.append(Temp_UnderBed_GR1[i])
                btw_T1T2_Temp_InSoil_GR1.append(Temp_InSoil_GR1[i])
                btw_T1T2_Temp_15AboveBed_GR1.append(Temp_15AboveBed_GR1[i])
                btw_T1T2_Temp_60AboveBed_GR1.append(Temp_60AboveBed_GR1[i])
                
            elif Max_temp[k]>=T2 and Max_temp[k]<T3 :
        
                Time_c3.append(Time[i])
                btw_T2T3_Temp_CntrlRoof.append(Temp_CntrlRoof[i])
                btw_T2T3_Temp_UnderBed_GBR2.append(Temp_UnderBed_GBR2[i])
                btw_T2T3_Temp_InSoil_GBR2.append(Temp_InSoil_GBR2[i])
                btw_T2T3_Temp_15AboveBed_GBR2.append(Temp_15AboveBed_GBR2[i])
                btw_T2T3_Temp_60AboveBed_GBR2.append(Temp_60AboveBed_GBR2[i])
                btw_T2T3_Temp_UnderBed_GBR1.append(Temp_UnderBed_GBR1[i])
                btw_T2T3_Temp_InSoil_GBR1.append(Temp_InSoil_GBR1[i])
                btw_T2T3_Temp_15AboveBed_GBR1.append(Temp_15AboveBed_GBR1[i])
                btw_T2T3_Temp_60AboveBed_GBR1.append(Temp_60AboveBed_GBR1[i])
                btw_T2T3_Temp_UnderBed_GR2.append(Temp_UnderBed_GR2[i])
                btw_T2T3_Temp_InSoil_GR2.append(Temp_InSoil_GR2[i])
                btw_T2T3_Temp_15AboveBed_GR2.append(Temp_15AboveBed_GR2[i])
                btw_T2T3_Temp_60AboveBed_GR2.append(Temp_60AboveBed_GR2[i])
                btw_T2T3_Temp_UnderBed_GR1.append(Temp_UnderBed_GR1[i])
                btw_T2T3_Temp_InSoil_GR1.append(Temp_InSoil_GR1[i])
                btw_T2T3_Temp_15AboveBed_GR1.append(Temp_15AboveBed_GR1[i])
                btw_T2T3_Temp_60AboveBed_GR1.append(Temp_60AboveBed_GR1[i])
    
            else :
                
                Time_c4.append(Time[i])
                sup_T3_Temp_CntrlRoof.append(Temp_CntrlRoof[i])
                sup_T3_Temp_UnderBed_GBR2.append(Temp_UnderBed_GBR2[i])
                sup_T3_Temp_InSoil_GBR2.append(Temp_InSoil_GBR2[i])
                sup_T3_Temp_15AboveBed_GBR2.append(Temp_15AboveBed_GBR2[i])
                sup_T3_Temp_60AboveBed_GBR2.append(Temp_60AboveBed_GBR2[i])
                sup_T3_Temp_UnderBed_GBR1.append(Temp_UnderBed_GBR1[i])
                sup_T3_Temp_InSoil_GBR1.append(Temp_InSoil_GBR1[i])
                sup_T3_Temp_15AboveBed_GBR1.append(Temp_15AboveBed_GBR1[i])
                sup_T3_Temp_60AboveBed_GBR1.append(Temp_60AboveBed_GBR1[i])
                sup_T3_Temp_UnderBed_GR2.append(Temp_UnderBed_GR2[i])
                sup_T3_Temp_InSoil_GR2.append(Temp_InSoil_GR2[i])
                sup_T3_Temp_15AboveBed_GR2.append(Temp_15AboveBed_GR2[i])
                sup_T3_Temp_60AboveBed_GR2.append(Temp_60AboveBed_GR2[i])
                sup_T3_Temp_UnderBed_GR1.append(Temp_UnderBed_GR1[i])
                sup_T3_Temp_InSoil_GR1.append(Temp_InSoil_GR1[i])
                sup_T3_Temp_15AboveBed_GR1.append(Temp_15AboveBed_GR1[i])
                sup_T3_Temp_60AboveBed_GR1.append(Temp_60AboveBed_GR1[i])
    
                
            
        elif Time[i].day!=j and j==31 :
            
            j=1
            k+=1
            
            if Max_temp[k]<T1 :
                
                Time_c1.append(Time[i])
                inf_T1_Temp_CntrlRoof.append(Temp_CntrlRoof[i])
                inf_T1_Temp_UnderBed_GBR2.append(Temp_UnderBed_GBR2[i])
                inf_T1_Temp_InSoil_GBR2.append(Temp_InSoil_GBR2[i])
                inf_T1_Temp_15AboveBed_GBR2.append(Temp_15AboveBed_GBR2[i])
                inf_T1_Temp_60AboveBed_GBR2.append(Temp_60AboveBed_GBR2[i])
                inf_T1_Temp_UnderBed_GBR1.append(Temp_UnderBed_GBR1[i])
                inf_T1_Temp_InSoil_GBR1.append(Temp_InSoil_GBR1[i])
                inf_T1_Temp_15AboveBed_GBR1.append(Temp_15AboveBed_GBR1[i])
                inf_T1_Temp_60AboveBed_GBR1.append(Temp_60AboveBed_GBR1[i])
                inf_T1_Temp_UnderBed_GR2.append(Temp_UnderBed_GR2[i])
                inf_T1_Temp_InSoil_GR2.append(Temp_InSoil_GR2[i])
                inf_T1_Temp_15AboveBed_GR2.append(Temp_15AboveBed_GR2[i])
                inf_T1_Temp_60AboveBed_GR2.append(Temp_60AboveBed_GR2[i])
                inf_T1_Temp_UnderBed_GR1.append(Temp_UnderBed_GR1[i])
                inf_T1_Temp_InSoil_GR1.append(Temp_InSoil_GR1[i])
                inf_T1_Temp_15AboveBed_GR1.append(Temp_15AboveBed_GR1[i])
                inf_T1_Temp_60AboveBed_GR1.append(Temp_60AboveBed_GR1[i])
            
            elif Max_temp[k]>=T1 and Max_temp[k]<T2 :
                
                Time_c2.append(Time[i])
                btw_T1T2_Temp_CntrlRoof.append(Temp_CntrlRoof[i])
                btw_T1T2_Temp_UnderBed_GBR2.append(Temp_UnderBed_GBR2[i])
                btw_T1T2_Temp_InSoil_GBR2.append(Temp_InSoil_GBR2[i])
                btw_T1T2_Temp_15AboveBed_GBR2.append(Temp_15AboveBed_GBR2[i])
                btw_T1T2_Temp_60AboveBed_GBR2.append(Temp_60AboveBed_GBR2[i])
                btw_T1T2_Temp_UnderBed_GBR1.append(Temp_UnderBed_GBR1[i])
                btw_T1T2_Temp_InSoil_GBR1.append(Temp_InSoil_GBR1[i])
                btw_T1T2_Temp_15AboveBed_GBR1.append(Temp_15AboveBed_GBR1[i])
                btw_T1T2_Temp_60AboveBed_GBR1.append(Temp_60AboveBed_GBR1[i])
                btw_T1T2_Temp_UnderBed_GR2.append(Temp_UnderBed_GR2[i])
                btw_T1T2_Temp_InSoil_GR2.append(Temp_InSoil_GR2[i])
                btw_T1T2_Temp_15AboveBed_GR2.append(Temp_15AboveBed_GR2[i])
                btw_T1T2_Temp_60AboveBed_GR2.append(Temp_60AboveBed_GR2[i])
                btw_T1T2_Temp_UnderBed_GR1.append(Temp_UnderBed_GR1[i])
                btw_T1T2_Temp_InSoil_GR1.append(Temp_InSoil_GR1[i])
                btw_T1T2_Temp_15AboveBed_GR1.append(Temp_15AboveBed_GR1[i])
                btw_T1T2_Temp_60AboveBed_GR1.append(Temp_60AboveBed_GR1[i])
                
            elif Max_temp[k]>=T2 and Max_temp[k]<T3 :
        
                Time_c3.append(Time[i])
                btw_T2T3_Temp_CntrlRoof.append(Temp_CntrlRoof[i])
                btw_T2T3_Temp_UnderBed_GBR2.append(Temp_UnderBed_GBR2[i])
                btw_T2T3_Temp_InSoil_GBR2.append(Temp_InSoil_GBR2[i])
                btw_T2T3_Temp_15AboveBed_GBR2.append(Temp_15AboveBed_GBR2[i])
                btw_T2T3_Temp_60AboveBed_GBR2.append(Temp_60AboveBed_GBR2[i])
                btw_T2T3_Temp_UnderBed_GBR1.append(Temp_UnderBed_GBR1[i])
                btw_T2T3_Temp_InSoil_GBR1.append(Temp_InSoil_GBR1[i])
                btw_T2T3_Temp_15AboveBed_GBR1.append(Temp_15AboveBed_GBR1[i])
                btw_T2T3_Temp_60AboveBed_GBR1.append(Temp_60AboveBed_GBR1[i])
                btw_T2T3_Temp_UnderBed_GR2.append(Temp_UnderBed_GR2[i])
                btw_T2T3_Temp_InSoil_GR2.append(Temp_InSoil_GR2[i])
                btw_T2T3_Temp_15AboveBed_GR2.append(Temp_15AboveBed_GR2[i])
                btw_T2T3_Temp_60AboveBed_GR2.append(Temp_60AboveBed_GR2[i])
                btw_T2T3_Temp_UnderBed_GR1.append(Temp_UnderBed_GR1[i])
                btw_T2T3_Temp_InSoil_GR1.append(Temp_InSoil_GR1[i])
                btw_T2T3_Temp_15AboveBed_GR1.append(Temp_15AboveBed_GR1[i])
                btw_T2T3_Temp_60AboveBed_GR1.append(Temp_60AboveBed_GR1[i])
    
            else :
                
                Time_c4.append(Time[i])
                sup_T3_Temp_CntrlRoof.append(Temp_CntrlRoof[i])
                sup_T3_Temp_UnderBed_GBR2.append(Temp_UnderBed_GBR2[i])
                sup_T3_Temp_InSoil_GBR2.append(Temp_InSoil_GBR2[i])
                sup_T3_Temp_15AboveBed_GBR2.append(Temp_15AboveBed_GBR2[i])
                sup_T3_Temp_60AboveBed_GBR2.append(Temp_60AboveBed_GBR2[i])
                sup_T3_Temp_UnderBed_GBR1.append(Temp_UnderBed_GBR1[i])
                sup_T3_Temp_InSoil_GBR1.append(Temp_InSoil_GBR1[i])
                sup_T3_Temp_15AboveBed_GBR1.append(Temp_15AboveBed_GBR1[i])
                sup_T3_Temp_60AboveBed_GBR1.append(Temp_60AboveBed_GBR1[i])
                sup_T3_Temp_UnderBed_GR2.append(Temp_UnderBed_GR2[i])
                sup_T3_Temp_InSoil_GR2.append(Temp_InSoil_GR2[i])
                sup_T3_Temp_15AboveBed_GR2.append(Temp_15AboveBed_GR2[i])
                sup_T3_Temp_60AboveBed_GR2.append(Temp_60AboveBed_GR2[i])
                sup_T3_Temp_UnderBed_GR1.append(Temp_UnderBed_GR1[i])
                sup_T3_Temp_InSoil_GR1.append(Temp_InSoil_GR1[i])
                sup_T3_Temp_15AboveBed_GR1.append(Temp_15AboveBed_GR1[i])
                sup_T3_Temp_60AboveBed_GR1.append(Temp_60AboveBed_GR1[i])
    
    # And we name the table we are gonna use in the code to access the average (sum(data)/numb(data))
    Avg_Temp_CntrlRoof = []
    Avg_Temp_UnderBed_GBR2 = []
    Avg_Temp_InSoil_GBR2 = []
    Avg_Temp_15AboveBed_GBR2 = []
    Avg_Temp_60AboveBed_GBR2 = []
    Avg_Temp_UnderBed_GBR1 = []
    Avg_Temp_InSoil_GBR1 = []
    Avg_Temp_15AboveBed_GBR1 = []
    Avg_Temp_60AboveBed_GBR1 = []
    Avg_Temp_UnderBed_GR2 = []
    Avg_Temp_InSoil_GR2 = []
    Avg_Temp_15AboveBed_GR2 = []
    Avg_Temp_60AboveBed_GR2 = []
    Avg_Temp_UnderBed_GR1 = []
    Avg_Temp_InSoil_GR1 = []
    Avg_Temp_15AboveBed_GR1 = []
    Avg_Temp_60AboveBed_GR1 = []
    
    Sum_Temp_CntrlRoof = np.zeros((24,12))
    Sum_Temp_UnderBed_GBR2 = np.zeros((24,12))
    Sum_Temp_InSoil_GBR2 = np.zeros((24,12))
    Sum_Temp_15AboveBed_GBR2 = np.zeros((24,12))
    Sum_Temp_60AboveBed_GBR2 = np.zeros((24,12))
    Sum_Temp_UnderBed_GBR1 = np.zeros((24,12))
    Sum_Temp_InSoil_GBR1 = np.zeros((24,12))
    Sum_Temp_15AboveBed_GBR1 = np.zeros((24,12))
    Sum_Temp_60AboveBed_GBR1 = np.zeros((24,12))
    Sum_Temp_UnderBed_GR2 = np.zeros((24,12))
    Sum_Temp_InSoil_GR2 = np.zeros((24,12))
    Sum_Temp_15AboveBed_GR2 = np.zeros((24,12))
    Sum_Temp_60AboveBed_GR2 = np.zeros((24,12))
    Sum_Temp_UnderBed_GR1 = np.zeros((24,12))
    Sum_Temp_InSoil_GR1 = np.zeros((24,12))
    Sum_Temp_15AboveBed_GR1 = np.zeros((24,12))
    Sum_Temp_60AboveBed_GR1 = np.zeros((24,12))
    S = np.zeros((24,12))
            
    if c==1 :
        for i in range (1,len(inf_T1_Temp_CntrlRoof)-1):
            for n in range (0,24):
                if Time_c1[i].hour==n:
                    for m in range (0,12):
                        if Time_c1[i].minute==(m*5):
                        
                            S[n][m]+=1
                          
                            Sum_Temp_CntrlRoof[n][m]+=inf_T1_Temp_CntrlRoof[i]
                            Sum_Temp_UnderBed_GBR2[n][m]+=inf_T1_Temp_UnderBed_GBR2[i]
                            Sum_Temp_InSoil_GBR2[n][m]+=inf_T1_Temp_InSoil_GBR2[i]
                            Sum_Temp_15AboveBed_GBR2[n][m]+=inf_T1_Temp_15AboveBed_GBR2[i]
                            Sum_Temp_60AboveBed_GBR2[n][m]+=inf_T1_Temp_60AboveBed_GBR2[i]
                            Sum_Temp_UnderBed_GBR1[n][m]+=inf_T1_Temp_UnderBed_GBR1[i]
                            Sum_Temp_InSoil_GBR1[n][m]+=inf_T1_Temp_InSoil_GBR1[i]
                            Sum_Temp_15AboveBed_GBR1[n][m]+=inf_T1_Temp_15AboveBed_GBR1[i]
                            Sum_Temp_60AboveBed_GBR1[n][m]+=inf_T1_Temp_60AboveBed_GBR1[i]
                            Sum_Temp_UnderBed_GR2[n][m]+=inf_T1_Temp_UnderBed_GR2[i]
                            Sum_Temp_InSoil_GR2[n][m]+=inf_T1_Temp_InSoil_GR2[i]
                            Sum_Temp_15AboveBed_GR2[n][m]+=inf_T1_Temp_15AboveBed_GR2[i]
                            Sum_Temp_60AboveBed_GR2[n][m]+=inf_T1_Temp_60AboveBed_GR2[i]
                            Sum_Temp_UnderBed_GR1[n][m]+=inf_T1_Temp_UnderBed_GR1[i]
                            Sum_Temp_InSoil_GR1[n][m]+=inf_T1_Temp_InSoil_GR1[i]
                            Sum_Temp_15AboveBed_GR1[n][m]+=inf_T1_Temp_15AboveBed_GR1[i]
                            Sum_Temp_60AboveBed_GR1[n][m]+=inf_T1_Temp_60AboveBed_GR1[i]
                    
    # Finaly we put them into the list that we will visualise in the plots
        for n in range (0,24):
            for m in range (0,12):
                    Avg_Temp_CntrlRoof.append(Sum_Temp_CntrlRoof[n][m]/S[n][m])
                    Avg_Temp_UnderBed_GBR2.append(Sum_Temp_UnderBed_GBR2[n][m]/S[n][m])
                    Avg_Temp_InSoil_GBR2.append(Sum_Temp_InSoil_GBR2[n][m]/S[n][m])
                    Avg_Temp_15AboveBed_GBR2.append(Sum_Temp_15AboveBed_GBR2[n][m]/S[n][m])
                    Avg_Temp_60AboveBed_GBR2.append(Sum_Temp_60AboveBed_GBR2[n][m]/S[n][m])
                    Avg_Temp_UnderBed_GBR1.append(Sum_Temp_UnderBed_GBR1[n][m]/S[n][m])
                    Avg_Temp_InSoil_GBR1.append(Sum_Temp_15AboveBed_GBR1[n][m]/S[n][m])
                    Avg_Temp_15AboveBed_GBR1.append(Sum_Temp_15AboveBed_GBR1[n][m]/S[n][m])
                    Avg_Temp_60AboveBed_GBR1.append(Sum_Temp_60AboveBed_GBR1[n][m]/S[n][m])
                    Avg_Temp_UnderBed_GR2.append(Sum_Temp_UnderBed_GR2[n][m]/S[n][m])
                    Avg_Temp_InSoil_GR2.append(Sum_Temp_InSoil_GR2[n][m]/S[n][m])
                    Avg_Temp_15AboveBed_GR2.append(Sum_Temp_15AboveBed_GR2[n][m]/S[n][m])
                    Avg_Temp_60AboveBed_GR2.append(Sum_Temp_60AboveBed_GR2[n][m]/S[n][m])
                    Avg_Temp_UnderBed_GR1.append(Sum_Temp_UnderBed_GR1[n][m]/S[n][m])
                    Avg_Temp_InSoil_GR1.append(Sum_Temp_InSoil_GR1[n][m]/S[n][m])
                    Avg_Temp_15AboveBed_GR1.append(Sum_Temp_15AboveBed_GR1[n][m]/S[n][m])
                    Avg_Temp_60AboveBed_GR1.append(Sum_Temp_60AboveBed_GR1[n][m]/S[n][m])
                
    # And we visualise the plot 
        if a==1 :
            plt.plot_date(avg_time, Avg_Temp_60AboveBed_GBR1,"-", label = 'Average Temperature 60cm Above Bed_GBR1')
            plt.plot_date(avg_time, Avg_Temp_15AboveBed_GBR1,"-", label = 'Average Temperature 15cm Above Bed_GBR1')
            plt.plot_date(avg_time, Avg_Temp_InSoil_GBR1,"-", label = 'Average Temperature of Soil_GBR1')
            plt.plot_date(avg_time, Avg_Temp_UnderBed_GBR1,"-", label = 'Average Temperature under the bed_GBR1')
            plt.plot_date(avg_time, Avg_Temp_CntrlRoof,"-", label = 'Average Temperature of Control Roof')
            plt.legend()
            plt.title("Average Temperatures of the GRB1")
            plt.show()
            
        elif a==2 :
            plt.plot_date(avg_time, Avg_Temp_60AboveBed_GBR2,"-", label = 'Average Temperature 60cm Above Bed_GBR2')
            plt.plot_date(avg_time, Avg_Temp_15AboveBed_GBR2,"-", label = 'Average Temperature 15cm Above Bed_GBR2')
            plt.plot_date(avg_time, Avg_Temp_InSoil_GBR2,"-", label = 'Average Temperature of Soil_GBR2')
            plt.plot_date(avg_time, Avg_Temp_UnderBed_GBR2,"-", label = 'Average Temperature under the bed_GBR2')
            plt.plot_date(avg_time, Avg_Temp_CntrlRoof,"-", label = 'Average Temperature of Control Roof')
            plt.legend()
            plt.title("Average Temperatures of the GRB2")
            plt.show()
             
        elif a==3 :
            plt.plot_date(avg_time, Avg_Temp_60AboveBed_GR1,"-", label = 'Average Temperature 60cm Above Bed_GR1')
            plt.plot_date(avg_time, Avg_Temp_15AboveBed_GR1,"-", label = 'Average Temperature 15cm Above Bed_GR1')
            plt.plot_date(avg_time, Avg_Temp_InSoil_GR1,"-", label = 'Average Temperature of Soil_GR1')
            plt.plot_date(avg_time, Avg_Temp_UnderBed_GR1,"-", label = 'Average Temperature under the bed_GR1')
            plt.plot_date(avg_time, Avg_Temp_CntrlRoof,"-", label = 'Average Temperature of Control Roof')
            plt.legend()
            plt.title("Average Temperatures of the GR1")
            plt.show()
            
        elif a==4 :
            plt.plot_date(avg_time, Avg_Temp_60AboveBed_GR2,"-", label = 'Average Temperature 60cm Above Bed_GR2')
            plt.plot_date(avg_time, Avg_Temp_15AboveBed_GR2,"-", label = 'Avergae Temperature 15cm Above Bed_GR2')
            plt.plot_date(avg_time, Avg_Temp_InSoil_GR2,"-", label = 'Avergae Temperature of Soil_GR2')
            plt.plot_date(avg_time, Avg_Temp_UnderBed_GR2,"-", label = 'Average Temperature under the bed_GR2')
            plt.plot_date(avg_time, Avg_Temp_CntrlRoof,"-", label = 'AverageTemperature of Control Roof')
            plt.legend()
            plt.title("Average Temperatures of the GR2")
            plt.show()
    
    elif c==2 :
        for i in range (1,len(btw_T1T2_Temp_CntrlRoof)-1):
            for n in range (0,24):
                if Time_c2[i].hour==n:
                    for m in range (0,12):
                        if Time_c2[i].minute==(m*5):
                        
                            S[n][m]+=1
                          
                            Sum_Temp_CntrlRoof[n][m]+=btw_T1T2_Temp_CntrlRoof[i]
                            Sum_Temp_UnderBed_GBR2[n][m]+=btw_T1T2_Temp_UnderBed_GBR2[i]
                            Sum_Temp_InSoil_GBR2[n][m]+=btw_T1T2_Temp_InSoil_GBR2[i]
                            Sum_Temp_15AboveBed_GBR2[n][m]+=btw_T1T2_Temp_15AboveBed_GBR2[i]
                            Sum_Temp_60AboveBed_GBR2[n][m]+=btw_T1T2_Temp_60AboveBed_GBR2[i]
                            Sum_Temp_UnderBed_GBR1[n][m]+=btw_T1T2_Temp_UnderBed_GBR1[i]
                            Sum_Temp_InSoil_GBR1[n][m]+=btw_T1T2_Temp_InSoil_GBR1[i]
                            Sum_Temp_15AboveBed_GBR1[n][m]+=btw_T1T2_Temp_15AboveBed_GBR1[i]
                            Sum_Temp_60AboveBed_GBR1[n][m]+=btw_T1T2_Temp_60AboveBed_GBR1[i]
                            Sum_Temp_UnderBed_GR2[n][m]+=btw_T1T2_Temp_UnderBed_GR2[i]
                            Sum_Temp_InSoil_GR2[n][m]+=btw_T1T2_Temp_InSoil_GR2[i]
                            Sum_Temp_15AboveBed_GR2[n][m]+=btw_T1T2_Temp_15AboveBed_GR2[i]
                            Sum_Temp_60AboveBed_GR2[n][m]+=btw_T1T2_Temp_60AboveBed_GR2[i]
                            Sum_Temp_UnderBed_GR1[n][m]+=btw_T1T2_Temp_UnderBed_GR1[i]
                            Sum_Temp_InSoil_GR1[n][m]+=btw_T1T2_Temp_InSoil_GR1[i]
                            Sum_Temp_15AboveBed_GR1[n][m]+=btw_T1T2_Temp_15AboveBed_GR1[i]
                            Sum_Temp_60AboveBed_GR1[n][m]+=btw_T1T2_Temp_60AboveBed_GR1[i]
                    
    # Finaly we put them into the list that we will visualise in the plots
        for n in range (0,24):
            for m in range (0,12):
                    Avg_Temp_CntrlRoof.append(Sum_Temp_CntrlRoof[n][m]/S[n][m])
                    Avg_Temp_UnderBed_GBR2.append(Sum_Temp_UnderBed_GBR2[n][m]/S[n][m])
                    Avg_Temp_InSoil_GBR2.append(Sum_Temp_InSoil_GBR2[n][m]/S[n][m])
                    Avg_Temp_15AboveBed_GBR2.append(Sum_Temp_15AboveBed_GBR2[n][m]/S[n][m])
                    Avg_Temp_60AboveBed_GBR2.append(Sum_Temp_60AboveBed_GBR2[n][m]/S[n][m])
                    Avg_Temp_UnderBed_GBR1.append(Sum_Temp_UnderBed_GBR1[n][m]/S[n][m])
                    Avg_Temp_InSoil_GBR1.append(Sum_Temp_15AboveBed_GBR1[n][m]/S[n][m])
                    Avg_Temp_15AboveBed_GBR1.append(Sum_Temp_15AboveBed_GBR1[n][m]/S[n][m])
                    Avg_Temp_60AboveBed_GBR1.append(Sum_Temp_60AboveBed_GBR1[n][m]/S[n][m])
                    Avg_Temp_UnderBed_GR2.append(Sum_Temp_UnderBed_GR2[n][m]/S[n][m])
                    Avg_Temp_InSoil_GR2.append(Sum_Temp_InSoil_GR2[n][m]/S[n][m])
                    Avg_Temp_15AboveBed_GR2.append(Sum_Temp_15AboveBed_GR2[n][m]/S[n][m])
                    Avg_Temp_60AboveBed_GR2.append(Sum_Temp_60AboveBed_GR2[n][m]/S[n][m])
                    Avg_Temp_UnderBed_GR1.append(Sum_Temp_UnderBed_GR1[n][m]/S[n][m])
                    Avg_Temp_InSoil_GR1.append(Sum_Temp_InSoil_GR1[n][m]/S[n][m])
                    Avg_Temp_15AboveBed_GR1.append(Sum_Temp_15AboveBed_GR1[n][m]/S[n][m])
                    Avg_Temp_60AboveBed_GR1.append(Sum_Temp_60AboveBed_GR1[n][m]/S[n][m])
                
    # And we visualise the plot 
        if a==1 :
            plt.plot_date(avg_time, Avg_Temp_60AboveBed_GBR1,"-", label = 'Average Temperature 60cm Above Bed_GBR1')
            plt.plot_date(avg_time, Avg_Temp_15AboveBed_GBR1,"-", label = 'Average Temperature 15cm Above Bed_GBR1')
            plt.plot_date(avg_time, Avg_Temp_InSoil_GBR1,"-", label = 'Average Temperature of Soil_GBR1')
            plt.plot_date(avg_time, Avg_Temp_UnderBed_GBR1,"-", label = 'Average Temperature under the bed_GBR1')
            plt.plot_date(avg_time, Avg_Temp_CntrlRoof,"-", label = 'Average Temperature of Control Roof')
            plt.legend()
            plt.title("Average Temperatures of the GRB1")
            plt.show()
            
        elif a==2 :
            plt.plot_date(avg_time, Avg_Temp_60AboveBed_GBR2,"-", label = 'Average Temperature 60cm Above Bed_GBR2')
            plt.plot_date(avg_time, Avg_Temp_15AboveBed_GBR2,"-", label = 'Average Temperature 15cm Above Bed_GBR2')
            plt.plot_date(avg_time, Avg_Temp_InSoil_GBR2,"-", label = 'Average Temperature of Soil_GBR2')
            plt.plot_date(avg_time, Avg_Temp_UnderBed_GBR2,"-", label = 'Average Temperature under the bed_GBR2')
            plt.plot_date(avg_time, Avg_Temp_CntrlRoof,"-", label = 'Average Temperature of Control Roof')
            plt.legend()
            plt.title("Average Temperatures of the GRB2")
            plt.show()
             
        elif a==3 :
            plt.plot_date(avg_time, Avg_Temp_60AboveBed_GR1,"-", label = 'Average Temperature 60cm Above Bed_GR1')
            plt.plot_date(avg_time, Avg_Temp_15AboveBed_GR1,"-", label = 'Average Temperature 15cm Above Bed_GR1')
            plt.plot_date(avg_time, Avg_Temp_InSoil_GR1,"-", label = 'Average Temperature of Soil_GR1')
            plt.plot_date(avg_time, Avg_Temp_UnderBed_GR1,"-", label = 'Average Temperature under the bed_GR1')
            plt.plot_date(avg_time, Avg_Temp_CntrlRoof,"-", label = 'Average Temperature of Control Roof')
            plt.legend()
            plt.title("Average Temperatures of the GR1")
            plt.show()
            
        elif a==4 :
            plt.plot_date(avg_time, Avg_Temp_60AboveBed_GR2,"-", label = 'Average Temperature 60cm Above Bed_GR2')
            plt.plot_date(avg_time, Avg_Temp_15AboveBed_GR2,"-", label = 'Avergae Temperature 15cm Above Bed_GR2')
            plt.plot_date(avg_time, Avg_Temp_InSoil_GR2,"-", label = 'Avergae Temperature of Soil_GR2')
            plt.plot_date(avg_time, Avg_Temp_UnderBed_GR2,"-", label = 'Average Temperature under the bed_GR2')
            plt.plot_date(avg_time, Avg_Temp_CntrlRoof,"-", label = 'AverageTemperature of Control Roof')
            plt.legend()
            plt.title("Average Temperatures of the GR2")
            plt.show()
    
    
    elif c==3 :
        for i in range (1,len(btw_T2T3_Temp_CntrlRoof)-1):
            for n in range (0,24):
                if Time_c3[i].hour==n:
                    for m in range (0,12):
                        if Time_c3[i].minute==(m*5):
                        
                            S[n][m]+=1
                          
                            Sum_Temp_CntrlRoof[n][m]+=btw_T2T3_Temp_CntrlRoof[i]
                            Sum_Temp_UnderBed_GBR2[n][m]+=btw_T2T3_Temp_UnderBed_GBR2[i]
                            Sum_Temp_InSoil_GBR2[n][m]+=btw_T2T3_Temp_InSoil_GBR2[i]
                            Sum_Temp_15AboveBed_GBR2[n][m]+=btw_T2T3_Temp_15AboveBed_GBR2[i]
                            Sum_Temp_60AboveBed_GBR2[n][m]+=btw_T2T3_Temp_60AboveBed_GBR2[i]
                            Sum_Temp_UnderBed_GBR1[n][m]+=btw_T2T3_Temp_UnderBed_GBR1[i]
                            Sum_Temp_InSoil_GBR1[n][m]+=btw_T2T3_Temp_InSoil_GBR1[i]
                            Sum_Temp_15AboveBed_GBR1[n][m]+=btw_T2T3_Temp_15AboveBed_GBR1[i]
                            Sum_Temp_60AboveBed_GBR1[n][m]+=btw_T2T3_Temp_60AboveBed_GBR1[i]
                            Sum_Temp_UnderBed_GR2[n][m]+=btw_T2T3_Temp_UnderBed_GR2[i]
                            Sum_Temp_InSoil_GR2[n][m]+=btw_T2T3_Temp_InSoil_GR2[i]
                            Sum_Temp_15AboveBed_GR2[n][m]+=btw_T2T3_Temp_15AboveBed_GR2[i]
                            Sum_Temp_60AboveBed_GR2[n][m]+=btw_T2T3_Temp_60AboveBed_GR2[i]
                            Sum_Temp_UnderBed_GR1[n][m]+=btw_T2T3_Temp_UnderBed_GR1[i]
                            Sum_Temp_InSoil_GR1[n][m]+=btw_T2T3_Temp_InSoil_GR1[i]
                            Sum_Temp_15AboveBed_GR1[n][m]+=btw_T2T3_Temp_15AboveBed_GR1[i]
                            Sum_Temp_60AboveBed_GR1[n][m]+=btw_T2T3_Temp_60AboveBed_GR1[i]
                    
    # Finaly we put them into the list that we will visualise in the plots
        for n in range (0,24):
            for m in range (0,12):
                    Avg_Temp_CntrlRoof.append(Sum_Temp_CntrlRoof[n][m]/S[n][m])
                    Avg_Temp_UnderBed_GBR2.append(Sum_Temp_UnderBed_GBR2[n][m]/S[n][m])
                    Avg_Temp_InSoil_GBR2.append(Sum_Temp_InSoil_GBR2[n][m]/S[n][m])
                    Avg_Temp_15AboveBed_GBR2.append(Sum_Temp_15AboveBed_GBR2[n][m]/S[n][m])
                    Avg_Temp_60AboveBed_GBR2.append(Sum_Temp_60AboveBed_GBR2[n][m]/S[n][m])
                    Avg_Temp_UnderBed_GBR1.append(Sum_Temp_UnderBed_GBR1[n][m]/S[n][m])
                    Avg_Temp_InSoil_GBR1.append(Sum_Temp_15AboveBed_GBR1[n][m]/S[n][m])
                    Avg_Temp_15AboveBed_GBR1.append(Sum_Temp_15AboveBed_GBR1[n][m]/S[n][m])
                    Avg_Temp_60AboveBed_GBR1.append(Sum_Temp_60AboveBed_GBR1[n][m]/S[n][m])
                    Avg_Temp_UnderBed_GR2.append(Sum_Temp_UnderBed_GR2[n][m]/S[n][m])
                    Avg_Temp_InSoil_GR2.append(Sum_Temp_InSoil_GR2[n][m]/S[n][m])
                    Avg_Temp_15AboveBed_GR2.append(Sum_Temp_15AboveBed_GR2[n][m]/S[n][m])
                    Avg_Temp_60AboveBed_GR2.append(Sum_Temp_60AboveBed_GR2[n][m]/S[n][m])
                    Avg_Temp_UnderBed_GR1.append(Sum_Temp_UnderBed_GR1[n][m]/S[n][m])
                    Avg_Temp_InSoil_GR1.append(Sum_Temp_InSoil_GR1[n][m]/S[n][m])
                    Avg_Temp_15AboveBed_GR1.append(Sum_Temp_15AboveBed_GR1[n][m]/S[n][m])
                    Avg_Temp_60AboveBed_GR1.append(Sum_Temp_60AboveBed_GR1[n][m]/S[n][m])
                
    # And we visualise the plot 
        if a==1 :
            plt.plot_date(avg_time, Avg_Temp_60AboveBed_GBR1,"-", label = 'Average Temperature 60cm Above Bed_GBR1')
            plt.plot_date(avg_time, Avg_Temp_15AboveBed_GBR1,"-", label = 'Average Temperature 15cm Above Bed_GBR1')
            plt.plot_date(avg_time, Avg_Temp_InSoil_GBR1,"-", label = 'Average Temperature of Soil_GBR1')
            plt.plot_date(avg_time, Avg_Temp_UnderBed_GBR1,"-", label = 'Average Temperature under the bed_GBR1')
            plt.plot_date(avg_time, Avg_Temp_CntrlRoof,"-", label = 'Average Temperature of Control Roof')
            plt.legend()
            plt.title("Average Temperatures of the GRB1")
            plt.show()
            
        elif a==2 :
            plt.plot_date(avg_time, Avg_Temp_60AboveBed_GBR2,"-", label = 'Average Temperature 60cm Above Bed_GBR2')
            plt.plot_date(avg_time, Avg_Temp_15AboveBed_GBR2,"-", label = 'Average Temperature 15cm Above Bed_GBR2')
            plt.plot_date(avg_time, Avg_Temp_InSoil_GBR2,"-", label = 'Average Temperature of Soil_GBR2')
            plt.plot_date(avg_time, Avg_Temp_UnderBed_GBR2,"-", label = 'Average Temperature under the bed_GBR2')
            plt.plot_date(avg_time, Avg_Temp_CntrlRoof,"-", label = 'Average Temperature of Control Roof')
            plt.legend()
            plt.title("Average Temperatures of the GRB2")
            plt.show()
             
        elif a==3 :
            plt.plot_date(avg_time, Avg_Temp_60AboveBed_GR1,"-", label = 'Average Temperature 60cm Above Bed_GR1')
            plt.plot_date(avg_time, Avg_Temp_15AboveBed_GR1,"-", label = 'Average Temperature 15cm Above Bed_GR1')
            plt.plot_date(avg_time, Avg_Temp_InSoil_GR1,"-", label = 'Average Temperature of Soil_GR1')
            plt.plot_date(avg_time, Avg_Temp_UnderBed_GR1,"-", label = 'Average Temperature under the bed_GR1')
            plt.plot_date(avg_time, Avg_Temp_CntrlRoof,"-", label = 'Average Temperature of Control Roof')
            plt.legend()
            plt.title("Average Temperatures of the GR1")
            plt.show()
            
        elif a==4 :
            plt.plot_date(avg_time, Avg_Temp_60AboveBed_GR2,"-", label = 'Average Temperature 60cm Above Bed_GR2')
            plt.plot_date(avg_time, Avg_Temp_15AboveBed_GR2,"-", label = 'Avergae Temperature 15cm Above Bed_GR2')
            plt.plot_date(avg_time, Avg_Temp_InSoil_GR2,"-", label = 'Avergae Temperature of Soil_GR2')
            plt.plot_date(avg_time, Avg_Temp_UnderBed_GR2,"-", label = 'Average Temperature under the bed_GR2')
            plt.plot_date(avg_time, Avg_Temp_CntrlRoof,"-", label = 'AverageTemperature of Control Roof')
            plt.legend()
            plt.title("Average Temperatures of the GR2")
            plt.show()
             
    elif c==4 :
        for i in range (1,len(sup_T3_Temp_CntrlRoof)-1):
            for n in range (0,24):
                if Time_c4[i].hour==n:
                    for m in range (0,12):
                        if Time_c4[i].minute==(m*5):
                        
                            S[n][m]+=1
                          
                            Sum_Temp_CntrlRoof[n][m]+=sup_T3_Temp_CntrlRoof[i]
                            Sum_Temp_UnderBed_GBR2[n][m]+=sup_T3_Temp_UnderBed_GBR2[i]
                            Sum_Temp_InSoil_GBR2[n][m]+=sup_T3_Temp_InSoil_GBR2[i]
                            Sum_Temp_15AboveBed_GBR2[n][m]+=sup_T3_Temp_15AboveBed_GBR2[i]
                            Sum_Temp_60AboveBed_GBR2[n][m]+=sup_T3_Temp_60AboveBed_GBR2[i]
                            Sum_Temp_UnderBed_GBR1[n][m]+=sup_T3_Temp_UnderBed_GBR1[i]
                            Sum_Temp_InSoil_GBR1[n][m]+=sup_T3_Temp_InSoil_GBR1[i]
                            Sum_Temp_15AboveBed_GBR1[n][m]+=sup_T3_Temp_15AboveBed_GBR1[i]
                            Sum_Temp_60AboveBed_GBR1[n][m]+=sup_T3_Temp_60AboveBed_GBR1[i]
                            Sum_Temp_UnderBed_GR2[n][m]+=sup_T3_Temp_UnderBed_GR2[i]
                            Sum_Temp_InSoil_GR2[n][m]+=sup_T3_Temp_InSoil_GR2[i]
                            Sum_Temp_15AboveBed_GR2[n][m]+=sup_T3_Temp_15AboveBed_GR2[i]
                            Sum_Temp_60AboveBed_GR2[n][m]+=sup_T3_Temp_60AboveBed_GR2[i]
                            Sum_Temp_UnderBed_GR1[n][m]+=sup_T3_Temp_UnderBed_GR1[i]
                            Sum_Temp_InSoil_GR1[n][m]+=sup_T3_Temp_InSoil_GR1[i]
                            Sum_Temp_15AboveBed_GR1[n][m]+=sup_T3_Temp_15AboveBed_GR1[i]
                            Sum_Temp_60AboveBed_GR1[n][m]+=sup_T3_Temp_60AboveBed_GR1[i]
                    
    # Finaly we put them into the list that we will visualise in the plots
        for n in range (0,24):
            for m in range (0,12):
                    Avg_Temp_CntrlRoof.append(Sum_Temp_CntrlRoof[n][m]/S[n][m])
                    Avg_Temp_UnderBed_GBR2.append(Sum_Temp_UnderBed_GBR2[n][m]/S[n][m])
                    Avg_Temp_InSoil_GBR2.append(Sum_Temp_InSoil_GBR2[n][m]/S[n][m])
                    Avg_Temp_15AboveBed_GBR2.append(Sum_Temp_15AboveBed_GBR2[n][m]/S[n][m])
                    Avg_Temp_60AboveBed_GBR2.append(Sum_Temp_60AboveBed_GBR2[n][m]/S[n][m])
                    Avg_Temp_UnderBed_GBR1.append(Sum_Temp_UnderBed_GBR1[n][m]/S[n][m])
                    Avg_Temp_InSoil_GBR1.append(Sum_Temp_15AboveBed_GBR1[n][m]/S[n][m])
                    Avg_Temp_15AboveBed_GBR1.append(Sum_Temp_15AboveBed_GBR1[n][m]/S[n][m])
                    Avg_Temp_60AboveBed_GBR1.append(Sum_Temp_60AboveBed_GBR1[n][m]/S[n][m])
                    Avg_Temp_UnderBed_GR2.append(Sum_Temp_UnderBed_GR2[n][m]/S[n][m])
                    Avg_Temp_InSoil_GR2.append(Sum_Temp_InSoil_GR2[n][m]/S[n][m])
                    Avg_Temp_15AboveBed_GR2.append(Sum_Temp_15AboveBed_GR2[n][m]/S[n][m])
                    Avg_Temp_60AboveBed_GR2.append(Sum_Temp_60AboveBed_GR2[n][m]/S[n][m])
                    Avg_Temp_UnderBed_GR1.append(Sum_Temp_UnderBed_GR1[n][m]/S[n][m])
                    Avg_Temp_InSoil_GR1.append(Sum_Temp_InSoil_GR1[n][m]/S[n][m])
                    Avg_Temp_15AboveBed_GR1.append(Sum_Temp_15AboveBed_GR1[n][m]/S[n][m])
                    Avg_Temp_60AboveBed_GR1.append(Sum_Temp_60AboveBed_GR1[n][m]/S[n][m])
                
    # And we visualise the plot 
        if a==1 :
            plt.plot_date(avg_time, Avg_Temp_60AboveBed_GBR1,"-", label = 'Average Temperature 60cm Above Bed_GBR1')
            plt.plot_date(avg_time, Avg_Temp_15AboveBed_GBR1,"-", label = 'Average Temperature 15cm Above Bed_GBR1')
            plt.plot_date(avg_time, Avg_Temp_InSoil_GBR1,"-", label = 'Average Temperature of Soil_GBR1')
            plt.plot_date(avg_time, Avg_Temp_UnderBed_GBR1,"-", label = 'Average Temperature under the bed_GBR1')
            plt.plot_date(avg_time, Avg_Temp_CntrlRoof,"-", label = 'Average Temperature of Control Roof')
            plt.legend()
            plt.title("Average Temperatures of the GRB1")
            plt.show()
            
        elif a==2 :
            plt.plot_date(avg_time, Avg_Temp_60AboveBed_GBR2,"-", label = 'Average Temperature 60cm Above Bed_GBR2')
            plt.plot_date(avg_time, Avg_Temp_15AboveBed_GBR2,"-", label = 'Average Temperature 15cm Above Bed_GBR2')
            plt.plot_date(avg_time, Avg_Temp_InSoil_GBR2,"-", label = 'Average Temperature of Soil_GBR2')
            plt.plot_date(avg_time, Avg_Temp_UnderBed_GBR2,"-", label = 'Average Temperature under the bed_GBR2')
            plt.plot_date(avg_time, Avg_Temp_CntrlRoof,"-", label = 'Average Temperature of Control Roof')
            plt.legend()
            plt.title("Average Temperatures of the GRB2")
            plt.show()
             
        elif a==3 :
            plt.plot_date(avg_time, Avg_Temp_60AboveBed_GR1,"-", label = 'Average Temperature 60cm Above Bed_GR1')
            plt.plot_date(avg_time, Avg_Temp_15AboveBed_GR1,"-", label = 'Average Temperature 15cm Above Bed_GR1')
            plt.plot_date(avg_time, Avg_Temp_InSoil_GR1,"-", label = 'Average Temperature of Soil_GR1')
            plt.plot_date(avg_time, Avg_Temp_UnderBed_GR1,"-", label = 'Average Temperature under the bed_GR1')
            plt.plot_date(avg_time, Avg_Temp_CntrlRoof,"-", label = 'Average Temperature of Control Roof')
            plt.legend()
            plt.title("Average Temperatures of the GR1")
            plt.show()
            
        elif a==4 :
            plt.plot_date(avg_time, Avg_Temp_60AboveBed_GR2,"-", label = 'Average Temperature 60cm Above Bed_GR2')
            plt.plot_date(avg_time, Avg_Temp_15AboveBed_GR2,"-", label = 'Avergae Temperature 15cm Above Bed_GR2')
            plt.plot_date(avg_time, Avg_Temp_InSoil_GR2,"-", label = 'Avergae Temperature of Soil_GR2')
            plt.plot_date(avg_time, Avg_Temp_UnderBed_GR2,"-", label = 'Average Temperature under the bed_GR2')
            plt.plot_date(avg_time, Avg_Temp_CntrlRoof,"-", label = 'AverageTemperature of Control Roof')
            plt.legend()
            plt.title("Average Temperatures of the GR2")
            plt.show()
             

# 6/ Creating dialog to use easily this code

"""

print("Hi there, \n If you want to visualise the raw data of : \n")
print("    - the temperatrues of the BGR1, run 'raw_BGR1_visu()' on the console")
print("    - the temperatrues of the BGR2, run 'raw_BGR2_visu()' on the console")
print("    - the temperatrues of the GR1, run 'raw_GR1_visu()' on the console")
print("    - the temperatrues of the GR2, run 'raw_GR2_visu()' on the console")
print("    - the Raingauges, run 'raw_RG_visu()' on the console")

print(" \n If you want to visualise the denoised data : \n")  
print("    - the temperatrues of the BGR1, run 'filter_BGR1_visu()' on the console")
print("    - the temperatrues of the BGR2, run 'filter_BGR2_visu()' on the console")
print("    - the temperatrues of the GR1, run 'filter_GR1_visu()' on the console")
print("    - the temperatrues of the GR2, run 'filter_GR2_visu()' on the console")
print("    - the Raingauges, run 'filter_RG_visu()' on the console")

print(" \n If you want to visualise the average of all the data displayed on a day scale : \n")  
print("    - the temperatrues of the BGR1, run 'avg_BGR1_visu()' on the console")
print("    - the temperatrues of the BGR2, run 'avg_BGR2_visu()' on the console")
print("    - the temperatrues of the GR1, run 'avg_GR1_visu()' on the console")
print("    - the temperatrues of the GR2, run 'avg_GR2_visu()' on the console")
print("    - the Raingauges, run 'avg_RG_visu()' on the console")

print(" \n If you want to visualise the average of all the data startified by the average temperature of the day : \n")  
print("    - the temperatrues of the BGR1, run 'cat_BGR1_visu()' on the console")
print("    - the temperatrues of the BGR2, run 'cat_BGR2_visu()' on the console")
print("    - the temperatrues of the GR1, run 'cat_GR1_visu()' on the console")
print("    - the temperatrues of the GR2, run 'cat_GR2_visu()' on the console")

print(" \n If you want to know the correlation of : \n")
print("    - the temperature sensors of the BGR1, run 'corr_BGR1' on the console")
print("    - the temperature sensors of the BGR2, run 'corr_BGR2' on the console")
print("    - the temperature sensors of the GR1, run 'corr_GR1' on the console")
print("    - the temperature sensors of the GR2, run 'corr_GR2' on the console")
print("    - the temperature sensors between the beds, run 'corr_beds' on the console")
"""




# Bonus/ Failed attempts at coding   

  
#l = time.strptime(july_11[0][2], '%d/%m/%Y %H:%M')
#datetime.datetime(2022,int(data_table[0][i][3:5]),int(data_table[0][i][0:2]),int(data_table[0][i][11:13]),int(data_table[0][i][15:17])))
#time.strptime(data_table[0][i], '%d/%m/%Y %H:%M'))
