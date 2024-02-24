# just place the script into your home (considering you leave your Downloads file in its default place)
# Script for keeping track of a specific folder and move any new files uploaded into it
import sys
import time
import os
import logging

# this module helps with tracking the folder, works woth observer event model
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler

extensions = {
    'documents':['.txt','.pdf','.docx'],
    'images':['.jpg','.jpeg','.png','.bmp'],
    'programs':['.exe','.msi'],
    'videos':['mp4','.mov','.mpeg','.mpg']
}

# possible folders with their own types of files 
# the script will take care of new extensions automatically, just add them to the list 
# if the extension does not exist in our list it will just be added to a new folder
dest_documents = './Downloads/Documents/'
possible_extensions_documents = ['.txt','.pdf','.docx']
dest_images = './Downloads/Images/'
possible_extensions_images = ['.jpg','.jpeg','.png','.bmp']
dest_programs = './Downloads/Programs/'
possible_extensions_programs = ['.exe','.msi']
dest_videos = './Downloads/Videos/'
possible_extensions_videos = ['mp4','.mov','.mpeg','.mpg']
random_extensions = './Downloads/Random/'

class EventHandler(LoggingEventHandler):
    def on_created(self, event):

        # extracting only the file name from the full path name
        file_name = (event.src_path.rsplit('/'))[-1]

        # print(file_name)
        if any (event.src_path.endswith(ext) for ext in possible_extensions_documents):
            os.rename(event.src_path,f'{dest_documents}/{file_name}')
        elif any(event.src_path.endswith(ext) for ext in possible_extensions_images):
             os.rename(event.src_path,f'{dest_images}/{file_name}')
        elif any(event.src_path.endswith(ext) for ext in possible_extensions_programs):
            os.rename(event.src_path,f'{dest_programs}/{file_name}')
        elif any(event.src_path.endswith(ext) for ext in possible_extensions_videos):
            os.rename(event.src_path,f'{dest_videos}/{file_name}')
        else:
            os.rename(event.src_path,f'{random_extensions}/{file_name}')

if __name__ == '__main__':
    
    logging.basicConfig(filename='dev.log',
                        filemode='a',
                        level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    
    # directory or file to be monitored, needs to be set whenever calling the script to run
    path = sys.argv[1] if len(sys.argv) > 1 else '.'

    # possible folders with their own types of files 
    # the script will take care of new extensions automatically, just add them to the list 
    # if the extension does not exist in our list it will just be added to a new folder
    dest_documents = f'./{path}/Documents/'
    possible_extensions_documents = ['.txt','.pdf','.docx']
    dest_images = f'./{path}/Images/'
    possible_extensions_images = ['.jpg','.jpeg','.png','.bmp']
    dest_programs = f'./{path}/Programs/'
    possible_extensions_programs = ['.exe','.msi']
    dest_videos = f'./{path}/Videos/'
    possible_extensions_videos = ['mp4','.mov','.mpeg','.mpg']
    random_extensions = f'./{path}/Random/'

    event_handler = EventHandler()
    observer = Observer()
    observer.schedule(event_handler,path,recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)

    except KeyboardInterrupt:
        observer.stop()
        observer.join()