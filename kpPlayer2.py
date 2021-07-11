import keyboard
from soco import SoCo
from time import sleep

# initialise sonos
livingRoom = SoCo('192.168.1.206')


def setPlaylist(pl):
    print('setting playlist: ' + pl)
    livingRoom.clear_queue()
    pl = livingRoom.get_sonos_playlist_by_attr('title', pl)
    livingRoom.add_to_queue(pl)

def playSonos(key):
    print('received: ' + str(key))  
    livingRoom.play_from_queue(key)
    
def stopSonos():
    print('Stopping Sonos...')
    livingRoom.stop()


keyboard.add_hotkey('F1', lambda: setPlaylist('Lena Anglais'))

keyboard.add_hotkey('q', lambda: playSonos(0))
keyboard.add_hotkey('t', lambda: playSonos(1))
keyboard.add_hotkey('o', lambda: playSonos(2))
keyboard.add_hotkey('d', lambda: playSonos(3))
keyboard.add_hotkey('j', lambda: playSonos(4))
keyboard.add_hotkey('z', lambda: playSonos(5))
keyboard.add_hotkey('b', lambda: playSonos(6))
keyboard.add_hotkey('.', lambda: playSonos(7))

keyboard.add_hotkey('space', lambda: stopSonos())
keyboard.add_hotkey('enter', lambda: stopSonos())

print('waiting for input...')
keyboard.wait()

