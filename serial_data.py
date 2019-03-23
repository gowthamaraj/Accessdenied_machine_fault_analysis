import serial


from influxdb import InfluxDBClient

client = InfluxDBClient(host='localhost', port=8086)


client.switch_database('network')



ser = serial.Serial('COM3',9600,timeout=1)

while(1):
    t1=int(ser.readline().decode('ascii'))
    t2=int(ser.readline().decode('ascii'))       
    json_body = [
    {
    "measurement": "access_denied",
    "tags": {
    "user": "data",
    },
    "fields": {
    "sound": t1, 
    "vibs": t2,    
    }
    }
    ]
    client.write_points(json_body)