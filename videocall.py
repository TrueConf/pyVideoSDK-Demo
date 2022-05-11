# coding=utf8
'''''
@author: zobov
'''

import pyVideoSDK
from pyVideoSDK.methods import Methods
import pyVideoSDK.consts

sdk = pyVideoSDK.open_session(ip = "127.0.0.1", port = 4523, pin = "123", debug = False)
methods = Methods(sdk)

@sdk.handler({"event": "appStateChanged", "appState": None})
@sdk.handler({"method": "getAppState", "appState": None})
def on_state_change(response):
    print(f'    @@@ {response["appState"]}')


if __name__ == '__main__':
    methods.call("echotest@trueconf.com")
    sdk.run()
