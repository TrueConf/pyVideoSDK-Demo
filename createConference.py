# coding=utf8
'''
@author: Andrey Zobov

Example: 
  1. Connect to TrueConf Server.
  2. Authorize on the server.
'''

import pyVideoSDK
from pyVideoSDK.methods import Methods
from pyVideoSDK.consts import EVENT, METHOD_RESPONSE
import pyVideoSDK.consts as C
import config

print(__doc__)

TRUECONF_SERVER = "<Server IP>"
TRUECONF_ID = "<trueconf_id>"
PASSWORD = "<password>"

sdk = pyVideoSDK.open_session(ip = config.IP, port = config.PORT, pin = config.PIN, debug = config.DEBUG)
methods = Methods(sdk)

@sdk.handler(EVENT[C.EV_appStateChanged])
@sdk.handler(METHOD_RESPONSE[C.M_getAppState])
def on_state_change(response):
    print(f'    Application state is {response["appState"]}')
    # Need to login
    if response["appState"] == 2:
        methods.login(TRUECONF_ID, PASSWORD)
    elif response["appState"] == 3:
        # Create a new conference when it's possible: appState is 3
        methods.createConference("My conference title", C.CONFTYPE_symmetric, True, ["kiosk2", "kiosk3"])

'''
@sdk.handler({})
def on_all(response):
    print(f'    @@@ {response}')
'''

if __name__ == '__main__':
    # Try to connect to TrueConf Server
    methods.connectToServer(TRUECONF_SERVER)
    sdk.run()