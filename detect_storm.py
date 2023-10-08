###
###
### detect_storm.py - This script calculates average magnetic field magnitudes for one hour intervals. Takes 'result.csv' which consists of columns:
### year,doy,h,m,velocity,density,temperature,minutes,magnitude
### respectively.
###
###

data_fd = open('result.csv','r')
data = data_fd.readlines()[1:]

report = open('report.csv','w')

head=0
tail=0

while tail < len(data):
    
    avg = 0
    x=0
    while tail < len(data) and int(data[tail].strip().split(',')[-2].strip('"')) - int(data[head].strip().split(',')[-2].strip('"')) <= 60:
        
        avg += float(data[tail].split(',')[-1].strip('"'))
        tail += 1
        x+=1
        
    avg = avg/x
    print(avg)
    report.write(','.join(data[head].strip().split(',')[:4]) + f',"{avg}"' + "\n")
    
    head = tail
    
report.close()
