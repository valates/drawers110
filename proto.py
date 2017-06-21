import sys
from pickleSerializers import save_obj, load_obj

CLOSED = 0
OPEN = 1
#DRAWERS = {1: CLOSED, 2: CLOSED, 3: CLOSED}
#ITEM_MAPS = {}

DRAWER_STATUS_PICKLE_NAME = 'drawermappings'
ITEM_MAP_PICKLE_NAME = 'itemmappings'
try:
    DRAWERS = load_obj(DRAWER_STATUS_PICKLE_NAME)
    ITEM_MAPS = load_obj(ITEM_MAP_PICKLE_NAME)
except:
    DRAWERS = {1: CLOSED, 2: CLOSED, 3: CLOSED}
    ITEM_MAPS = {}

def main(args):
    print("Drawer initialized")
    while (True): #open drawer, close drawer, add item drawer, remove item
        print("\n")
        print(DRAWERS)
        print(ITEM_MAPS)
        commands = input("Enter commmand: ").lower()
        commands = commands.split(" ")
        if (commands[0] == 'open'):
            if (int(commands[1]) in DRAWERS):
                open_drawer(int(commands[1]))
        elif (commands[0] == 'close'):
            if (int(commands[1]) in DRAWERS):
                close_drawer(int(commands[1]))
        elif (commands[0] == 'add'):
            if (int(commands[2]) in DRAWERS):
                #If no drawer specified, pick a random one maybe?
                add_object(commands[1], int(commands[2]))
        elif (commands[0] == 'remove'):
            if (commands[1] in ITEM_MAPS):
                remove_object(commands[1])
        else:
            print('Command entered poorly')

def open_drawer(drawer_number):
    if (DRAWERS[drawer_number] == CLOSED):
        print("Opened drawer " + str(drawer_number))
        DRAWERS[drawer_number] = OPEN
    save_obj(DRAWERS, DRAWER_STATUS_PICKLE_NAME)

def close_drawer(drawer_number):
    if (DRAWERS[drawer_number] == OPEN):
        print("Closed drawer " + str(drawer_number))
        DRAWERS[drawer_number] = CLOSED
    save_obj(DRAWERS, DRAWER_STATUS_PICKLE_NAME)

def add_object(item, drawer):
    open_drawer(drawer)
    ITEM_MAPS[item] = drawer
    save_obj(ITEM_MAPS, ITEM_MAP_PICKLE_NAME)
    close_drawer(drawer)
    print("Added " + item + " to drawer " + str(drawer))

def remove_object(item):
    drawer = ITEM_MAPS[item]
    open_drawer(drawer)
    ITEM_MAPS.pop(item)
    save_obj(ITEM_MAPS, ITEM_MAP_PICKLE_NAME)
    close_drawer(drawer)
    print("Removed " + item + " from drawer " + str(drawer))

if __name__ == '__main__':
    main(sys.argv)