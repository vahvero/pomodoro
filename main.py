"""
    Module create pomodoro style time managment 
    with progress bar and notification on the rest
    and work changes

    References:
        https://en.wikipedia.org/wiki/Pomodoro_Technique

    Example:
    ```
    # First argument is the work timer and the second the rest timer
    >>>py main.py 25 5
    # <the program executes 25 minutes and 5 minute cycles>
    ```

    Authors:
        Vahvero
"""

import fire
from progress.bar import Bar
import time
import os

import tkinter
from tkinter import messagebox

__author__ = "vahvero"
MINUTE = 60
NAME = "Pomodoro"

WORK_NAME = "Wörk"
REST_NAME = "Rötväys"
WORK_MESSAGE = "Start work!"
REST_MESSAGE = "Start rest!"
STEP_SIZE = 100

def create_bar(title, fill="#", suffix="%(percent)d%%"):
    """Create progress library bar

    Args:
        title ([type]): Name shown in the bar
        fill (str, optional): What step ascii looks like. Defaults to "#".
        suffix (str, optional): What is the ending format of the bar. Defaults to "%(percent)d%%".

    Returns:
        Bar: `progress` library bar
    """
    return Bar(title, fill=fill, suffix=suffix)


def start(work=25, rest=5):
    """Starts with wörk progress bar for `work` minutes
    and change progress bar to `rest` minutes. Repeat forever.

    Args:
        work (int, optional): Minutes of work. Defaults to 25.
        rest (int, optional): Minutes of rest. Defaults to 5.
    """
    root = tkinter.Tk()
    root.withdraw()
    # Create system invariant clear for cmd
    clear = lambda: os.system("cls") if os.name == "nt" else lambda: os.system("clear")
    clear()
    # Calculcate sleep time for 100 steps of the bars
    work_sleep = work * MINUTE / STEP_SIZE
    rest_sleep = rest * MINUTE / STEP_SIZE

    while True:
        with create_bar(WORK_NAME) as bar:
            for _ in range(STEP_SIZE):
                time.sleep(work_sleep)
                bar.next()
        
        messagebox.showinfo(NAME, REST_MESSAGE)

        with create_bar(REST_NAME) as bar:
            for _ in range(STEP_SIZE):
                time.sleep(rest_sleep)
                bar.next()

        messagebox.showinfo(NAME, WORK_MESSAGE)
        clear()

if __name__ == "__main__":
    fire.Fire(start)
