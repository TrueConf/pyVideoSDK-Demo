'''
@author: Andrey Zobov

Example: get the list of hardware.
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

@sdk.handler(METHOD[C.M_getHardware])
def on_get_hardware(response):
    print('==============================================')
    print('Hadrware list:')
    print('==============================================')
    print(f'{response}')
    print('==============================================')

'''
@sdk.handler({})
def on_all(response):
    print(f'    @@@ {response}')
'''

if __name__ == '__main__':
    methods.getHardware()
    sdk.run()