# read this future me: in the github, create recommendations and make the user set default browser as microsoft edge
# and default .bat file as cmd.exe
# basically just dont change default apps
# (this is required)

from os import name, system, listdir, startfile
from time import sleep, perf_counter
from colorama import Fore, init
from pymem import Pymem
from random import choice, randint
from webbrowser import open as link
from psutil import virtual_memory
from subprocess import check_output
import winreg
from threading import Thread
from requests import get


init(convert=True)
thisVersion = 149

def banPrompt():
    system("""mshta javascript:alert(\"You are banned from accessing Malex. \");close();""")
    quit()

def banUser():
    key = winreg.CreateKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\WS")

def unbanUser():
    def deleteSubkey(key0, key1, key2=""):
        if key2=="":
            currentkey = key1
        else:
            currentkey = key1+ "\\" +key2

        open_key = winreg.OpenKey(key0, currentkey ,0,winreg.KEY_ALL_ACCESS)
        infokey = winreg.QueryInfoKey(open_key)
        for x in range(0, infokey[0]):
            subkey = winreg.EnumKey(open_key, 0)
            try:
                winreg.DeleteKey(open_key, subkey)
                print( "Removed %s\\%s " % ( currentkey, subkey))
            except:
                deleteSubkey( key0, currentkey, subkey )

        winreg.DeleteKey(open_key,"")
        open_key.Close()
        return

    deleteSubkey(winreg.HKEY_LOCAL_MACHINE,r'SOFTWARE\Microsoft\WS')

try:
    reg = winreg.ConnectRegistry(None, winreg.HKEY_LOCAL_MACHINE)
    k = winreg.OpenKey(reg,r"SOFTWARE\Microsoft\WS")
    rover = Thread(target=banPrompt)
    rover.start()
    quit()
except Exception as err:
    if isinstance(err, WindowsError):
        pass
    else:
        input(Fore.RED + "Unexpected error: " + str(err))
        quit()
    print(Fore.YELLOW + "User is not banned." + Fore.RESET)

try:
    r = get("https://pastebin.com/raw/Rsr7KGZ0", headers={'user-agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"})
    if (r.status_code != 200):
        print(Fore.YELLOW + "Could not verify if Malex version is updated (you're being forced to exit)")
        print(Fore.YELLOW + "Download an updated version off the Github repo")
        quit()
        while True:
            pass
    latestVersion = int(r.text)
    if (thisVersion != latestVersion):
        input(Fore.YELLOW + "The Malex version you are currently using is outdated. Please check the Malex github repo to get the latest version (you're being forced to exit)\n")
        quit()
    else:
        print(Fore.YELLOW + "Latest version of Malex.")
    Fore.RESET
except Exception as err:
    input(Fore.YELLOW + "Malex could not verify if the version you are using is the latest version. You are forced to exit\n"+str(err))
    quit()

try:
    Fores = [
        Fore.RED,
        Fore.CYAN,
        Fore.GREEN,
        Fore.BLUE,
        Fore.YELLOW,
        Fore.LIGHTCYAN_EX,
        Fore.LIGHTMAGENTA_EX,
        Fore.MAGENTA,
        Fore.LIGHTRED_EX,
        Fore.LIGHTBLUE_EX,
        Fore.LIGHTGREEN_EX,
        Fore.LIGHTYELLOW_EX,
    ]

    _ = open("notblocked.txt", "w")
    _.write("")
    _.close()
    _ = open("blocks.txt", "w")
    _.write("")
    _.close()
    _ = open("information.txt", "w")
    _.write("")
    _.close()
    Malex = """
                    ..          ..            .            .           . . . . . .   .        .
                    . .        . .           . .           .           .              .      .
                    .  .      .  .          .   .          .           .               .    .
                    .   .    .   .         .     .         .           .                 . .
                    .    .  .    .        . . . . .        .           . . . . . .        .
                    .     ..     .       .         .       .           .                 . .
                    .            .      .           .      .           .                .   .
                    .            .     .             .     .           .               .     .
                    .            .    .               .    .           .              .       .
                    .            .   .                 .   . . . . .   . . . . . .   .         .
    """

    def countdown(time_sec):
        while time_sec:
            mins, secs = divmod(time_sec, 60)
            timeformat = "{:02d}:{:02d}".format(mins, secs)
            print(choice(Fores) + timeformat, end="\r")
            sleep(0.05)
            time_sec -= 1

    def processExists(process_name):
        call = "TASKLIST", "/FI", "imagename eq %s" % process_name
        # use buildin check_output right away
        output = check_output(call).decode()
        # check in last line for process name
        last_line = output.strip().split("\r\n")[-1]
        # because Fail message could be translated
        return last_line.lower().startswith(process_name.lower())

    def realCountdown(time_sec):
        while time_sec:
            mins, secs = divmod(time_sec, 60)
            timeformat = "{:02d}:{:02d}".format(mins, secs)
            print(choice(Fores) + timeformat, end="\r")
            sleep(1)
            time_sec -= 1

    def cls():
        if name == "nt":
            system("cls")
        else:
            system("clear")
        print(Fore.RESET + choice(Fores) + Malex + Fore.RESET)

    def effect():
        for i in range(5000):
            print(
                str(
                    choice(
                        [
                            Fore.RED,
                            Fore.GREEN,
                            Fore.MAGENTA,
                            Fore.CYAN,
                            Fore.BLUE,
                            Fore.YELLOW,
                            Fore.LIGHTBLUE_EX,
                            Fore.LIGHTCYAN_EX,
                            Fore.LIGHTGREEN_EX,
                            Fore.LIGHTMAGENTA_EX,
                            Fore.LIGHTRED_EX,
                            Fore.LIGHTYELLOW_EX,
                        ]
                    )
                )
                + str(randint(0, 9)),
                end="",
            )

    system("title Malex by SpinachIsDelicious on Github")

    global exe_files
    global failcount
    global succeedcount
    global disr_list
    global failedMalware
    global succeededMalware
    global dirFiles
    global FILE_EXTENSION
    global DIRECTORY_PATH
    global TERMINATE_AFTER_FINISH
    global theMsg
    global prediction
    global yas

    def execute():
        cls()
        effect()
        cls()
        DIRECTORY_PATH = input(
            Fore.RED + "Input malware folder directory path: " + choice(Fores)
        )
        DIRECTORY_PATH = DIRECTORY_PATH.replace('"', "")
        cls()
        effect()
        cls()
        FILE_EXTENSION = input(
            Fore.RED
            + "Input file extension for malware (just type exe, or type 'all'): "
            + choice(Fores)
        ).lower()

        cls()
        effect()
        cls()
        TERMINATE_AFTER_FINISH = input(
            Fore.RED
            + "Ignore this field. Just press enter (it's only for me, the developer): "
            + choice(Fores)
        )
        cls()
        effect()
        cls()
        if TERMINATE_AFTER_FINISH == "SpinachIsDelicious":
            TERMINATE_AFTER_FINISH = True
        else:
            TERMINATE_AFTER_FINISH = False

        try:
            listdir(DIRECTORY_PATH)
            cls()
            print(Fore.YELLOW + "This tool is by SpinachIsDelicious!")
            sleep(7)
            cls()
            effect()
            cls()
        except:
            cls()
            print(Fore.YELLOW + "Invalid directory path provided." + Fore.RESET)
            sleep(3)
            quit()
        succeededMalware = {}
        failedMalware = {}
        failcount = 0
        succeedcount = 0

        abort = input(
            Fore.RED
            + "This tool will run all the files in the directory provided which may damage your system. Abort? Y/N: "
            + Fore.BLUE
        ).lower()
        while abort not in ["y", "n"]:
            print(Fore.MAGENTA + "Enter a valid option." + Fore.RESET)
            sleep(1)
            cls()
            abort = input(
                Fore.RED
                + "This tool will run all the files on your system which may damage your system. Abort? Y/N: "
                + Fore.BLUE
            ).lower()
        if abort == "y":
            quit(Fore.LIGHTBLUE_EX + "Aborting!")

        print(
            Fore.RED
            + "I am giving you 5 seconds if you want to cancel. I'm not responsible for your actions or any actions that the tool takes upon your system. Press Ctrl + C to exit application"
        )
        realCountdown(5)
        cls()
        effect()
        cls()

        print(Fore.LIGHTBLUE_EX + "Grabbing directory files...", end="")
        disr_list = listdir(DIRECTORY_PATH)
        files = []
        for file in disr_list:
            if FILE_EXTENSION == "all":
                files.append(file)
            else:
                if file.endswith(f".{FILE_EXTENSION}"):
                    files.append(file)
        for file in files:
            if str(file).split('.')[1] != 'exe':
                files.remove(file)
        if len(files) == 0:
            print(
                Fore.YELLOW
                + " >>> Error: No directory files detected matching the file extension. Please make sure configuration is proper."
            )
            sleep(6)
            quit()
        print(Fore.LIGHTYELLOW_EX + " >>> Grabbed" + Fore.RESET)
        sleep(4)
        cls()
        effect()
        cls()
        print(
            Fore.CYAN
            + f"Detected {len(files)} file(s) ending in {FILE_EXTENSION}!"
            + Fore.RESET
        )
        prediction = abs(float(round(len(files) * 0.34 + (len(files) / 15) * 5, 2)))
        print(
            choice(Fores)
            + f"Predicted time of completion: {str(prediction)}"
            + Fore.RESET
        )
        countdown(50)

        cls()
        system(f"taskkill /f /im msedge.exe")
        cls()
        start = perf_counter()
        for exe_file in files:
            while (virtual_memory()[2]) > 95:
                print(
                    Fore.RED
                    + "Virtual memory overloaded. Sleeping 1 second"
                    + Fore.RESET
                )
                sleep(1)
            startfile(f"{DIRECTORY_PATH}\\{exe_file}")
            file = f"DIRECTORY_PATH\\{exe_file}"
            print(Fore.LIGHTMAGENTA_EX + f'Attempted running "{exe_file}"', end="")
            sleep(0.15)
            print(
                Fore.LIGHTCYAN_EX + " >>> Scanning memory for process..." + Fore.RESET,
                end="",
            )
            try:
                if exe_file.split('.')[1] != 'exe':
                    banUser()
                    print(
                        Fore.RED
                        + "\nUser has been banned"
                        + Fore.RESET
                    )
                    input(Fore.YELLOW + "You are forced to exit Malex.")
                    quit()
                Pymem(exe_file)
                succeedcount += 1
                print(Fore.RED + " >>> Not Blocked")
                succeededMalware[exe_file] = str(perf_counter() - start)
            except:
                failcount += 1
                print(Fore.GREEN + " >>> Blocked")
                failedMalware[exe_file] = str(perf_counter() - start)
        end = perf_counter()
        if TERMINATE_AFTER_FINISH:
            for exe_file in files:
                system(f'taskkill /f /im "{exe_file}"')
        time_taken = round(end - start, 2)
        for malware in succeededMalware:
            text = f'{FILE_EXTENSION.capitalize()} file "{str(malware)}" has ran at time {str(round(float(succeededMalware[malware]), 2))} after task start\n'
            _ = open("notblocked.txt", "a")
            _.write(text)
            _.close()
        for malware in failedMalware:
            text = f'{FILE_EXTENSION.capitalize()} file "{str(malware)}" has been blocked at time {str(round(float(succeededMalware[malware]), 2))} after task start\n'
            _ = open("blocks.txt", "a")
            _.write(text)
            _.close()

        print("\n\n")
        if FILE_EXTENSION == "all":
            yas = "all"
        else:
            yas = f"all .{FILE_EXTENSION}"
        if time_taken < prediction:
            print(
                Fore.MAGENTA
                + f"Finished running all .{yas} files in directory! Malex (copy by SpinachIsDelicious) has taken {str(time_taken)} seconds to finish! Faster than the expected time of {str(prediction)}! {round(prediction - time_taken, 2)} seconds faster than the prediction."
            )
            theMsg = f"Faster than the expected time of {prediction}! By {str(round(prediction-time_taken, 2))}"
        elif time_taken > prediction:
            print(
                Fore.MAGENTA
                + f"Finished running all .{FILE_EXTENSION} files! Malex (copy by SpinachIsDelicious) has taken {str(time_taken)} seconds to finish! This is {str(round(time_taken - prediction, 2))} more seconds than the expected time of {str(prediction)}."
            )
            theMsg = f"This is {str(round(time_taken - prediction, 2))} more seconds than the expected time of {str(prediction)}."
        else:
            print(
                Fore.MAGENTA
                + f"Finished running all .{FILE_EXTENSION} files! Malex (copy by SpinachIsDelicious) has taken {time_taken} seconds to finish! The predicted time of all tasks finishing running is correct. Wow!"
            )
            theMsg = (
                f"The predicted time of all tasks finishing running is correct. Wow!"
            )

        with open("information.txt", "w") as file:
            text = f"""
Malware was not blocked {str(succeedcount)} times
Malware was blocked {str(failcount)} times
Total malware attempted running is {str(len(files))}
Time taken Malex is {time_taken}
Predicted time taken is {prediction}
{theMsg}

    all credits go to SpinachIsDelicious on github. yes i am typing this, skids who steal code isnt cool
    thats why i am not sharing open source ver of this tool
    I'm encountering an error where the exe file window randomly closes...
    if you encounter this error, please open an issue on my github and I will start debugging the application
    to find the error. I just think that it's closing because of an issue
    of my hardware/software
    """
            file.write(text)

        sleep(6)
        cls()
        print(
            Fore.YELLOW
            + "Malex by SpinachIsDelicious on Github has finished executing! Blocks.txt and notblocked.txt have been created in the directory of Malex, check it out! There is also information.txt that contains information of the tasks completed by Malex. Blocks.txt contains antivirus blocks, and notblocked contains antivirus fails."
        )
        print(
            Fore.BLUE
            + "If you want to see the previous information, view information.txt which was created inside of the directory Malex is in."
        )
        print(Fore.GREEN + f"The malware has been blocked {str(failcount)} time(s).")
        input(
            Fore.RED
            + f"The malware has not been blocked {str(succeedcount)} time(s).\n"
            + Fore.GREEN
            + " >>> "
        )
        effect()

    effect()
    cls()
    print(
        Fore.GREEN
        + "Press Ctrl + C at any time during the application process to exit.\n"
        + Fore.YELLOW
        + "This tool has been created by SpinachIsDelicious on Github.\n"
        + Fore.CYAN
        + "To get in contact, information will be on my Github. Discord is fastest.\n"
        + Fore.BLUE
        + "I am not responsible for any of your actions using your tool. I'm literally accountable for nothing you do. Keep in mind that.\n"
        + Fore.RED
        + "This tool isn't open source because of skids. Stop stealing code skids :)\n"
        + Fore.CYAN
        + "By the way, this Malex has a variety of errors, and it does not support file types other than .exe\n"
    )
    link("https://discordapp.com/users/871531078391853158", new=1, autoraise=True)
    # refer above for the disdcord profile thing
    sleep(6)
    execute()

    # task log / dev log
    # 1) open link of discord profile after task finish
    # 3) add cool credits screen
    # 5) instead of saving malex info files (blocks,txt, notblocked.txt) save to a specific path that the user specifies
    # (like a network directory since ransomware will encrypt blocks.txt and notblocked.txt)
    # 7) contact me page using requests api
except Exception as Error:
    input(
        Fore.RED
        + "The program has encountered an error. Please open an issue ticket on the Github. Error: "
        + str(Error)
        + Fore.GREEN
        + ": If the error is a file, if the file isn't a .exe file Malex isn't broken. Malex isn't compatible with files other than .exe"
    )
    sleep(10)
    cls()
    print(Fore.RED + "Contact Support Immediately!!!")
    sleep(3)
    quit()
