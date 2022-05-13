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

@sdk.handler(EVENT[C.EV_rejectReceived])
def on_reject(response):
    print('Reject received')
    print(f'    Cause: {response["cause"]}')
    print(f'           {C.CAUSE[response["cause"]]}')

'''
@sdk.handler({})
def on_all(response):
    print(f'    @@@ {response}')
'''

if __name__ == '__main__':
    methods.call("echotest@trueconf.com")
    sdk.run()