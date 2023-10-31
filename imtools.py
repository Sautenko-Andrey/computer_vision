import os

def get_imlist(path:str) -> list:
    '''Returns names list of all jpg-files
    within catalog'''

    return [os.path.join(path,f) for f in os.listdir(path) if f.endswith(".jpg")]