import os
from AppOpener import open,close


def get_all_apps():
    start_menu_path = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs"
    system_apps_path = "C:\\Windows\\System32"

    programs = []

    for program in os.listdir(start_menu_path):
        if program.endswith(".lnk"):
            program_name = os.path.splitext(program)[0]
            programs.append(program_name.replace('_', ' ').lower())

    for app in os.listdir(system_apps_path):
        if app.endswith(".exe"):
            app_name = os.path.splitext(app)[0]
            programs.append(app_name.lower())
    lst = ['camera','calendar','calculator','clock','photos','movies','microsoft store','paint','settings','media player','maps']
    programs.extend(lst)
    return programs


def open_app(app_name):
    open(app_name, match_closest=True)

def close_app(app_name):
    close(app_name, match_closest=True, output=False)