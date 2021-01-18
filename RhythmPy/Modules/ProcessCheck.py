import psutil
import time

"""
this will be used to check if the game is running
"""


def IsProcessRunning(processName):
    """
    Check if there is any running process that contains the given name processName.
    """
    # Iterate over the all the running process
    for proc in psutil.process_iter():
        try:
            # Check if process name contains the given name string.
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False


def findProcessIdByName(processName):
    """
    Get a list of all the PIDs of a all the running process whose name contains
    the given string processName
    """
    listOfProcessObjects = []
    # Iterate over the all the running process
    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=["pid", "name", "create_time"])
            # Check if process name contains the given name string.
            if processName.lower() in pinfo["name"].lower():
                listOfProcessObjects.append(pinfo)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return listOfProcessObjects


# main loop can be ignored
def main():
    print("*** Check if a process is running or not ***")

    # Check if any process are running or not.
    if IsProcessRunning("opera"):
        print("Yes a this process was running")
    else:
        print("No chrome process was running")
    print("*** Find PIDs of a running process by Name ***")

    # Find PIDs od all the running instances of process that contains 'opera' in it's name
    listOfProcessIds = findProcessIdByName("opera")

    if len(listOfProcessIds) > 0:
        print("Process Exists | PID and other details are")

        for elem in listOfProcessIds:
            processID = elem["pid"]
            processName = elem["name"]
            processCreationTime = time.strftime(
                "%Y-%m-%d %H:%M:%S", time.localtime(elem["create_time"])
            )
            print((processID, processName, processCreationTime))
    else:
        print("No Running Process found with given text")

    print("** Find running process by name using List comprehension **")
    # Find PIDs od all the running instances of process that contains 'opera' in it's name
    procObjList = [
        procObj
        for procObj in psutil.process_iter()
        if "chrome" in procObj.name().lower()
    ]
    for elem in procObjList:
        print(elem)


if __name__ == "__main__":
    main()
