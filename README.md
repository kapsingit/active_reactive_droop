# active_reactive_droop

Implements reactive droop from 1.02 pu to 1.042 pu followed by active power droop starting from 1.042 pu to 1.058 pu. This controller is implemented in 12  house test case system. The model is in .glm file. The simulation is performed for a year 2014 in a minute resolution. The load and PV power data are stored present csv file for a year in a minute resolution. Note first column is date, second column is solar available power which is assumed to be same for all house. The 3rd to 14th columns store individual load data for 12 houses.


