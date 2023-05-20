import numpy as np
import sympy as sym
import matplotlib.pyplot as plt


def estimate(verify_val):
    count1 = float(verify_val[1])
    count2 = float(verify_val[2])
    day1 = int(verify_val[5])
    day2 = int(verify_val[6])
    Age = float(verify_val[3])
    if Age >= 18:
        adult = True
    else:
        adult = False
    power = 3
    day = [1,2,3,4,5,6,7,8,9,10,11]
    Adult = [155,145,110,80,62.5,50,60,80,120,175,280] # Adult data without complications
    child = [218, 200, 168.75, 137.5, 112.5, 106.25, 118.75, 143.75, 181.25, 250, 343.75] # Child data without complications 
    pat_data1 = []
    pat_data2 = []
    if adult == True:
        data = Adult
    else:
        data = child 
    factor1 = count1/data[day1]
    factor2 = count2/data[day2]
    factor = (factor1+factor2)/2
    coefficient = np.polyfit(day,data,power)
    x = sym.Symbol('x')
    d = 0
    e = 0
    f = 0
    g = 0
    h = 0
    i = 0
    j = 0
    k = 0
    if power >= 2:
        a = coefficient[0]
        b = coefficient[1]
        c = coefficient[2]
    if power >= 3:
        d = coefficient[3]
    if power >= 4:
        e = coefficient[4]
    if power >= 5:
        f = coefficient[5]
    if power >= 6:
        g = coefficient[6]
    if power >= 7:
        h = coefficient[7]
    if power >= 8:
        i = coefficient[8]
    if power >= 9:
        j = coefficient[9]
    if power >= 10:
        k = coefficient[10]
    
    p1 = power
    p2 = power-1
    p3 = power-2
    p4 = power-3
    p5 = power-4
    p6 = power-5
    p7 = power-6
    p8 = power-7
    p9 = power-8
    p10 = power-9
    p11 = power-10
    
    model = a*(x**p1)+b*(x**p2)+c*(x**p3)+d*(x**p4)+e*(x**p5)+f*(x**p6)+g*(x**p7)+h*(x**p8)+i*(x**p9)+j*(x**p10)+k*(x**p11)
    P_data1_m = model*factor1
    P_data2_m = model*factor2
    #substitute x in equation model with day2
    P_data1 = list()
    P_data2 = list()
    for n in day:
        P_data1 = (P_data1_m.subs(x,n))
        P_data1 = abs(P_data1)
        if P_data1 > 350:
            P_data1 = 350
        pat_data1.append(P_data1)
        P_data2 = (P_data2_m.subs(x,n))
        P_data2 = abs(P_data2)
        if P_data2 > 350:
            P_data2 = 350
        pat_data2.append(P_data2)
    confidence = 100-((abs(pat_data2[day1]-count1))/count1)*100
    print(confidence)
    results = {0:day,1:data,2:pat_data1,3:pat_data2,4:confidence}
    # plt.plot(day,data, label = 'Data')
    # plt.plot(day,pat_data1, label = 'Patient 1')
    # plt.plot(day,pat_data2, label = 'Patient 2')
    # plt.legend()
    # plt.show()
    return results 

#verify_val = {0:'Name',1:110,2:92,3:20,4:"Date_onset",5:3,6:5}

#Bin = estimate(verify_val)
