# Mini Project 2.0 - Software and Automation Frameworks

**Aalborg University - 5th Semester Robotics 2021**

This is a revised version of the SAF Mini Project. Comments and some code has been re-written.

The system consists of two main programs;
- A PLC operating program (**TCP CLIENT**) <-- Written in ST
- A PC operating program (**TCP SERVER**) <-- Written in Python

A video showing what is going on --> https://www.youtube.com/shorts/YcugWAWQTyA

![ezgif-2-7454e1afb4](https://user-images.githubusercontent.com/72069575/147881400-cdd35e56-2063-4b6f-92cc-17aff5f12d2c.gif)

### TODO

To finish this mini project the following elements has to be completed:

- [x] Create mini project repository document
- [x] Gather information about system
- [x] Create programs for both PC and PLC
- [x] Conduct tests physically
- [x] Begin writing report document
- [x] Check and finish report

- [x] All tasks are complete :tada:

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
2. Send the RFID info to a PC via TCP/IP as a byte-string. 
3. The PC program shall decode the information and display the ‘CarrierID’ in a GUI. 
4. The PLC shall then perform a safety check, to ensure that a bottom cover is ready for processing.
5. The PLC shall then send the starting time and date to the PC via TCP/IP as a byte string.
6. The PLC shall then perform the process of drilling/stamping four holes.
7. The PLC shall then send the ending time and date to the PC via TCP/IP as a byte string.
8. The PC program shall decode the information and display the starting time and date, and then release the pallet.
9. The PC program shall calculate and display the used process time.
10. The decoded data shall be stored in a file on the PC, so that it can be analyzed later.

## Useful pictures...

**Variables used in PLC program**

![VARSetupCode](https://user-images.githubusercontent.com/72069575/147881694-e9d841e8-7929-4d88-8fb0-98a0b64cc1c8.PNG)

**Variables used for sensors and actuators**

![VARSetup](https://user-images.githubusercontent.com/72069575/147881751-94eb8628-d979-4add-a781-10a65ab4ad36.PNG)

**Setup in CODESYS**

![DeviceSetup](https://user-images.githubusercontent.com/72069575/147881772-3d5f8c20-f7b1-415a-859e-f15bf6441658.PNG)


