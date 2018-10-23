Errorlist1 = importfile('Error_list7.csv', 2, 640);
Errorlist2 = importfile('Error_list8.csv', 2, 640);
Errorlist3 = importfile('Error_list9.csv', 2, 640);
Errorlist4 = importfile('Error_list10.csv', 2, 640);
Errorlist5 = importfile('Error_list11.csv', 2, 640);
Errorlist6 = importfile('Error_list12.csv', 2, 640);
Errorlist7 = importfile('Error_list7.csv', 2, 640);
Errorlist8 = importfile('Error_list8.csv', 2, 640);
Errorlist9 = importfile('Error_list9.csv', 2, 640);
Errorlist10 = importfile('Error_list10.csv', 2, 640);
Errorlist11 = importfile('Error_list11.csv', 2, 640);
Errorlist12 = importfile('Error_list12.csv', 2, 640);
curtailment = importfile('Curtailment.csv', 2, 1440);
react_absorb = importfile('reactive_absorption.csv', 2, 1440);

subplot(12,1,1)
plot(Errorlist1')
subplot(12,1,2)
plot(Errorlist2')
subplot(12,1,3)
plot(Errorlist3')
subplot(12,1,4)
plot(Errorlist4')
subplot(12,1,5)
plot(Errorlist5')
subplot(12,1,6)
plot(Errorlist6')
subplot(12,1,7)
plot(Errorlist7')
subplot(12,1,8)
plot(Errorlist8')
subplot(12,1,9)
plot(Errorlist9')
subplot(12,1,10)
plot(Errorlist10')
subplot(12,1,11)
plot(Errorlist11')
subplot(12,1,12)
plot(Errorlist12')

%%
figure
subplot(2,1,1)
plot(curtailment(:,12))
subplot(2,1,2)
plot(react_absorb(:,12))
