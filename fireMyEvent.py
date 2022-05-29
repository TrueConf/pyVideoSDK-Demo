'''''
@author: zobov

Example: 
    Fire a custom event through VideoSDK or Room

API Version: 4.1.0+

'''

import config
import pyVideoSDK
from pyVideoSDK.methods import Methods
from pyVideoSDK.consts import EVENT, METHOD_RESPONSE
import pyVideoSDK.consts as C
from pprint import pprint

print(__doc__)

sdk = pyVideoSDK.open_session(ip = config.IP, port = config.PORT, pin = config.PIN, debug = config.DEBUG)
methods = Methods(sdk)

@sdk.handler(EVENT[C.EV_appStateChanged])
@sdk.handler(METHOD_RESPONSE[C.M_getAppState])
def on_state_change(response):
    print(f'    Application state is {response["appState"]}')

@sdk.handler(METHOD_RESPONSE[C.M_fireMyEvent])
def on_fire_my_event_result(response):
    print("    Method call result:")
    pprint(response)

@sdk.handler(EVENT[C.EV_myEvent])
def on_my_event(response):
    print("    Event:")
    pprint(response)

if __name__ == '__main__':
    methods.fireMyEvent("hello_world_event")
    sdk.run()