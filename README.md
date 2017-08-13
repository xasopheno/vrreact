## Breathing Game
Let's trying making a thing.

Currently:
A ReactNative app connects to a Python3 server serving random numbers to websocket
and displays those numbers in a View.

## Installation
Start the Server and then connect to it with the ReactNative app.

### Server
Python3

pip3 install asyncio
(I'll set up a virtualenv at some point)

python3 src/Server/Server.py

####/Notes
Not totally sure, but something after Python3.5 should be ok. 
Won't run with python2 (python), because of the async stuff. 

Python, because I've done all my dsp stuff in Python and it has great data science and mathematics libraries.
It also means I'll be able to reuse some code from music stuff for making simple seeds out of streaming data.
### Client
ReactNative.

npm install
react-native run-ios

-- or --

react-native run-android

####/Notes
I have a nice workflow in the iOS simulator, so that's probably where I'll be developing. 
react-native run-android in the simulator is difficult, but on the device is super easy. 
If we need to specifically target Android phones, let me know. All said, should work well on both devices.

## Tests
We definitely need tests. That should actually be our next meeting. 
Let's figure out which tests this would need to pass to work.
Then build those tests and the required components.

## Contributors

Danny and Martha. What goes here?

## License
What should go here?
