import serial
import matplotlib.pyplot as plt
import numpy as np


from influxdb import InfluxDBClient

client = InfluxDBClient(host='localhost', port=8086)


client.switch_database('network')
a=np.array([500])
b=np.array([20])
n=0
mean1=0
mean2=0
rms1=0
rms2=0

ser = serial.Serial('COM3',9600,timeout=1)

while(1):
    t1=int(ser.readline().decode('ascii'))
    mean1+=t1
    rms1+=t1**2
    a=np.concatenate((a, np.array([t1])))
    t2=int(ser.readline().decode('ascii')) 
    mean2+=t2
    rms2+=t2**2
    b=np.concatenate((b, np.array([t2])))
    if n==100:
        sp = np.fft.fft(np.sin(a))
        freq = np.fft.fftfreq(a.shape[-1])
        plt.plot(freq, sp.real)
        plt.show() 
        
        sp = np.fft.fft(np.sin(b))
        freq = np.fft.fftfreq(b.shape[-1])
        plt.plot(freq, sp.real)
        plt.show()    
    n+=1
    mn1 = mean1/n
    rs1=(rms1/n)**(1/2)
    mn2 = mean2/n
    rs2=(rms2/n)**(1/2)
    
    json_body = [ { "measurement": "access_denied", "tags": { "user": "data", }, "fields": { "sound": t1, "vibs": t2,"mean_sound":mn1,"mean_vibs":mn2,"rms_sound":rs1,"rms_vibes":rs2, } } ]
    
    if mn2<=2:
        print("normal")
    else if mn2>=2 and mn2<3:
        print("inner bearing")
        
    else if mn2>=4 and mn2<5:
        print("shaft misalighnment")
        
    else if mn2>=5:
        print("looseness")
        
        
    client.write_points(json_body)