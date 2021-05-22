import glob


def IsProduction():
    """
    Checks if Rhythmpy is being run in a Production enviroment
    Returns: Bool (True, False)
    """
    count = 0
    files = glob.glob("./**/*.py", recursive=True)
    for file in files:
        count += 1
    if count < 10:
        return True
    else:
        return False


IsProduction()
