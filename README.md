# Mini Project 2.0 - Software and Automation Frameworks

**Aalborg University - 5th Semester Robotics 2021**

This is a revised version of the SAF Mini Project. Comments and some code has been re-written.

The system consists of two main programs;
- A PLC operating program (**TCP CLIENT**) <-- Written in ST
- A PC operating program (**TCP SERVER**) <-- Written in Python

### TODO

To finish this mini project the following elements has to be completed:

- [x] Create mini project repository document
- [x] Gather information about system
- [x] Create programs for both PC and PLC
- [x] Conduct tests physically
- [x] Begin writing report document
- [ ] Check and finish report

- [ ] All tasks are complete :tada:

## What is going on in general?

The general setup is built upon the AAU Smart Manufacturing Lab, which is sandbox production platform. The task is to have the system move a carriage (or carrier) around on a conveyor. In our case we utilize a production element on top of the conveyor, in this case a drilling process. This drilling process module is shown below;

![image](https://user-images.githubusercontent.com/72069575/147492326-054b4788-44b5-4f3d-a840-c687017fe23d.png)

This module is included with various inputs and outputs, such as optical sensors detecting the positions of a part and pneumatic valves that operate movement of the drillhead. All of these functions are controlled with a PLC. In this case the PLC is a Festo CECC-LK. It is equipped with 12 digital inputs, 8 digital outputs, and 2 fast digital inputs.

![Festo CECC-LK](https://user-images.githubusercontent.com/72069575/147491957-62b63138-e6fc-47c2-83e5-5711a5f14aab.png)

## Project tasks - Official

1. Read the pallet RFID tag when a pallet moves to the module you are working on
2. Send the RFID info to a PC via TCP/IP as an XML-encoded string
3. The PC program shall decode the information and display the relevant information on screen during program execution
4. The PC program shall return an estimated processing time to the PLC via TCP/IP
6. The PLC shall simulate the physical processing time by letting the pallet wait for the returned time.
7. The decoded data shall be stored in a file on the PC, so that it can be analyzed later.

## Project tasks - Revised
1. Read the pallet RFID tag when a pallet moves to the module you are working on
2. Send the RFID info to a PC via TCP/IP as a string
3. The PC program shall decode the information and display the relevant information on screen during program execution
4. The PLC shall initialize the process of drilling holes and send the starting time and date to the PC via TCP/IP.
5. The PLC shall when the process is finished, send the ending time and date to the PC via TCP/IP.
6. The PC program calculates the processing time and shows the relevant information on screen during program execution. 
9. The decoded data shall be stored in a file on the PC, so that it can be analyzed later.
