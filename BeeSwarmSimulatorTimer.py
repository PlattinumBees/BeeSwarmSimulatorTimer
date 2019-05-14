"""
Author: Plattinum Bees
Description: This tool was developed to help keep track of mob and loot items that have a fixed time between occurances.
This project is offered freely to users and modify as needed. I searched for a simple python script to do this, but was
unable to find one. I learned (and borrowed code) on multithreading from tutorialspoint.com
(link = https://www.tutorialspoint.com/python3/python_multithreading.htm) and how to display python using tkinter from
likegeeks.com (link = https://likegeeks.com/python-gui-examples-tkinter-tutorial/)

Enjoy the project and let me know if you have tips/suggestions, thanks!

-PB
"""

import threading
import time
import datetime
import tkinter as tk

exitFlag = 0

'''Each variable is has 3 variables to help process the multithreading needed to keep each timer running independently
_time holds the value of the current countdown to pass to the GUI
_counter holds the current count of seconds since the timer was started
_TIMER is the value, in seconds, you want to count down from. (I.e. 1 hour = 3600 seconds)
'''
King_time = 0
king_counter = 0
KING_TIMER = 86400
Ant_Pass = 0
ant_counter = 0
ANT_TIMER = 7200
Jelly_dispenser = 0
jelly_counter = 0
JELLY_TIMER = 79200
Wealth_clock = 0
wealth_counter = 0
WEALTH_TIMER = 3600

class myThread (threading.Thread):
   def __init__(self, threadID, name, counter, timer):
       threading.Thread.__init__(self)
       self.threadID = threadID
       self.name = name
       self.counter = counter
       self.timer = timer

   def run(self):
      print ("Starting " + self.name)
      print_time(self.name, self.counter, 5, self.timer)
      print (self.name + " is READY!")

def print_time(threadName, delay, counter, timer):
   while counter < timer:
      if exitFlag:
         threadName.exit()
      global King_time, Ant_Pass, Jelly_dispenser, Wealth_clock
      global king_counter, ant_counter, jelly_counter, wealth_counter
      time.sleep(delay)
      if threadName == "King Beetle":
          King_time = timer - king_counter
          king_counter +=1
      elif threadName == "Ant Ticket":
          Ant_Pass = timer - ant_counter
          ant_counter +=1
      elif threadName == "Jelly Dispenser":
          Jelly_dispenser = timer - jelly_counter
          jelly_counter +=1
      elif threadName == "Wealth Clock":
          Wealth_clock = timer - wealth_counter
          wealth_counter +=1
      else:
          print ("%s: %s" % (threadName, ": Can't find the time, sorry!"))
      counter += 1

class ProgressBar():
    def __init__(self, root):
        self.root=root
        self.root.title("Bee Swarm Simulator Timers")
        self.root.geometry("200x50+900+100")
        self.q = tk.StringVar()
        #self.r = tk.StringVar()
        tk.Label(root, text="Auto-quit in: ", bg="yellow",
                 width=10).grid(row=0, column=0)
        tk.Label(root, textvariable=self.q, bg="yellow",
                 width=10).grid(row=0, column=1)
        tk.Button(self.root, text="Quit", bg="red",
                  command=self.root.destroy).grid(row=1, column=1)
        self.ctr=1000000
        self.update_label()
        self.start_countdown()

    def resetKing(self):
        global king_counter; king_counter = 0
    def resetAnt(self):
        global ant_counter; ant_counter = 0
    def resetJelly(self):
        global jelly_counter; jelly_counter = 0
    def resetWealth(self):
        global wealth_counter; wealth_counter = 0

    def start_countdown(self):
        """ a separate process in a separate GUI
        """
        top2=tk.Toplevel(self.root, bg="lightyellow")
        top2.geometry("485x115+900+300")

        # King Beetle
        self.label_king = tk.IntVar()
        self.label_king.set(self.ctr)
        tk.Label(top2, text="King Beetle", width=20, font=("Verdans", 15)).grid(column=0, row=0)
        tk.Label(top2, textvariable=self.label_king, width=15, font=("Verdans", 15)).grid(column=1, row=0)
        tk.Button(top2, text="Reset", width=10, font=("Verdans", 10), command=self.resetKing).grid(column=2, row=0)

        # Ant Pass
        self.label_ant = tk.IntVar()
        self.label_ant.set(self.ctr)
        tk.Label(top2, text="Ant Pass", width=20, font=("Verdans", 15)).grid(column=0, row=1)
        tk.Label(top2, textvariable=self.label_ant, width=15, font=("Verdans", 15)).grid(column=1, row=1)
        tk.Button(top2, text="Reset", width=10, font=("Verdans", 10), command=self.resetAnt).grid(column=2, row=1)

        # Star Area Jelly Dispenser
        self.label_jelly = tk.IntVar()
        self.label_jelly.set(self.ctr)
        tk.Label(top2, text="Jelly Dispenser", width=20, font=("Verdans", 15)).grid(column=0, row=2)
        tk.Label(top2, textvariable=self.label_jelly, width=15, font=("Verdans", 15)).grid(column=1, row=2)
        tk.Button(top2, text="Reset", width=10, font=("Verdans", 10), command=self.resetJelly).grid(column=2, row=2)

        # Wealth Clock
        self.label_wealth = tk.IntVar()
        self.label_wealth.set(self.ctr)
        tk.Label(top2, text="Wealth Clock", width=20, font=("Verdans", 15)).grid(column=0, row=3)
        tk.Label(top2, textvariable=self.label_wealth, width=15, font=("Verdans", 15)).grid(column=1, row=3)
        tk.Button(top2, text="Reset", width=10, font=("Verdans", 10), command=self.resetWealth).grid(column=2, row=3)

        if self.ctr > 0:
            self.update()
        else:
            self.top2.destroy()

    def update(self):
        global Ant_Pass, King_time, Jelly_dispenser
        if self.ctr > 0:
            self.root.after(1000, self.update)  ## 1/2 second
            self.label_ant.set((str(datetime.timedelta(seconds=Ant_Pass))))
            self.label_king.set((str(datetime.timedelta(seconds=King_time))))
            self.label_jelly.set((str(datetime.timedelta(seconds=Jelly_dispenser))))
            self.label_wealth.set((str(datetime.timedelta(seconds=Wealth_clock))))
            self.ctr -= 1
        else:
            ## sleep for one second to allow any remaining after() to execute
            ## can also use self.root.after_cancel(id)
            self.root.after(1000, self.root.destroy)

    def update_label(self):
        self.q.set(self.ctr)
        ## only call after() while the countdown is running (self.ctr > 0)
        ## to avoid a dangling after() when the program terminates
        if self.ctr > 0:
            self.root.after(1000, self.update_label)  ## one second

def startThreads():
# Create new threads
    thread1 = myThread(1, "King Beetle", 1, KING_TIMER)
    thread2 = myThread(2, "Ant Ticket", 1, ANT_TIMER)
    thread3 = myThread(3, "Jelly Dispenser", 1, JELLY_TIMER)
    thread4 = myThread(4, "Wealth Clock", 1, WEALTH_TIMER)
    # Start new Threads
    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()

def joinThreads():
    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()
    print ("Exiting Main Thread")

def doubleTimer():
    root = tk.Tk()
    PB = ProgressBar(root)
    root.mainloop()

startThreads()
doubleTimer()





