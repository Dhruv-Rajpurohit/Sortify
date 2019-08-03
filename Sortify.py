import os, shutil
dict_extensions = {
    'audio_extentions' : ('.mp3','.m4a','.wav','.flac'),
    'video_extentions' : ('mp4','.mkv','.MKV',',mpeg'),
    'documents_extentions' : ('.doc','.pdf','.txt'),
}


folderpath = input('Type Folder Path: ')

def file_finder(folder_path, file_extentions):
    files = []
    for file in os.listdir(folder_path):
        for extension in file_extentions:
            if file.endswith(extension):
                files.append(file)
    return files

# print(file_finder(folderpath, video_extentions))
for extension_type, extension_tuple in dict_extensions.items():
    folder_name = extension_type.split('_')[0] + 'Files'
    folder_path = os.path.join(folderpath, folder_name)
    os.mkdir(folder_path)
    for item in file_finder(folderpath, extension_tuple):
        item_path = os.path.join(folderpath,item)
        new_path = os.path.join(folder_path,item)
        shutil.move(item_path,new_path)
    
