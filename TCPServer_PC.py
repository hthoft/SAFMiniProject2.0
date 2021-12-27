import socket
import re
import tkinter as tk
import datetime

root = tk.Tk()
root.title('PLC DATA')
root.geometry('500x200')

canvas = tk.Canvas(root, height=200, width=500)
canvas.pack()

frame = tk.Frame(root, bg='white')
frame.place(relheight=1, relwidth=1)

carrierID = 'none'
carrierTime = 'none'
timeSetup = 0
processTime = 0
processTime1 = 0
processTime2 = 0

label1 = tk.Label(frame, text=carrierID, fg='black', bg='white', font=('Arial', 50, 'bold'))
label1.place(anchor='c', x=250, y=50)

label2 = tk.Label(frame, text=carrierTime, fg='black', bg='white', font=('Arial', 20, 'bold'))
label2.place(anchor='c', x=250, y=110)

label3 = tk.Label(frame, text=processTime, fg='black', bg='white', font=('Arial', 20, 'bold'))
label3.place(anchor='c', x=250, y=150)

root.update()

localIP = "172.20.66.28"
localPort = 65000
bufferSize = 1024
msgFromServer = "Hello UDP Client"
bytesToSend = str.encode(msgFromServer)
# Create a datagram socket, bind to address and ip
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
UDPServerSocket.bind((localIP, localPort))
UDPServerSocket.listen(1)

today = datetime.datetime.now().strftime("%B %d, %Y %H:%M:%S")
file_time = datetime.datetime.now().strftime("%B %d, %Y")

file_name = ("Log: " + file_time[0:8] + " " + file_time[9:11] + file_time[12:17]+ '.txt')


f= open(str(file_name),"w+")

f.write("Date was: " + str(today))
f.write("\n")


while True:
    root.bind('<Escape>', lambda e: root.destroy())
    # Wait for a connection
    print('waiting for a connection')
    connection, client_address = UDPServerSocket.accept()
    print("tcp server up and listening")
    try:
        print('connection from', client_address)
        while True:

            data = connection.recv(4)

            if 'DT#' in str(data):
                date = []
                for i in range(5):
                    date.append(str(data))
                    data = connection.recv(4)
                date.append(str(data))
                date = ''.join(str(e) for e in date)

                carrierTime = str('Time of RFID ') + str(str(date).replace("'", "").replace("b", ""))[3:]

                if timeSetup == 0:
                    start_time = datetime.datetime.now()
                elif timeSetup == 1:
                    end_time = datetime.datetime.now()
                    difference = end_time-start_time
                    processTime = difference
                    print(processTime)
                    label3['text'] = str('Processing Time: ' + str(processTime)[5:-3])



                label1['text'] = str('CarrierID: ' + str(carrierID))
                label2['text'] = carrierTime

                f.write("\n")
                f.write(str('CarrierID: ' + str(carrierID)))
                f.write("\n")
                f.write(carrierTime)
                f.write("\n")
                f.write(str(processTime)[5:-3])
                f.write("\n")


                if timeSetup == 1:
                    timeSetup = -1

                timeSetup += 1

            else:
                print('CarrierID ' + str(data).replace("'", "").replace("b", ""))
                carrierID = int(re.search(r'\d+', str(data)).group())

            root.update()
            if data:
                #print('sending data back to the client')
                connection.sendall(data)
            else:
                print('no more data from', client_address)
                break
    finally:
        # Clean up the connection
        connection.close()
