
    #In same WatchDog.Py program ,if file with same name exists , it should rename the file by appending a random number

import os
import shutil
import time
import random

# filesystemeventhandler  observer class of watchdog module
# look for changes in the path mentioned, and calls the specific event handler

from watchdog.observers import Observer 
# event handler class that manages the file system events(eg creation, movement, deletion)
from watchdog.events import FileSystemEventHandler



# paths

from_dir ="c:/Users/HP EliteBook 840 G4/Downloads"
to_dir="C:/Users/HP EliteBook 840 G4/BlockVerse Assignments/PYTEST"


dir_tree={
    "Image_files":[".jpg",".jpeg",".png"],
    "Video_files":[".mp4",".mp3",".mov"],
    "Document_files":[".ppt",".csv",".pdf"]
}

# Creating class FileMovementHandler and pass FileSystemEventHandler as parameter to use all the methods and attributes from FileSystemEventHandler inside FileMovementHandler
class FileMovementHandler(FileSystemEventHandler):

    def on_created(self, event):
        name,extension=os.path.splitext(event.src_path)

        time.sleep(1)
        for key, value in dir_tree.items():
            time.sleep(1)
            if extension in value:
                file_name=os.path.basename (event.src_path)
                print("Downloaded"+file_name)

                path1= from_dir+ '/'+file_name
                path2=to_dir+'/'+key
                path3=to_dir + '/'+key +'/'+file_name

                if os.path.exists(path2):
                    print("Directory exists..")


                    # Check if the file with the same name exists in the destination
                    if os.path.exists(path3):
                        # Generate a new filename with a random number appended before the extension
                        random_number = str(random.randint(1000, 9999))
                        new_file_name = os.path.splitext(file_name)[0] + "_" + random_number + extension
                        path3 = to_dir + '/' + key + '/' + new_file_name
                        print(f"File with the same name exists, renaming to {new_file_name}")
                        
                    print("moving"+ file_name+ "...")
                    shutil.move(path1,path3)
                    time.sleep(1)
                else:
                  print("Making Directory..")
                  os.makedirs(path2)
                  print("Moving"+file_name+ "...")
                  shutil.move(path1,path3)
                  time.sleep(1)

  # intialize event handler class                
event_handler = FileMovementHandler()
observer=Observer()
#recursive=true observe the changes in subfolders as well
observer.schedule(event_handler, from_dir,recursive=True)
observer.start()
try:
    while True:
        time.sleep(2)
        print("running")
except KeyboardInterrupt:
    print("stopped")
    observer.stop()
