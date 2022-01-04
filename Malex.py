import os
import time

global exe_files
global failcount
global succeedcount
global disr_list

failcount = 0
succeedcount = 0

DIRECTORY_PATH = "C:\\Users\\Spinach\\Downloads\\Malware"
FILE_EXTENSION = "exe"

def execute(path, file_extension):
    abort = input("This is your last chance. This tool will run all the files on your system which may damage your system. Abort? Y/N: ").lower()
    while abort not in ['y','n']:
        print("Enter a valid option.")
        abort = input("This is your last chance. This tool will run all the files on your system which may damage your system. Abort? Y/N: ").lower()
    if abort == "y":
        quit("Aborting!")
    else:
        print("Not aborting.")

    disr_list = os.listdir(path)
    exe_files = []
    for file in disr_list:
        if file.endswith(f".{file_extension}"):
            exe_files.append(file)
    
    for exe_file in exe_files:
        exe_file = exe_file.replace(" ", "")
        os.startfile(f"\"{exe_file}\"")
        print(f"Ran \"{exe_file}\"")
        print("Sleeping 2 seconds for memory check...")
        time.sleep(2)
        # check if the file has loaded into memory and if hasn't, increment
        # failcount by one and if has, incriment succeedcount by one
    # print(f"The malware has failed executing {str(failcount)} times.")
    # input(f"The malware has succeeded executing {str(succeedcount)} times.\n")

execute(DIRECTORY_PATH, FILE_EXTENSION)