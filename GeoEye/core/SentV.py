import serial
import requests

# Replace 'COMx' with your Arduino port
ser = serial.Serial('COMx', 9600)

# Replace with your Django server URL
django_server_url = 'http://localhost:8000/receive_voltage_data/'

while True:
    line = ser.readline().decode('utf-8').strip()

    if line.startswith("DATA:"):
        voltage = float(line[5:])
        print("Received Voltage:", voltage)

        # Send voltage data to Django server
        response = requests.post(django_server_url, data={'voltage': voltage})

        if response.status_code == 200:
            print("Voltage data sent to Django successfully.")
        else:
            print("Failed to send voltage data to Django. Status Code:", response.status_code)
