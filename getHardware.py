'''
@author: Andrey Zobov

Example: 
    1. Get a list of the hardware.
    2. Close the session.
'''
from pprint import pprint
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

@sdk.handler(METHOD_RESPONSE[C.M_getHardware])
def on_get_hardware(response):
    print('==============================================')
    print('Hadrware list:')
    print('==============================================')
    pprint(response)
    print('==============================================')
    # Close the session
    sdk.close_session()

'''
@sdk.handler({})
def on_all(response):
    print(f'    @@@ {response}')
'''

if __name__ == '__main__':
    methods.getHardware()
    sdk.run()