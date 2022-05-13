# coding=utf8
'''
@author: Andrey Zobov

Example: Receiving an incoming chat message
'''

import pyVideoSDK
from pyVideoSDK.methods import Methods
from pyVideoSDK.consts import EVENT, METHOD
import pyVideoSDK.consts as C
import config

print(__doc__)

sdk = pyVideoSDK.open_session(ip = config.IP, port = config.PORT, pin = config.PIN, debug = False)
methods = Methods(sdk)

@sdk.handler(EVENT[C.EV_appStateChanged])
@sdk.handler(METHOD[C.M_getAppState])
def on_state_change(response):
    print(f'State changed to: {response["appState"]}')

@sdk.handler(EVENT[C.EV_incomingChatMessage])
def on_chat_massage(response):
    print('Incoming chat message')
    print(f'    From   : {response["peerId"]}')
    print(f'    Message: {response["message"]}')

if __name__ == '__main__':
    print(__doc__)
    sdk.run()