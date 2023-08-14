import math

grade = 3

if grade == 1:
    output = open("doping_of_region_5_linear",'w')
elif grade == 2:
    output = open("doping_of_region_5_exp",'w')
elif grade == 3:
    output = open("doping_of_region_5_square",'w')
elif grade == 4:
    output = open("doping_of_region_5_log",'w')

y_begin = 0.662
y_end = 1.092
y_len = (y_end - y_begin) * 1000 + 1

conc_begin = 5*10**19
conc_end = 1*10**17

if grade == 1:
    for i in range(0, int(y_len)):
        y = y_begin + i * 0.001
        conc = conc_begin + (conc_end - conc_begin)/y_len * i
        if conc > 1*10**19:
            output.write(str(round(y, 3)) + '\t' + str('%20.f' % conc) + '\n')
        elif conc > 1*10**18:
            output.write(str(round(y, 3)) + '\t' + str('%19.f' % conc) + '\n')
        else:
            output.write(str(round(y, 3)) + '\t' + str('%18.f' % conc) + '\n')
elif grade == 2:
    A = math.log(conc_begin/conc_end)/(y_end - y_begin)
    for i in range(0, int(y_len)):
        y = y_begin + i * 0.001
        conc = conc_begin * math.exp(-A * (y - y_begin))
        if conc > 1*10**19:
            output.write(str(round(y, 3)) + '\t' + str('%20.f' % conc) + '\n')
        elif conc > 1*10**18:
            output.write(str(round(y, 3)) + '\t' + str('%19.f' % conc) + '\n')
        else:
            output.write(str(round(y, 3)) + '\t' + str('%18.f' % conc) + '\n')
elif grade == 3:
    A = (conc_begin - conc_end)/(y_end - y_begin)**2
    for i in range(0, int(y_len)):
        y = y_begin + i * 0.001
        conc = conc_begin - A * (y - y_begin)**2
        if conc > 1*10**19:
            output.write(str(round(y, 3)) + '\t' + str('%20.f' % conc) + '\n')
        elif conc > 1*10**18:
            output.write(str(round(y, 3)) + '\t' + str('%19.f' % conc) + '\n')
        else:
            output.write(str(round(y, 3)) + '\t' + str('%18.f' % conc) + '\n')

output.close()