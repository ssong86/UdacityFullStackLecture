import os
def rename_files():
    #1. get the file names from a folder
    file_list = os.listdir(r"/Users/songair/Desktop/UdacityFullStack/Python/alphabet/alphabet2") # this should be changed in windows
                            #r stands for raw, don't interpret any otherway
    print(file_list)
    saved_path = os.getcwd() #cwd = current working directory
    print("Current Working Directory is " + saved_path)
    #os.chdir(rsaved_path)
    os.chdir(r"/Users/songair/Desktop/UdacityFullStack/Python/alphabet/alphabet2")
    #2. for each file, rename filename
    for file_name in file_list:
#        print("Old Name - " +  file_name)
#        print("New Name - " + file_name.translate(None, "0123456789"))
        os.rename(file_name, file_name.translate(None, "0123456789"))
    os.chdir(saved_path)
rename_files()
