## Code generated : 8:42 PM, 6/17/2018
## By: Kapil Duwadi, kapil.duwadi@jacks.sdstate.edu


from buspy.bus import open_bus
from buspy.comm.message import CommonParam
from buspy.comm.message import MessageCommonData
import numpy as np

import pandas as pd


START_TIME = pd.to_datetime('2014-06-22 00:00:00') 
END_TIME = pd.to_datetime('2014-06-22 23:59:00') 


df = pd.read_pickle("datasaved.pkl")

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

mp = 4375.0
mq = 1438.0
Qmax = 2761
Q_inv = np.full((12,1),0.0001)
P_inv = np.full((12,1),0.0001)
voltage=np.full((12, 1), 240.0)
V_cri=np.full((12, 1), 252)
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
V_criq = np.full((12, 1), 250.08)
Aq = np.full((12,1),0.0)
Qab = 0
Del_Qab=0
sens_q = sensitivity_q/10000
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
    transfer = MessageCommonData()
    for k in range(0,12):
        if voltage[k,0]<250.08:
            Q_inv[k,0] = 0.0001
        if voltage[k,0]>=250.08:
            if voltage[k,0]<252.0:
                Q_inv[k,0] = 1438.0*(voltage[k][0]-250.08)
        if voltage[k,0]>=252.0:
            Q_inv[k,0] = 2761.0
        P_inv[k,0] = PMPPT
    for i,n in enumerate(HOUSES):
        s_inv = complex(P_inv[i,0],Q_inv[i,0])
        transfer.add_param(CommonParam(name=n,param='constant_power_A',value = s_inv))
    return transfer

def get_message_final(LOAD):

    global Final_power
    global Display

    transfer = MessageCommonData()
    
    for i,n in enumerate(HOUSES):
        transfer.add_param(CommonParam(name=n,param='constant_power_A',value=(Final_power[i]+LOAD[i])))
        
    return transfer

    
Display = 0

with open_bus(BUS_FILE_MAIN) as bus_MAIN:
    with open_bus(BUS_FILE_ITER) as bus_ITER:
        while not bus_MAIN.finished:
            
            Display=Display+1
            
            print Display
            
            PMPPT=(0- DATA_FRAME[0][current_time])
            
            LOAD_current_time=[]
            
            for i in range(1,13):
                LOAD_current_time.append(( DATA_FRAME[i][current_time]))
                
            current_time += pd.to_timedelta('%s s' % (60.0))              
            
            Final_power=[]
            for i in range(0,12):
                Final_power.append(PMPPT)      
            result = bus_ITER.transaction(inputs=get_message_final(LOAD_current_time))
            for z,n in enumerate(HOUSES):
                voltage[z,0]=round(abs(result.get_param(n,"measured_voltage_A").value),3)
                        
            result = bus_MAIN.transaction(inputs=get_message(LOAD_current_time))

            for z,n in enumerate(HOUSES):
                voltage[z,0]=round(abs(result.get_param(n,"measured_voltage_A").value),3)                  
             
print 'bus finished'


