# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 00:16:32 2022

@author: lolan
"""
import pandas as pd
import datetime
import numpy as np
import matplotlib.pyplot as plt
from math import *
import statistics
import scipy.signal 
from statsmodels.nonparametric.smoothers_lowess import lowess
from sklearn.linear_model import LinearRegression # to build a LR model for comparison


july_11 = pd.read_csv(r"C:/Users/lolan/OneDrive/Bureau/Gritlab data/2022-07-11/11_july DATA PROCESSED.csv", sep = ";", header = None)
july_18 = pd.read_csv(r"C:/Users/lolan/OneDrive/Bureau/Gritlab data/2022-07-18/18_july DATA PROCESSED.csv", sep = ";", header = None)
aug_29  = pd.read_csv(r"C:/Users/lolan/OneDrive/Bureau/Gritlab data/2022-08-29/29_aug DATA PROCESSED.csv", sep = ";", header = None)

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
    Time_float=[]
 
# Then we transform the data into float so that we can manipulate it with Python and put it in the right list


    for i in range (1,len(data_table)):
        
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
        
        Time_float.append(float(data_table[21][i]))
           
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
                    Temp_60AboveBed_GR1,
                    Time_float)

def denoised_temp_v1(data_table,n):

#Fisrt we name the different lists of data we want to visualize  
    
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

    for i in range (2,len(data_table)-1):
        if int(data_table[0][i][11:13])-int(data_table[0][i-1][11:13])>1 or int(data_table[0][i+1][11:13])-int(data_table[0][i][11:13])>1:
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
        else :
            Time.append(datetime.datetime(2022,int(data_table[0][i][3:5]),int(data_table[0][i][0:2]),int(data_table[0][i][11:13]),int(data_table[0][i][14:16])))
            Temp_CntrlRoof.append((float(data_table[5][i-1]) + float(data_table[5][i])+float(data_table[5][i+1]))/3)
            Temp_UnderBed_GBR2.append((float(data_table[6][i-1])+float(data_table[6][i])+float(data_table[6][i+1]))/3)
            Temp_InSoil_GBR2.append((float(data_table[7][i-1])+float(data_table[7][i])+float(data_table[7][i+1]))/3)
            Temp_15AboveBed_GBR2.append((float(data_table[8][i-1])+float(data_table[8][i])+float(data_table[8][i+1]))/3)
            Temp_60AboveBed_GBR2.append((float(data_table[9][i-1])+float(data_table[9][i])+float(data_table[9][i+1]))/3)
            Temp_UnderBed_GBR1.append((float(data_table[10][i-1])+float(data_table[10][i])+float(data_table[10][i+1]))/3)
            Temp_InSoil_GBR1.append((float(data_table[11][i-1])+float(data_table[11][i])+float(data_table[11][i+1]))/3)
            Temp_15AboveBed_GBR1.append((float(data_table[12][i-1])+float(data_table[12][i])+float(data_table[12][i+1]))/3)
            Temp_60AboveBed_GBR1.append((float(data_table[13][i-1])+float(data_table[13][i])+float(data_table[13][i+1]))/3)
            Temp_UnderBed_GR2.append((float(data_table[14][i-1])+float(data_table[14][i])+float(data_table[14][i+1]))/3)
            Temp_InSoil_GR2.append((float(data_table[15][i-1])+float(data_table[15][i])+float(data_table[15][i+1]))/3)
            Temp_15AboveBed_GR2.append((float(data_table[16][i-1])+float(data_table[16][i])+float(data_table[16][i+1]))/3)
            Temp_60AboveBed_GR2.append((float(data_table[17][i-1])+float(data_table[17][i])+float(data_table[17][i+1]))/3)
            Temp_UnderBed_GR1.append((float(data_table[18][i-1])+float(data_table[18][i])+float(data_table[18][i+1]))/3)
            Temp_InSoil_GR1.append((float(data_table[19][i-1])+float(data_table[19][i])+float(data_table[19][i+1]))/3)
            Temp_15AboveBed_GR1.append((float(data_table[20][i-1])+float(data_table[20][i])+float(data_table[20][i+1]))/3)
            Temp_60AboveBed_GR1.append((float(data_table[21][i-1])+float(data_table[21][i])+float(data_table[21][i+1]))/3)
           
    
# Finaly we visualize the temperature according to the bed we are interested in

    if n==1 :
        plt.plot_date(Time, Temp_60AboveBed_GBR1,"-", label = 'Temperature 60cm Above Bed_GBR1')
        plt.plot_date(Time, Temp_15AboveBed_GBR1,"-", label = 'Temperature 15cm Above Bed_GBR1')
        plt.plot_date(Time, Temp_InSoil_GBR1,"-", label = 'Temperature of Soil_GBR1')
        plt.plot_date(Time, Temp_UnderBed_GBR1,"-", label = 'Temperature under the bed_GBR1')
        plt.plot_date(Time, Temp_CntrlRoof,"-", label = 'Temperature of Control Roof')
        plt.legend()
        plt.title("Denoised Temperatures of the GRB1")
        plt.show()
        
    elif n==2 :
        plt.plot_date(Time, Temp_60AboveBed_GBR2,"-", label = 'Temperature 60cm Above Bed_GBR2')
        plt.plot_date(Time, Temp_15AboveBed_GBR2,"-", label = 'Temperature 15cm Above Bed_GBR2')
        plt.plot_date(Time, Temp_InSoil_GBR2,"-", label = 'Temperature of Soil_GBR2')
        plt.plot_date(Time, Temp_UnderBed_GBR2,"-", label = 'Temperature under the bed_GBR2')
        plt.plot_date(Time, Temp_CntrlRoof,"-", label = 'Temperature of Control Roof')
        plt.legend()
        plt.title("Denoised Temperatures of the GRB2")
        plt.show()
        
    elif n==3 :
        plt.plot_date(Time, Temp_60AboveBed_GR1,"-", label = 'Temperature 60cm Above Bed_GR1')
        plt.plot_date(Time, Temp_15AboveBed_GR1,"-", label = 'Temperature 15cm Above Bed_GR1')
        plt.plot_date(Time, Temp_InSoil_GR1,"-", label = 'Temperature of Soil_GR1')
        plt.plot_date(Time, Temp_UnderBed_GR1,"-", label = 'Temperature under the bed_GR1')
        plt.plot_date(Time, Temp_CntrlRoof,"-", label = 'Temperature of Control Roof')
        plt.legend()
        plt.title("Denoised Temperatures of the GR1")
        plt.show()
        
    elif n==4 :
        plt.plot_date(Time, Temp_60AboveBed_GR2,"-", label = 'Temperature 60cm Above Bed_GR2')
        plt.plot_date(Time, Temp_15AboveBed_GR2,"-", label = 'Temperature 15cm Above Bed_GR2')
        plt.plot_date(Time, Temp_InSoil_GR2,"-", label = 'Temperature of Soil_GR2')
        plt.plot_date(Time, Temp_UnderBed_GR2,"-", label = 'Temperature under the bed_GR2')
        plt.plot_date(Time, Temp_CntrlRoof,"-", label = 'Temperature of Control Roof')
        plt.legend()
        plt.title("Denoised Temperatures of the GR2")
        plt.show()


#Second try (taking average of n=+-2 around the data)

def denoised_temp_v2(data_table,n):

#Fisrt we name the different lists of data we want to visualize  
    
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

    for i in range (3,len(data_table)-2):
        if int(data_table[0][i][11:13])-int(data_table[0][i-1][11:13])>1 or int(data_table[0][i+1][11:13])-int(data_table[0][i][11:13])>1 or int(data_table[0][i-1][11:13])-int(data_table[0][i-2][11:13])>1 or int(data_table[0][i+2][11:13])-int(data_table[0][i+1][11:13])>1:
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
        else :
            Time.append(datetime.datetime(2022,int(data_table[0][i][3:5]),int(data_table[0][i][0:2]),int(data_table[0][i][11:13]),int(data_table[0][i][14:16])))
            Temp_CntrlRoof.append((float(data_table[5][i-2]) + float(data_table[5][i-1]) + float(data_table[5][i])+float(data_table[5][i+1])+float(data_table[5][i+2]))/5)
            Temp_UnderBed_GBR2.append((float(data_table[6][i-2])+float(data_table[6][i-1])+float(data_table[6][i])+float(data_table[6][i+1])+float(data_table[6][i+2]))/5)
            Temp_InSoil_GBR2.append((float(data_table[7][i-2])+float(data_table[7][i-1])+float(data_table[7][i])+float(data_table[7][i+1])+float(data_table[6][i+2]))/5)
            Temp_15AboveBed_GBR2.append((float(data_table[8][i-2])+float(data_table[8][i-1])+float(data_table[8][i])+float(data_table[8][i+1])+float(data_table[8][i+2]))/5)
            Temp_60AboveBed_GBR2.append((float(data_table[9][i-2])+float(data_table[9][i-1])+float(data_table[9][i])+float(data_table[9][i+1])+float(data_table[9][i+2]))/5)
            Temp_UnderBed_GBR1.append((float(data_table[10][i-2])+float(data_table[10][i-1])+float(data_table[10][i])+float(data_table[10][i+1])+float(data_table[10][i+2]))/5)
            Temp_InSoil_GBR1.append((float(data_table[11][i-2])+float(data_table[11][i-1])+float(data_table[11][i])+float(data_table[11][i+1])+float(data_table[11][i+2]))/5)
            Temp_15AboveBed_GBR1.append((float(data_table[12][i-2])+float(data_table[12][i-1])+float(data_table[12][i])+float(data_table[12][i+1])+float(data_table[12][i+2]))/5)
            Temp_60AboveBed_GBR1.append((float(data_table[13][i-2])+float(data_table[13][i-1])+float(data_table[13][i])+float(data_table[13][i+1])+float(data_table[13][i+2]))/5)
            Temp_UnderBed_GR2.append((float(data_table[14][i-2])+float(data_table[14][i-1])+float(data_table[14][i])+float(data_table[14][i+1])+float(data_table[14][i+2]))/5)
            Temp_InSoil_GR2.append((float(data_table[15][i-2])+float(data_table[15][i-1])+float(data_table[15][i])+float(data_table[15][i+1])+float(data_table[15][i+2]))/5)
            Temp_15AboveBed_GR2.append((float(data_table[16][i-2])+float(data_table[16][i-1])+float(data_table[16][i])+float(data_table[16][i+1])+float(data_table[16][i+2]))/5)
            Temp_60AboveBed_GR2.append((float(data_table[17][i-2])+float(data_table[17][i-1])+float(data_table[17][i])+float(data_table[17][i+1])+float(data_table[17][i+2]))/5)
            Temp_UnderBed_GR1.append((float(data_table[18][i-2])+float(data_table[18][i-1])+float(data_table[18][i])+float(data_table[18][i+1])+float(data_table[18][i+2]))/5)
            Temp_InSoil_GR1.append((float(data_table[19][i-2])+float(data_table[19][i-1])+float(data_table[19][i])+float(data_table[19][i+1])+float(data_table[19][i+2]))/5)
            Temp_15AboveBed_GR1.append((float(data_table[20][i-2])+float(data_table[20][i-1])+float(data_table[20][i])+float(data_table[20][i+1])+float(data_table[20][i+2]))/5)
            Temp_60AboveBed_GR1.append((float(data_table[21][i-2])+float(data_table[21][i-1])+float(data_table[21][i])+float(data_table[21][i+1])+float(data_table[21][i+2]))/5)
           
    
# Finaly we visualize the temperature according to the bed we are interested in

    if n==1 :
        plt.plot_date(Time, Temp_60AboveBed_GBR1,"-", label = 'Temperature 60cm Above Bed_GBR1')
        plt.plot_date(Time, Temp_15AboveBed_GBR1,"-", label = 'Temperature 15cm Above Bed_GBR1')
        plt.plot_date(Time, Temp_InSoil_GBR1,"-", label = 'Temperature of Soil_GBR1')
        plt.plot_date(Time, Temp_UnderBed_GBR1,"-", label = 'Temperature under the bed_GBR1')
        plt.plot_date(Time, Temp_CntrlRoof,"-", label = 'Temperature of Control Roof')
        plt.legend()
        plt.title("Denoised Temperatures of the GRB1")
        plt.show()
        
    elif n==2 :
        plt.plot_date(Time, Temp_60AboveBed_GBR2,"-", label = 'Temperature 60cm Above Bed_GBR2')
        plt.plot_date(Time, Temp_15AboveBed_GBR2,"-", label = 'Temperature 15cm Above Bed_GBR2')
        plt.plot_date(Time, Temp_InSoil_GBR2,"-", label = 'Temperature of Soil_GBR2')
        plt.plot_date(Time, Temp_UnderBed_GBR2,"-", label = 'Temperature under the bed_GBR2')
        plt.plot_date(Time, Temp_CntrlRoof,"-", label = 'Temperature of Control Roof')
        plt.legend()
        plt.title("Denoised Temperatures of the GRB2")
        plt.show()
        
    elif n==3 :
        plt.plot_date(Time, Temp_60AboveBed_GR1,"-", label = 'Temperature 60cm Above Bed_GR1')
        plt.plot_date(Time, Temp_15AboveBed_GR1,"-", label = 'Temperature 15cm Above Bed_GR1')
        plt.plot_date(Time, Temp_InSoil_GR1,"-", label = 'Temperature of Soil_GR1')
        plt.plot_date(Time, Temp_UnderBed_GR1,"-", label = 'Temperature under the bed_GR1')
        plt.plot_date(Time, Temp_CntrlRoof,"-", label = 'Temperature of Control Roof')
        plt.legend()
        plt.title("Denoised Temperatures of the GR1")
        plt.show()
        
    elif n==4 :
        plt.plot_date(Time, Temp_60AboveBed_GR2,"-", label = 'Temperature 60cm Above Bed_GR2')
        plt.plot_date(Time, Temp_15AboveBed_GR2,"-", label = 'Temperature 15cm Above Bed_GR2')
        plt.plot_date(Time, Temp_InSoil_GR2,"-", label = 'Temperature of Soil_GR2')
        plt.plot_date(Time, Temp_UnderBed_GR2,"-", label = 'Temperature under the bed_GR2')
        plt.plot_date(Time, Temp_CntrlRoof,"-", label = 'Temperature of Control Roof')
        plt.legend()
        plt.title("Denoised Temperatures of the GR2")
        plt.show()




def moving_avg(data_table,n,k):
    
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
    
    if k<=1 : 
        
        for p in range (1, len(data_table)-1):
        
            Avg_Temp_CntrlRoof.append((1/k)*(Temp_CntrlRoof[p]-Temp_CntrlRoof[p-k])+Avg_Temp_CntrlRoof[p-1])
            Avg_Temp_UnderBed_GBR2.append((1/k)*(Temp_UnderBed_GBR2[p]-Temp_UnderBed_GBR2[p-k])+Avg_Temp_UnderBed_GBR2[p-1])
            Avg_Temp_InSoil_GBR2.append((1/k)*(Temp_InSoil_GBR2[p]-Temp_InSoil_GBR2[p-k])+Avg_Temp_InSoil_GBR2[p-1])
            Avg_Temp_15AboveBed_GBR2.append((1/k)*(Temp_15AboveBed_GBR2[p]-Temp_15AboveBed_GBR2[p-k])+Avg_Temp_15AboveBed_GBR2[p-1])
            Avg_Temp_60AboveBed_GBR2.append((1/k)*(Temp_60AboveBed_GBR2[p]-Temp_60AboveBed_GBR2[p-k])+Avg_Temp_60AboveBed_GBR2[p-1])
            Avg_Temp_UnderBed_GBR1.append((1/k)*(Temp_UnderBed_GBR1[p]-Temp_UnderBed_GBR1[p-k])+Avg_Temp_UnderBed_GBR1[p-1])
            Avg_Temp_InSoil_GBR1.append((1/k)*(Temp_InSoil_GBR1[p]-Temp_InSoil_GBR1[p-k])+Avg_Temp_InSoil_GBR1[p-1])
            Avg_Temp_15AboveBed_GBR1.append((1/k)*(Temp_15AboveBed_GBR1[p]-Temp_15AboveBed_GBR1[p-k])+Avg_Temp_15AboveBed_GBR1[p-1])
            Avg_Temp_60AboveBed_GBR1.append((1/k)*(Temp_60AboveBed_GBR1[p]-Temp_60AboveBed_GBR1[p-k])+Avg_Temp_60AboveBed_GBR1[p-1])
            Avg_Temp_UnderBed_GR2.append((1/k)*(Temp_UnderBed_GR2[p]-Temp_UnderBed_GR2[p-k])+Avg_Temp_UnderBed_GR2[p-1])
            Avg_Temp_InSoil_GR2.append((1/k)*(Temp_InSoil_GR2[p]-Temp_InSoil_GR2[p-k])+Avg_Temp_InSoil_GR2[p-1])
            Avg_Temp_15AboveBed_GR2.append((1/k)*(Temp_15AboveBed_GR2[p]-Temp_15AboveBed_GR2[p-k])+Avg_Temp_15AboveBed_GR2[p-1])
            Avg_Temp_60AboveBed_GR2.append((1/k)*(Temp_60AboveBed_GR2[p]-Temp_60AboveBed_GR2[p-k])+Avg_Temp_60AboveBed_GR2[p-1])
            Avg_Temp_UnderBed_GR1.append((1/k)*(Temp_UnderBed_GR1[p]-Temp_UnderBed_GR1[p-k])+Avg_Temp_UnderBed_GR1[p-1])
            Avg_Temp_InSoil_GR1.append((1/k)*(Temp_InSoil_GR1[p]-Temp_InSoil_GR1[p-k])+Avg_Temp_InSoil_GR1[p-1])
            Avg_Temp_15AboveBed_GR1.append((1/k)*(Temp_15AboveBed_GR1[p]-Temp_15AboveBed_GR1[p-k])+Avg_Temp_15AboveBed_GR1[p-1])
            Avg_Temp_60AboveBed_GR1.append((1/k)*(Temp_60AboveBed_GR1[p]-Temp_60AboveBed_GR1[p-k])+Avg_Temp_60AboveBed_GR1[p-1])
        
    else : 
        
        for p in range (1,k) :
        
            Avg_Temp_CntrlRoof.append((1/p)*(Temp_CntrlRoof[p]-Temp_CntrlRoof[0])+Avg_Temp_CntrlRoof[p-1])
            Avg_Temp_UnderBed_GBR2.append((1/p)*(Temp_UnderBed_GBR2[p]-Temp_UnderBed_GBR2[0])+Avg_Temp_UnderBed_GBR2[p-1])
            Avg_Temp_InSoil_GBR2.append((1/p)*(Temp_InSoil_GBR2[p]-Temp_InSoil_GBR2[0])+Avg_Temp_InSoil_GBR2[p-1])
            Avg_Temp_15AboveBed_GBR2.append((1/p)*(Temp_15AboveBed_GBR2[p]-Temp_15AboveBed_GBR2[0])+Avg_Temp_15AboveBed_GBR2[p-1])
            Avg_Temp_60AboveBed_GBR2.append((1/p)*(Temp_60AboveBed_GBR2[p]-Temp_60AboveBed_GBR2[0])+Avg_Temp_60AboveBed_GBR2[p-1])
            Avg_Temp_UnderBed_GBR1.append((1/p)*(Temp_UnderBed_GBR1[p]-Temp_UnderBed_GBR1[0])+Avg_Temp_UnderBed_GBR1[p-1])
            Avg_Temp_InSoil_GBR1.append((1/p)*(Temp_InSoil_GBR1[p]-Temp_InSoil_GBR1[0])+Avg_Temp_InSoil_GBR1[p-1])
            Avg_Temp_15AboveBed_GBR1.append((1/p)*(Temp_15AboveBed_GBR1[p]-Temp_15AboveBed_GBR1[0])+Avg_Temp_15AboveBed_GBR1[p-1])
            Avg_Temp_60AboveBed_GBR1.append((1/p)*(Temp_60AboveBed_GBR1[p]-Temp_60AboveBed_GBR1[0])+Avg_Temp_60AboveBed_GBR1[p-1])
            Avg_Temp_UnderBed_GR2.append((1/p)*(Temp_UnderBed_GR2[p]-Temp_UnderBed_GR2[0])+Avg_Temp_UnderBed_GR2[p-1])
            Avg_Temp_InSoil_GR2.append((1/p)*(Temp_InSoil_GR2[p]-Temp_InSoil_GR2[0])+Avg_Temp_InSoil_GR2[p-1])
            Avg_Temp_15AboveBed_GR2.append((1/p)*(Temp_15AboveBed_GR2[p]-Temp_15AboveBed_GR2[0])+Avg_Temp_15AboveBed_GR2[p-1])
            Avg_Temp_60AboveBed_GR2.append((1/p)*(Temp_60AboveBed_GR2[p]-Temp_60AboveBed_GR2[0])+Avg_Temp_60AboveBed_GR2[p-1])
            Avg_Temp_UnderBed_GR1.append((1/p)*(Temp_UnderBed_GR1[p]-Temp_UnderBed_GR1[0])+Avg_Temp_UnderBed_GR1[p-1])
            Avg_Temp_InSoil_GR1.append((1/p)*(Temp_InSoil_GR1[p]-Temp_InSoil_GR1[0])+Avg_Temp_InSoil_GR1[p-1])
            Avg_Temp_15AboveBed_GR1.append((1/p)*(Temp_15AboveBed_GR1[p]-Temp_15AboveBed_GR1[0])+Avg_Temp_15AboveBed_GR1[p-1])
            Avg_Temp_60AboveBed_GR1.append((1/p)*(Temp_60AboveBed_GR1[p]-Temp_60AboveBed_GR1[0])+Avg_Temp_60AboveBed_GR1[p-1])
        
        
        for p in range (k, len(data_table)-1):
        
            Avg_Temp_CntrlRoof.append((1/k)*(Temp_CntrlRoof[p]-Temp_CntrlRoof[p-k])+Avg_Temp_CntrlRoof[p-1])
            Avg_Temp_UnderBed_GBR2.append((1/k)*(Temp_UnderBed_GBR2[p]-Temp_UnderBed_GBR2[p-k])+Avg_Temp_UnderBed_GBR2[p-1])
            Avg_Temp_InSoil_GBR2.append((1/k)*(Temp_InSoil_GBR2[p]-Temp_InSoil_GBR2[p-k])+Avg_Temp_InSoil_GBR2[p-1])
            Avg_Temp_15AboveBed_GBR2.append((1/k)*(Temp_15AboveBed_GBR2[p]-Temp_15AboveBed_GBR2[p-k])+Avg_Temp_15AboveBed_GBR2[p-1])
            Avg_Temp_60AboveBed_GBR2.append((1/k)*(Temp_60AboveBed_GBR2[p]-Temp_60AboveBed_GBR2[p-k])+Avg_Temp_60AboveBed_GBR2[p-1])
            Avg_Temp_UnderBed_GBR1.append((1/k)*(Temp_UnderBed_GBR1[p]-Temp_UnderBed_GBR1[p-k])+Avg_Temp_UnderBed_GBR1[p-1])
            Avg_Temp_InSoil_GBR1.append((1/k)*(Temp_InSoil_GBR1[p]-Temp_InSoil_GBR1[p-k])+Avg_Temp_InSoil_GBR1[p-1])
            Avg_Temp_15AboveBed_GBR1.append((1/k)*(Temp_15AboveBed_GBR1[p]-Temp_15AboveBed_GBR1[p-k])+Avg_Temp_15AboveBed_GBR1[p-1])
            Avg_Temp_60AboveBed_GBR1.append((1/k)*(Temp_60AboveBed_GBR1[p]-Temp_60AboveBed_GBR1[p-k])+Avg_Temp_60AboveBed_GBR1[p-1])
            Avg_Temp_UnderBed_GR2.append((1/k)*(Temp_UnderBed_GR2[p]-Temp_UnderBed_GR2[p-k])+Avg_Temp_UnderBed_GR2[p-1])
            Avg_Temp_InSoil_GR2.append((1/k)*(Temp_InSoil_GR2[p]-Temp_InSoil_GR2[p-k])+Avg_Temp_InSoil_GR2[p-1])
            Avg_Temp_15AboveBed_GR2.append((1/k)*(Temp_15AboveBed_GR2[p]-Temp_15AboveBed_GR2[p-k])+Avg_Temp_15AboveBed_GR2[p-1])
            Avg_Temp_60AboveBed_GR2.append((1/k)*(Temp_60AboveBed_GR2[p]-Temp_60AboveBed_GR2[p-k])+Avg_Temp_60AboveBed_GR2[p-1])
            Avg_Temp_UnderBed_GR1.append((1/k)*(Temp_UnderBed_GR1[p]-Temp_UnderBed_GR1[p-k])+Avg_Temp_UnderBed_GR1[p-1])
            Avg_Temp_InSoil_GR1.append((1/k)*(Temp_InSoil_GR1[p]-Temp_InSoil_GR1[p-k])+Avg_Temp_InSoil_GR1[p-1])
            Avg_Temp_15AboveBed_GR1.append((1/k)*(Temp_15AboveBed_GR1[p]-Temp_15AboveBed_GR1[p-k])+Avg_Temp_15AboveBed_GR1[p-1])
            Avg_Temp_60AboveBed_GR1.append((1/k)*(Temp_60AboveBed_GR1[p]-Temp_60AboveBed_GR1[p-k])+Avg_Temp_60AboveBed_GR1[p-1])
    
    
    
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

def savitzky_golay(data_table,n,k) :
    
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
    
   
    Avg_Temp_CntrlRoof = scipy.signal.savgol_filter(Temp_CntrlRoof, k, 3)
    Avg_Temp_UnderBed_GBR2 = scipy.signal.savgol_filter(Temp_UnderBed_GBR2, k, 3)
    Avg_Temp_InSoil_GBR2 = scipy.signal.savgol_filter(Temp_InSoil_GBR2, k, 3)
    Avg_Temp_15AboveBed_GBR2 = scipy.signal.savgol_filter(Temp_15AboveBed_GBR2, k, 3)
    Avg_Temp_60AboveBed_GBR2 = scipy.signal.savgol_filter(Temp_60AboveBed_GBR2, k, 3)
    Avg_Temp_UnderBed_GBR1 = scipy.signal.savgol_filter(Temp_UnderBed_GBR1, k, 3)
    Avg_Temp_InSoil_GBR1 = scipy.signal.savgol_filter(Temp_InSoil_GBR1, k, 3)
    Avg_Temp_15AboveBed_GBR1 = scipy.signal.savgol_filter(Temp_15AboveBed_GBR1, k, 3)
    Avg_Temp_60AboveBed_GBR1 = scipy.signal.savgol_filter(Temp_60AboveBed_GBR1, k, 3)
    Avg_Temp_UnderBed_GR2 = scipy.signal.savgol_filter(Temp_UnderBed_GR1, k, 3)
    Avg_Temp_InSoil_GR2 = scipy.signal.savgol_filter(Temp_InSoil_GR1, k, 3)
    Avg_Temp_15AboveBed_GR2 = scipy.signal.savgol_filter(Temp_15AboveBed_GR1, k, 3)
    Avg_Temp_60AboveBed_GR2 = scipy.signal.savgol_filter(Temp_60AboveBed_GR1, k, 3)
    Avg_Temp_UnderBed_GR1 = scipy.signal.savgol_filter(Temp_UnderBed_GR2, k, 3)
    Avg_Temp_InSoil_GR1 = scipy.signal.savgol_filter(Temp_InSoil_GR2, k, 3)
    Avg_Temp_15AboveBed_GR1 = scipy.signal.savgol_filter(Temp_15AboveBed_GR2, k, 3)
    Avg_Temp_60AboveBed_GR1 = scipy.signal.savgol_filter(Temp_60AboveBed_GR2, k, 3)
    
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


def LOWESS(data_table,n,k):
    
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
    Time_float = temp_list(data_table)[18]
    
   
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
    
    Time_float_array = np.array(Time_float)
    X=Time_float_array.reshape(-1,1) # Note, we need X to be a 2D array, hence reshape
# x values for LOWESS
    x=Time_float
# y values for both
    Temp_CntrlRoof_array = np.array(Temp_CntrlRoof)
    y=Temp_CntrlRoof


# ------- Linear Regression -------
# Define and fit the model
    model1 = LinearRegression()
    LR = model1.fit(X, y)

# Predict a few points with Linear Regression model for the grpah
# Create 20 evenly spaced points from smallest X to largest X
    x_range = np.linspace(X.min(), X.max(), 1374) 
# Predict y values for our set of X values
    y_range = model1.predict(x_range.reshape(-1, 1))


# ------- LOWESS -------
# Generate y_hat values using lowess, try a couple values for hyperparameters
    y_hat1 = lowess(y, x) # note, default frac=2/3
    y_hat2 = lowess(y, x, frac=1/5)
    
    plt.plot_date(Time, Temp_CntrlRoof,".", label = 'point')
    plt.plot_date(Time, y_range,"-", label = 'LR')
    plt.plot_date(Time, y_hat1,"-", label = 'LOWESS1')
    plt.plot_date(Time, y_hat2,"-", label = 'LOWESS2')
    plt.legend()
    plt.title("Temperatures of the GR2")
    plt.show()

    
    
def Reg_lin(data_table,n,k):
    
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
    Time_float = temp_list(data_table)[18]
    
   
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