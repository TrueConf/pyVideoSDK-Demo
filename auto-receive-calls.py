# coding=utf8
'''''
@author: zobov
'''

import pyVideoSDK
from pyVideoSDK.methods import Methods
from pyVideoSDK.consts import EVENT, METHOD
import pyVideoSDK.consts as C
import config

sdk = pyVideoSDK.open_session(ip = config.IP, port = config.PORT, pin = config.PIN, debug = False)
methods = Methods(sdk)

@sdk.handler(EVENT[C.EV_appStateChanged])
@sdk.handler(METHOD[C.M_getAppState])
def on_state_change(response):
    print(f'    @@@ {response["appState"]}')

@sdk.handler(EVENT[C.EV_inviteReceived])
def on_invite(response):
    print('Incoming call:')
    print(f'             Type: {response["type"]}')
    print(f'             From: {response["peerId"]}')
    print(f'             Name: {response["peerDn"]}')
    print(f'    Conference ID: {response["confId"]}')
    # Accept all
    methods.accept()

if __name__ == '__main__':
    sdk.run()