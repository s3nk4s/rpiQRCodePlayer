import keyboard
from soco import SoCo
import time 

# initialise sonos
livingRoom = SoCo('192.168.1.206')


def setPlaylist(pl):
    print('setting playlist: ' + pl)
    livingRoom.clear_queue()
    pl = livingRoom.get_sonos_playlist_by_attr('title', pl)
    livingRoom.add_to_queue(pl)

def playSonos(key):

    try:

        print('received: ' + str(key))  
        livingRoom.play_from_queue(key)

        print('Playing: ' + livingRoom.get_current_track_info()['artist'] + ':' + livingRoom.get_current_track_info()['title'])

        trackTime = livingRoom.get_current_track_info()['duration']
        trackTime_s = sum(x * int(t) for x, t in zip([3600, 60, 1], trackTime.split(":"))) 

        print('turning off in:' + str(trackTime_s))
        livingRoom.set_sleep_timer(trackTime_s-1)
        #stopSonos()

    except:
        livingRoom.stop()

def stopSonos():
    print('Stopping Sonos...')
    livingRoom.stop()

keyboard.add_hotkey('ctrl+shift+7', lambda: playSonos(0))
keyboard.add_hotkey('ctrl+shift+6', lambda: playSonos(1))
keyboard.add_hotkey('ctrl+shift+5', lambda: playSonos(2))
keyboard.add_hotkey('ctrl+shift+4', lambda: playSonos(3))
keyboard.add_hotkey('ctrl+shift+3', lambda: playSonos(4))
keyboard.add_hotkey('ctrl+shift+2', lambda: playSonos(5))
keyboard.add_hotkey('ctrl+shift+1', lambda: stopSonos())

keyboard.add_hotkey('space', lambda: stopSonos())
keyboard.add_hotkey('enter', lambda: stopSonos())

keyboard.add_hotkey('F1', lambda: setPlaylist('Lena Anglais'))
keyboard.add_hotkey('F2', lambda: setPlaylist('Lena Francais'))
keyboard.add_hotkey('F3', lambda: setPlaylist('Simon'))


print('waiting for input...')
keyboard.wait() 
