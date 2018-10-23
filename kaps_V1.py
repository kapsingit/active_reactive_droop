## Code generated : 8:42 PM, 6/17/2018
## By: Kapil Duwadi, kapil.duwadi@jacks.sdstate.edu


from buspy.bus import open_bus
from buspy.comm.message import CommonParam
from buspy.comm.message import MessageCommonData
import numpy as np

import pandas as pd


START_TIME = pd.to_datetime('2014-01-01 00:00:00') 
END_TIME = pd.to_datetime('2014-12-31 23:59:00') 


#df = pd.read_pickle("datasaved.pkl")
df = pd.read_csv('PV_Load.csv',index_col='index',parse_dates=True)
print("reading done\n")

DATA_FRAME=[]
LOAD_current_time=[]

DATA_FRAME.append(df['PV_Power'])

for i in range(1,13):
    DATA_FRAME.append(df['load_%d'% i])

current_time = START_TIME



HOUSE_FILE = 'agg_zips.txt'
BUS_FILE_MAIN = 'bus_in_main.json'
BUS_FILE_ITER = 'bus_in_iter.json'

global Final_power
global Display
global PMPPT
global voltage
global mp
global mq
global P_inv
global V_cri
global A
global Pc
global Del_Pc
global B_inv
global Q_inv
global I
global sensitivity
global Pcurtail
global V_criq
global Aq
global Qab
global Del_Qab
global Bq_inv
global Qabsorb

mp = 2187.5
mq = 523.0
Qmax = 2761.0
Q_inv = np.full((12,1),0.0001)
P_inv = np.full((12,1),0.0001)
voltage=np.full((12, 1), 240.0)
V_cri=np.full((12, 1), 250.08)
I=np.identity(12)
sensitivity=np.matrix([ [0.0509, 0.0509, 0.0486,0.0486, 0.0468,0.0468, 0.0455,0.0455, 0.0447,0.0447, 0.0442, 0.0442],
                        [0.0509, 0.0509, 0.0486,0.0486, 0.0468,0.0468, 0.0455,0.0455, 0.0447,0.0447, 0.0442, 0.0442],
                        [0.0510, 0.0510, 0.1055,0.1055, 0.1025,0.1025, 0.1002,0.1002, 0.0988,0.0988, 0.0981, 0.0981],
                        [0.0510, 0.0510, 0.1055,0.1055, 0.1025,0.1025, 0.1002,0.1002, 0.0988,0.0988, 0.0981, 0.0981],
                        [0.0510, 0.0510, 0.1055,0.1055, 0.1595,0.1595, 0.1564,0.1564, 0.1543,0.1543, 0.1532, 0.1532],
                        [0.0510, 0.0510, 0.1055,0.1055, 0.1595,0.1595, 0.1564,0.1564, 0.1543,0.1543, 0.1532, 0.1532],
                        [0.0510, 0.0510, 0.1055,0.1055, 0.1595,0.1595, 0.2136,0.2136, 0.2109,0.2109, 0.2095, 0.2095],
                        [0.0510, 0.0510, 0.1055,0.1055, 0.1595,0.1595, 0.2136,0.2136, 0.2109,0.2109, 0.2095, 0.2095],
                        [0.0510, 0.0510, 0.1055,0.1055, 0.1595,0.1595, 0.2136,0.2136, 0.2682,0.2682, 0.2066, 0.2066],
                        [0.0510, 0.0510, 0.1055,0.1055, 0.1595,0.1595, 0.2136,0.2136, 0.2682,0.2682, 0.2066, 0.2066],
                        [0.0510, 0.0510, 0.1055,0.1055, 0.1595,0.1595, 0.2136, 0.2136,0.2682,0.2682, 0.3241, 0.3241],
                        [0.0510, 0.0510, 0.1055,0.1055, 0.1595,0.1595, 0.2136, 0.2136,0.2682,0.2682, 0.3241, 0.3241]])

sensitivity_q = np.matrix([[0.1445,   0.1445,	0.1445,	0.1445,	0.1445,	0.1445,	0.1446,	0.1446,	0.1446,	0.1446,	0.1446,	0.1446],
                           [0.1445,	0.1445,	0.1445,	0.1445,	0.1445,	0.1445,	0.1446,	0.1446,	0.1446,	0.1446,	0.1446,	0.1446],
                           [0.1446,	0.1446,	0.1596,	0.1596,	0.1597,	0.1597,	0.1597,	0.1597,	0.1597,	0.1597,	0.1597,	0.1597],
                           [0.1446,	0.1446,	0.1596,	0.1596,	0.1597,	0.1597,	0.1597,	0.1597,	0.1597,	0.1597,	0.1597,	0.1597],
                           [0.1447,	0.1447,	0.1597,	0.1597,	0.1747,	0.1747,	0.1748,	0.1748,	0.1748,	0.1748,	0.1748,	0.1748],
                           [0.1447,	0.1447,	0.1597,	0.1597,	0.1747,	0.1747,	0.1748,	0.1748,	0.1748,	0.1748,	0.1748,	0.1748],
                           [0.1447,	0.1447,	0.1597,	0.1597,	0.1748,	0.1748,	0.1898,	0.1898,	0.1898,	0.1898,	0.1898,	0.1898],
                           [0.1447,	0.1447,	0.1597,	0.1597,	0.1748,	0.1748,	0.1898,	0.1898,	0.1898,	0.1898,	0.1898,	0.1898],
                           [0.1447,	0.1447,	0.1597,	0.1597,	0.1748,	0.1748,	0.1898,	0.1898,	0.2048,	0.2048,	0.2048,	0.2048],
                           [0.1447,	0.1447,	0.1597,	0.1597,	0.1748,	0.1748,	0.1898,	0.1898,	0.2048,	0.2048,	0.2048,	0.2048],
                           [0.1447,	0.1447,	0.1597,	0.1597,	0.1748,	0.1748,	0.1898,	0.1898,	0.2048,	0.2048,	0.2198,	0.2198],
                           [0.1447,	0.1447,	0.1597,	0.1597,	0.1748,	0.1748,	0.1898,	0.1898,	0.2048,	0.2048,	0.2198,	0.2198]])
V_criq = np.full((12, 1), 244.8)
Aq = np.full((12,1),0.0)
Qab = 0
Del_Qab=0
sens_q = sensitivity_q/1000
Bq=mq*(sens_q)+I
Bq_inv=np.linalg.inv(Bq)
Qabsorb=np.full((12,1),0.0)



A=np.full((12, 1), 0.0)
Pc=0
Del_Pc=0
sens = sensitivity/1000
B=mp*(sens)+I
B_inv=np.linalg.inv(B)
Pcurtail=np.full((12, 1), 0.0)

Final_power=[]

HOUSES=["PV_N6A_DH1","PV_N6A_DH2","PV_N6A_DH3","PV_N6A_DH4","PV_N6A_DH5","PV_N6A_DH6","PV_N6A_DH7","PV_N6A_DH8","PV_N6A_DH9","PV_N6A_DH10","PV_N6A_DH11","PV_N6A_DH12"]


def change_repower(mat_delq,i):
    if abs(voltage[i,0])>244.8:
        if abs(voltage[i,0])<250.08:
            qa = Qabsorb[i,0]+mat_delq
            qinv = round(qa,4)
        else:
            qinv = Qmax
    else:
        qinv = 0
    if abs(voltage[i,0])>250.08:
        qinv = Qmax
    if qinv>Qmax:
        qinv = Qmax

    Qabsorb[i,0] = qinv
                
    return qinv


def change_power(mat_del_pc, i):

    if abs(voltage[i,0])>=250.08:
        Del_Pc=mat_del_pc
        Pc=round(Pcurtail[i,0]+Del_Pc,4)
        Pinv=round(PMPPT+Pc,4)
    else:
        Pinv=PMPPT
        Pc=0.0
                
    if Pinv>0:
        Pinv=0.0
   
    if Pinv<PMPPT:
        Pinv=PMPPT
        Pc=0.0
        
    Pcurtail[i,0]=Pc
    return Pinv



def get_message(LOAD):
    global Q_inv
    global B_inv
    global A
    global mp
    global mq
    global voltage
    global P_inv
    global PMPPT
    global Final_power
    global Xq
    global Aq
    matqmax = np.full((12,1),Qmax)
    addp = sensitivity_q*matqmax
    transfer = MessageCommonData()
    for k in range(0,12):
        if voltage[k,0]<244.8:
            #Q_inv[k,0] = 0.0001
            Aq[k,0]=0
        if voltage[k,0]>=244.8:
            if voltage[k,0]<250.08:
                #Q_inv[k,0] = 1438.0*(voltage[k][0]-250.08)
                Aq[k,0]=mq*voltage[k,0]-mq*V_criq[k,0]-Qabsorb[k,0]
        if voltage[k,0]>=250.08:
            A[k,0]=mp*voltage[k,0]-mp*V_cri[k,0]-Pcurtail[k,0]-mp*(addp[k,0])/10000
            #Q_inv[k,0] = 2761.0
            #Aq[k,0]=mq*voltage[k,0]-mq*V_criq[k,0]-Qabsorb[k,0]
            Aq[k,0] = 0
        else:
            A[k,0] = 0
    X=B_inv*A
    Xq = Bq_inv*Aq
    X=X/5
    Xq = Xq/5
    Final_power=[]
    for i,n in enumerate(HOUSES):
        inverter_power = change_power(X[i,0],i)
        inverter_re_power = change_repower(Xq[i,0],i)
        #s_inv = complex(PMPPT+LOAD[i],inverter_re_power)
        s_inv = complex(inverter_power,inverter_re_power)
        Final_power.append(s_inv)
        transfer.add_param(CommonParam(name=n,param='constant_power_A',value = s_inv+LOAD[i]))
    return transfer

def get_message_final(LOAD):

    global Final_power
    global Display

    transfer = MessageCommonData()
    
    for i,n in enumerate(HOUSES):
        transfer.add_param(CommonParam(name=n,param='constant_power_A',value=(Final_power[i]+LOAD[i])))
        
    return transfer

    
Display = 0
##ermax_list12 = []
##ermax_list11 = []
##ermax_list10 = []
##ermax_list9 = []
##ermax_list8 = []
##ermax_list7 = []
##ermax_list6 = []
##ermax_list5 = []
##ermax_list4 = []
##ermax_list3 = []
##ermax_list2 = []
##ermax_list1 = []
##curtailment = []
##reactive_absorption = []


##voltage_prev_12 = 240
##voltage_prev_11 = 240
##voltage_prev_10 = 240
##voltage_prev_9 = 240
##voltage_prev_8 = 240
##voltage_prev_7 = 240
##voltage_prev_6 = 240
##voltage_prev_5 = 240
##voltage_prev_4 = 240
##voltage_prev_3 = 240
##voltage_prev_2 = 240
##voltage_prev_1 = 240

with open_bus(BUS_FILE_MAIN) as bus_MAIN:
    with open_bus(BUS_FILE_ITER) as bus_ITER:
        while not bus_MAIN.finished:
            
            Display=Display+1
            
            if Display==10000:
                print '10000'
            if Display==100000:
                print '100000'
            if Display==200000:
                print '200000'
            if Display==300000:
                print '300000'
            if Display==400000:
                print '400000'
            if Display==500000:
                print '500000'
            if Display==525500:
                print '525500'
            
            PMPPT=(0- DATA_FRAME[0][current_time])
            
            LOAD_current_time=[]
##            er12 =[]
##            er11 = []
##            er10 = []
##            er9 = []
##            er8 = []
##            er7 = []
##            er6 =[]
##            er5 = []
##            er4 = []
##            er3 = []
##            er2 = []
##            er1 = []
##            ermax = []
            
            for i in range(1,13):
                LOAD_current_time.append(( DATA_FRAME[i][current_time]))
                
            current_time += pd.to_timedelta('%s s' % (60.0))
            if PMPPT<-0.01:                
                for ite_loop in range(0,10):
                    
                    result = bus_ITER.transaction(inputs=get_message(LOAD_current_time))
                    for z,n in enumerate(HOUSES):
                        voltage[z,0]=round(abs(result.get_param(n,"measured_voltage_A").value),3)
##                        if z == 11:
##                            er12.append(voltage[z,0]-voltage_prev_12)
##                            voltage_prev_12 = voltage[z,0]
##                        if z == 10:
##                            er11.append(voltage[z,0]-voltage_prev_11)
##                            voltage_prev_11 = voltage[z,0]
##                        if z == 9:
##                            er10.append(voltage[z,0]-voltage_prev_10)
##                            voltage_prev_10 = voltage[z,0]
##                        if z == 8:
##                            er9.append(voltage[z,0]-voltage_prev_9)
##                            voltage_prev_9 = voltage[z,0]
##                        if z == 7:
##                            er8.append(voltage[z,0]-voltage_prev_8)
##                            voltage_prev_8 = voltage[z,0]
##                        if z == 6:
##                            er7.append(voltage[z,0]-voltage_prev_7)
##                            voltage_prev_7 = voltage[z,0]
##                        if z == 5:
##                            er6.append(voltage[z,0]-voltage_prev_6)
##                            voltage_prev_6 = voltage[z,0]
##                        if z == 4:
##                            er5.append(voltage[z,0]-voltage_prev_5)
##                            voltage_prev_5 = voltage[z,0]
##                        if z == 3:
##                            er4.append(voltage[z,0]-voltage_prev_4)
##                            voltage_prev_4 = voltage[z,0]
##                        if z == 2:
##                            er3.append(voltage[z,0]-voltage_prev_3)
##                            voltage_prev_3 = voltage[z,0]
##                        if z == 1:
##                            er2.append(voltage[z,0]-voltage_prev_2)
##                            voltage_prev_2 = voltage[z,0]
##                        if z == 0:
##                            er1.append(voltage[z,0]-voltage_prev_1)
##                            voltage_prev_1 = voltage[z,0]
                        
##                ermax_list12.append(er12)
##                ermax_list11.append(er11)
##                ermax_list10.append(er10)
##                ermax_list9.append(er9)
##                ermax_list8.append(er8)
##                ermax_list7.append(er7)
##                ermax_list6.append(er12)
##                ermax_list5.append(er11)
##                ermax_list4.append(er10)
##                ermax_list3.append(er9)
##                ermax_list2.append(er8)
##                ermax_list1.append(er7)
                        
                result = bus_MAIN.transaction(inputs=get_message_final(LOAD_current_time))

                for z,n in enumerate(HOUSES):
                    voltage[z,0]=round(abs(result.get_param(n,"measured_voltage_A").value),3)                  

            if PMPPT>=-0.01:
                Final_power=[]
                for i in range(0,12):
                    Final_power.append(PMPPT)                                
                result = bus_MAIN.transaction(inputs=get_message_final(LOAD_current_time))
                for z,n in enumerate(HOUSES):
                    voltage[z,0]=round(abs(result.get_param(n,"measured_voltage_A").value),3)

            #curt = []
            #react = []
            #for i in range(0,12):
                #bb = Final_power[i]
                #curt.append(bb.real-PMPPT)
                #react.append(bb.imag)

            #curtailment.append(curt)
            #reactive_absorption.append(react)


##ermax_list12 = pd.DataFrame(ermax_list12)            
##ermax_list11 = pd.DataFrame(ermax_list11)
##ermax_list10 = pd.DataFrame(ermax_list10)
##ermax_list9 = pd.DataFrame(ermax_list9)
##ermax_list8 = pd.DataFrame(ermax_list8)
##ermax_list7 = pd.DataFrame(ermax_list7)
##ermax_list6 = pd.DataFrame(ermax_list12)            
##ermax_list5 = pd.DataFrame(ermax_list11)
##ermax_list4 = pd.DataFrame(ermax_list10)
##ermax_list3 = pd.DataFrame(ermax_list9)
##ermax_list2 = pd.DataFrame(ermax_list8)
##ermax_list1 = pd.DataFrame(ermax_list7)
#curtailment = pd.DataFrame(curtailment)
#reactive_absorption = pd.DataFrame(reactive_absorption)


##ermax_list12.to_csv('Error_list12.csv')
##ermax_list11.to_csv('Error_list11.csv')
##ermax_list10.to_csv('Error_list10.csv')
##ermax_list9.to_csv('Error_list9.csv')
##ermax_list8.to_csv('Error_list8.csv')
##ermax_list7.to_csv('Error_list7.csv')
##ermax_list6.to_csv('Error_list6.csv')
##ermax_list5.to_csv('Error_list5.csv')
##ermax_list4.to_csv('Error_list4.csv')
##ermax_list3.to_csv('Error_list3.csv')
##ermax_list2.to_csv('Error_list2.csv')
##ermax_list1.to_csv('Error_list1.csv')
#curtailment.to_csv('Curtailment.csv')
#reactive_absorption.to_csv('reactive_absorption.csv')

             
print 'bus finished'


