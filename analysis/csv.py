import os
import logging as lg

lg.basicConfig(level=lg.DEBUG)

def launch_analysis(data_file):
    directory = os.path.dirname(os.path.dirname(__file__))
    path_to_file = os.path.join(directory, "data", data_file)
    
    try:
        with open(path_to_file, 'r') as f:
            preview = f.readline()
            lg.debug("Yeah we managed to read the file this is ze preview bro : {}".format(preview))
    except FileNotFoundError as e:
        lg.critical('Oh :(The file was not found sorry... Here is the message : )'.format(e))

def main():
    launch_analysis('current_mps.csv')

if __name__ == "__main__":
    launch_analysis('current_mps.csv')
