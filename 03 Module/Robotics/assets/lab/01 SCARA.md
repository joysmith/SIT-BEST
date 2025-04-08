### How to switch ON SCARA

1. Mains power supply on from wall
2. **SCARA robo station** switch on by rotating selector switch
3. Release emergency switch from following place
   - **Teaching Pendant**
   - **SCARA Traning cell**
   - **IIoT Based HMI**
   - **CCU** wait for 2 min, then press reset button
4. **IIoT Based HMI Interface**
   - double click/touch "Request IIoT HMI access"
   - Rotate "Red know"-selector switch to right side allow IIoT access
   -
5. **SCARA Training Cell** manually set
   - single block: rotate "selector switch" left side
   - single station: rotate "selector switch" left side
6. **Teaching Pendant**
   - Teach button on (white light will glow)
   - Press "Jog" button
   - Hold safety switch lightly
   - press "servo" on
   - press: -x, x, -y, y, -z, z ...
   - Safety switch release, press function button then f2 to close and move to home screen

<br>
<br>

### How to switch OFF SCARA

Perform the Start step in reverse order

<br>
<br>

### How to Operate SCARA in JOG mode -Manual

1. **Teaching Pendant**
   - Teach button on (white light will glow)
   - Press "Jog" button
   - Hold safety switch lightly
   - press "servo" on
   - press: -x, x, -y, y, -z, z ...
   - Safety switch release, press function button then f2 to close and move to home screen

<br>
<br>

### How to run SCARA Homing program -Manual

#### Option 1

1. **Pendant**
   - press "character" button
   - use direction key: select "file/edit"
   - Press "exe"-green button
   - use direction key: select "MOV PHOME" or HOME
   - press "Function key" 2x times to change menu option
   - press "F2" button for "change option" select
   - press safety switch & hold
   - press "servo" button
   - Hold "F1" button for "IMOVE" option

#### Option 2

1. **Pendant**
   - press "Character" --> RUN
   - press "EXE"-green button
2. Navigate by using direction key--> "OPERATION"
   - press "EXE"
3. press F4 "Choose"
4. File name "HOME"
5. Make sure reset is 001
6. off teach button, and in **_CCU_** select:multi station. multi cycle
7. servo on
8. press "F1"
