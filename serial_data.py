import serial
import matplotlib.pyplot as plt
import numpy as np


from influxdb import InfluxDBClient

#client = InfluxDBClient(host='localhost', port=8086)


#client.switch_database('network')
a=np.array([500])
n=0

ser = serial.Serial('COM3',9600,timeout=1)

while(1):
    t1=int(ser.readline().decode('ascii'))
    a=np.concatenate((a, np.array([t1])))
    t2=int(ser.readline().decode('ascii')) 
    #a=np.concatenate((a, np.array([a[0]])))
    if n==100:
        sp = np.fft.fft(np.sin(a))
        freq = np.fft.fftfreq(a.shape[-1])
        plt.plot(freq, sp.real)
        plt.show()    
    n+=1
    
    #json_body = [ { "measurement": "access_denied", "tags": { "user": "data", }, "fields": { "sound": t1, "vibs": t2, } } ]
    #client.write_points(json_body)