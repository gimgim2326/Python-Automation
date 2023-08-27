import os
import shutil

def get_folders_in_directory(directory_path):
    folder_names = []
    for item in os.listdir(directory_path):
        item_path = os.path.join(directory_path, item)
        if os.path.isdir(item_path):
            folder_names.append(item)
    return folder_names

# Write the name of the directory here,
# that needs to get sorted
path = '/Users/gimsdp/iCloud Docs/video'
target_path = '/Users/gimsdp/Sorted Files'
  
  
# This will create a properly organized 
# list with all the filename that is
# there in the directory
folders = get_folders_in_directory(path)

if folders:
    for folder in folders:
        list_ = os.listdir(path+'/'+folder)
        for file_ in list_:
            name, ext = os.path.splitext(file_)
        
            # This is going to store the extension type
            ext = ext[1:]
        
            # This forces the next iteration,
            # if it is the directory
            if ext == '':
                continue
        
            # This will move the file to the directory
            # where the name 'ext' already exists
            if os.path.exists(target_path+'/'+ext):
                #if ext=='jpg' or ext=="png" or ext=="jpeg" or ext=="JPG" or ext=="PNG" or ext=="JPEG" or ext=="mp4" or ext=="gif" or ext=="GIF" or ext=="MP4" or ext=="MOV" or ext=="mov" or ext=="3gp":
                shutil.move(path+'/'+folder+'/'+file_, target_path+'/'+ext+'/'+file_)
        
            # This will create a new directory,
            # if the directory does not already exist
            else:        
                #if ext=='jpg' or ext=="png" or ext=="jpeg" or ext=="JPG" or ext=="PNG" or ext=="JPEG" or ext=="mp4" or ext=="gif" or ext=="GIF" or ext=="MP4" or ext=="MOV" or ext=="mov"or ext=="3gp":
                os.makedirs(target_path+'/'+ext)
                shutil.move(path+'/'+folder+'/'+file_, target_path+'/'+ext+'/'+file_)


# This will go through each and every file
list_ = os.listdir(path)
for file_ in list_:
        name, ext = os.path.splitext(file_)
    
        # This is going to store the extension type
        ext = ext[1:]
    
        # This forces the next iteration,
        # if it is the directory
        if ext == '':
            continue
    
        # This will move the file to the directory
        # where the name 'ext' already exists
        if os.path.exists(target_path+'/'+ext):
            #if ext=='jpg' or ext=="png" or ext=="jpeg" or ext=="JPG" or ext=="PNG" or ext=="JPEG" or ext=="mp4" or ext=="gif" or ext=="GIF" or ext=="MP4" or ext=="MOV" or ext=="mov" or ext=="3gp":
            shutil.move(path+'/'+file_, target_path+'/'+ext+'/'+file_)
    
        # This will create a new directory,
        # if the directory does not already exist
        else:        
            #if ext=='jpg' or ext=="png" or ext=="jpeg" or ext=="JPG" or ext=="PNG" or ext=="JPEG" or ext=="mp4" or ext=="gif" or ext=="GIF" or ext=="MP4" or ext=="MOV" or ext=="mov" or ext=="3gp":
            os.makedirs(target_path+'/'+ext)
            shutil.move(path+'/'+file_, target_path+'/'+ext+'/'+file_)