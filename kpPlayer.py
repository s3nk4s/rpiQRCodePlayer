import keyboard
from soco import SoCo
from time import sleep

playlist = {'q':'http://rpi2020.btlan/music/pjonce.mp3',
            't':'http://rpi2020.btlan/music/spToday.mp3',
            'o':'http://rpi2020.btlan/music/o.mp3',
            'd':'http://rpi2020.btlan/music/d.mp3',
            'j':'http://rpi2020.btlan/music/j.mp3',
            'z':'http://rpi2020.btlan/music/z.mp3',
            'b':'http://rpi2020.btlan/music/b.mp3',
            '.':'http://rpi2020.btlan/music/..mp3',
            }

# initialise sonos
livingRoom = SoCo('192.168.1.206')

def playSonos(key):
    print('received: ' + key)
    print('Playing ' + playlist[key])
    #livingRoom.play_uri(playlist[key])

def stopSonos():
    print('Stopping Sonos...')
    livingRoom.stop()

keyboard.add_hotkey('q', lambda: playSonos('q'))
keyboard.add_hotkey('t', lambda: playSonos('t'))
keyboard.add_hotkey('o', lambda: playSonos('o'))
keyboard.add_hotkey('d', lambda: playSonos('d'))
keyboard.add_hotkey('j', lambda: playSonos('j'))
keyboard.add_hotkey('z', lambda: playSonos('z'))
keyboard.add_hotkey('b', lambda: playSonos('b'))
keyboard.add_hotkey('.', lambda: playSonos('.'))

keyboard.add_hotkey('space', lambda: stopSonos())
keyboard.add_hotkey('enter', lambda: stopSonos())

print('waiting for input...')
keyboard.wait()
