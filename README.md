# R0B0
R0B0
An assistant that does the boring stuff on your computer and keeps you entertained.
## How to install it:
### 1. Download Python (if you don't have it installed). 
* **For Windows:** go to the official site (python.org),download the latest stable version,double click the downloaded file,select "add python.exe to path" then click on "install now".
* **For macOS:** go to the python page for mac and download the universal installer, open the installer and follow the universal steps of installation pressing "continue".
* **For Linux:** the majority of distributions have python preinstalled. To update or install the newest version, run these commands on your terminal:
   ``` bash
   sudo apt update
   sudo apt install python3 python3-pip
   ```
  **How to verify the installation:**
   Open Command Prompt(Windows) or Terminal(mac and Linux) then type the following command and press enter:
   ``` bash
   python --version
   ```
    *(on mac or linux, you might need to type `python3 --version` instead).If successful, it will display the installed version.*
### 2. Download the libraries.
In Python, some libraries are preinstalled, but others aren't. So type this command on your terminal:
``` bash
pip install pyttsx3 sounddevice scipy wikipedia pyjokes simpleeval SpeechRecognition
```
### 3. Run the code.
Copy the code from `R0B0.py` and save it into a file named `main.py` or any name ending in .py, open your terminal, navigate to the folder where you saved the file using the command `cd` (e.g: `cd myfolder`) then run the script using Python 
```bash
python main.py
```
## Here are some R0B0's features:
* making folders
* searching on wikipedia
* telling jokes
* searching on Youtube
* opening Chrome
* opening Task Manager
## How to use it:
R0B0 works on vocal command and is always listening, so the wake word is **rocket assistant**.
After telling the wake word wait R0B0 to acknowledge it(he will say **I'm listening**), then wait 1 or 2 seconds and tell your command.
**Note**: Make sure your microphone is connected and set as default recording device in your system settings.
### Terminal Preview 
Here is how your terminal should look after a conversation with R0B0:
<img width="1587" height="906" alt="Capture" src="https://github.com/user-attachments/assets/76802e03-e58a-49af-92de-7d522cd45e5e" />
