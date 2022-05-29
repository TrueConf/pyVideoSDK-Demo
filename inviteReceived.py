# coding=utf8
'''''
@author: zobov

Example: 
    Processing of the invite received.

'''

import pyVideoSDK
from pyVideoSDK.methods import Methods
from pyVideoSDK.consts import EVENT, METHOD_RESPONSE
import pyVideoSDK.consts as C
import config

sdk = pyVideoSDK.open_session(ip = config.IP, port = config.PORT, pin = config.PIN, debug = config.DEBUG)
methods = Methods(sdk)

@sdk.handler(EVENT[C.EV_appStateChanged])
@sdk.handler(METHOD_RESPONSE[C.M_getAppState])
def on_state_change(response):
    print(f'    @@@ {response["appState"]}')

@sdk.handler(EVENT[C.EV_inviteReceived])
def on_invite(response):
    print('Incoming call:')
    print(f'             Type: {response["type"]}')
    print(f'             From: {response["peerId"]}')
    print(f'             Name: {response["peerDn"]}')
    print(f'    Conference ID: {response["confId"]}\n')
    # Ask
    if input("Accept incoming? (y/n): ").lower() == "y":
        # Accept
        methods.accept()
        print("Call accepted.")
    else:
        methods.reject()
        print("Call rejected.")

if __name__ == '__main__':
    sdk.run()