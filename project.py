from sharepoint import SharePoint

# set file name
file_name = 'package.txt'

# set the folder name
folder_name = 'data'

# get file
file  = SharePoint().download_file(file_name, folder_name)

# save file
with open(file_name, 'wb') as f:
    f.write(file)
    f.close()