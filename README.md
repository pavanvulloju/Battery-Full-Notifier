# Battery-Full-Notifier
A Script that Notifies the user when a required level is reached while Charging the PC/Laptop


## Folder Structure
```
📦BatteryNotification
 ┣ 📂venv
 ┣ 📜app.py
 ┣ 📜mybattery.bat
 ┗ 📜charge.vbs
 ```

## Step 1: Create a Virtual Environment (venv)

create a virtual environment inside any folder and place the app.py with venv folder

## Step 2: Create a <b>.bat</b> file

create a ```.bat``` file with the code as below with any name. (eg. <i>mybattery.bat</i> )
```bat

@echo off
"PYTHON_EXE_PATH"
"APP.PY_PATH"
exit

```
Here replace PYTHON_EXE_PATH with python exe path inside venv and replace APP.PY_PATH with app.py path 

- (Eg. replace `PYTHON_EXE_PATH` with "C:\Users\<username>\Desktop\Python_Projects\BatteryNotification\venv\Scripts\python.exe" )


- (Eg. replace `APP.PY_PATH` with C:\Users\<username>\Desktop\Python_Projects\BatteryNotification\app.py )

## Step 3: Create a .vbs file as shown below 
Create a vbs file in the same directory with the below code inside it.(Eg. charge.vbs)

This file is needed to make the hovering cmd screen on desktop to disappear.

```vbs
CreateObject("Wscript.Shell").Run "BAT_FILE_PATH", 0, True
```

Replace the BAT_FILE_PATH with the path of bat file inside the vbs file.

- (Eg. replace `BAT_FILE_PATH` with "C:\Users\<username>\Desktop\Python_Projects\BatteryNotification\mybattery.bat" )


## Step 4: Create a shortcut for the .vbs
Create a shortcut for the .vbs file and place it inside the below mentioned path.

`C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp`

---

So whenever you power on your PC/Laptop, app.py with be running in the background and notifies you whenever the battery if Full.
