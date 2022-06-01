# pyVideoSDK-Demo
Python code examples that use TrueConf VideoSDK API and TrueConf Room API

## How to use

### Download and install TrueConf Room

   1. [Download TrueConf Room](https://github.com/TrueConf/pyVideoSDK/blob/main/download.md)
   1. Install with default settigs (Port = 80)
   1. Launch application c **-pin** parameter in the command line. Example:
   ```
   "C:\Program Files\TrueConf\Room\TrueConfRoom.exe" -pin "pin123"
   ```

### Login

   1. Get your free accounts in https://t.me/TrueConfSDKPromoBot
   1. Click at the link on the application main screen and open the **web-manager**
   1. Connect to the server and login in

**Now the application is ready to use**   

## Preparing the python environment

### Clone the repository including submodules

```
git clone --recurse-submodules https://github.com/TrueConf/pyVideoSDK-Demo.git
```

### Install the required modules

```bash
# Change the current directory
cd pyVideoSDK-Demo
```

```bash
# Install the required modules
pip install -r requirements.txt
```

### Fix the config.py file if need it

💡 If you run the application and a python script on the same computer then to fix the _"config.py"_ is not required.

```python
IP = "127.0.0.1"
PORT = 80
PIN = "pin123"
DEBUG = False
```

## Run "connect-to-server-and-login.py"

Modify lines below in _"connect-to-server-and-login.py"_ by your data that received from the https://t.me/TrueConfSDKPromoBot:


```python
...
TRUECONF_SERVER = "<Server IP>"
TRUECONF_ID = "<trueconf_id>"
PASSWORD = "<password>"
...
```

💡 How can I find of my data for connection and authorization?

![get-free-accounts-bot](https://user-images.githubusercontent.com/33928051/171378668-096026ee-356c-477e-95f4-2cac2fcf9679.png)

### After running the script, you will see something like this:

![connect-to-server-and-login-console](https://user-images.githubusercontent.com/33928051/171176897-5401a223-66af-4558-a151-15a46bddf189.png)


