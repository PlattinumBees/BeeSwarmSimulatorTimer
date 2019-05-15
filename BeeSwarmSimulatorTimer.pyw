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
remaining time =holds the value of the current countdown to pass to the GUI
counter = holds the current count of seconds since the timer was started
timer = is the value, in seconds, you want to count down from. (I.e. 1 hour = 3600 seconds)
'''

'''   BOOSTERS  '''
wealth_list = [0, 0, 3600]  #remaining time, counter, timer]
field_list = [0, 0, 7200]
blue_field_list = [0, 0, 7200]
red_field_list = [0, 0, 7200]

'''  DISPENSERS '''
jelly_list = [0, 0, 79200]
ant_list = [0, 0, 7200]
blueberry_list = [0, 0, 14400]
strawberry_list = [0, 0, 14400]
honey_list = [0, 0, 3600]
treat_list = [0, 0, 3600]
glue_list = [0, 0, 79200]
'''     MOBS    '''
ladybug_list = [0, 0, 300]
rhino_list = [0, 0, 300]
spider_list = [0, 0, 1800]
mantis_list = [0, 0, 1200]
scorpion_list = [0, 0, 1200]
werewolf_list = [0, 0, 3600]
snail_list = [0, 0, 345600]
cavemonster_list = [0, 0, 1800]
'''    BOSSES   '''
king_list = [0, 0, 86400]
tunnel_list = [0, 0, 172800]
stick_list = [0, 0, 129600]
'''    QUESTS   '''
brownbear_list = [0, 0, 14400]
blackbear_list = [0, 0, 3600]

#all_lists = [wealth_list,field_list,blue_field_list,red_field_list,jelly_list,ant_list,king_list, ]

class myThread (threading.Thread):
    def __init__(self, threadID, name, counter, timer):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
        self.timer = timer
    def run(self):
        print ("Starting " + self.name)
        print_time(self.name, self.counter, 0, self.timer)
        print (self.name + " is READY!")
def print_time(threadName, delay, counter, timer):
    while True:
        if exitFlag:
            threadName.exit()
        #global king_list, ant_list, jelly_list, wealth_list
        #global all_lists
        time.sleep(delay)
        # BOOSTERS
        if threadName == "Wealth Clock":
            wealth_list[0] = timer - wealth_list[1]
            wealth_list[1]+=1
        elif threadName == "Field Boost":
            field_list[0] = timer - field_list[1]
            field_list[1]+=1
        elif threadName == "Blue Field Boost":
            blue_field_list[0] = timer - blue_field_list[1]
            blue_field_list[1]+=1
        elif threadName == "Red Field Boost":
            red_field_list[0] = timer - red_field_list[1]
            red_field_list[1]+=1
        # DISPENSERS
        elif threadName == "Ant Ticket":
            ant_list[0] = timer - ant_list[1]
            ant_list[1] +=1
        elif threadName == "Royal Jelly":
            jelly_list[0] = timer - jelly_list[1]
            jelly_list[1] +=1
        elif threadName == "Blueberry Dispenser":
            blueberry_list[0] = timer - blueberry_list[1]
            blueberry_list[1] +=1
        elif threadName == "Strawberry Dispenser":
            strawberry_list[0] = timer - strawberry_list[1]
            strawberry_list[1] +=1
        elif threadName == "Honey Dispenser":
            honey_list[0] = timer - honey_list[1]
            honey_list[1] +=1
        elif threadName == "Treat Dispenser":
            treat_list[0] = timer - treat_list[1]
            treat_list[1] +=1
        elif threadName == "Glue Dispenser":
            glue_list[0] = timer - glue_list[1]
            glue_list[1] +=1
        # MOBS
        # Lady Bug
        elif threadName == "Lady Bug":
            ladybug_list[0] = timer - ladybug_list[1]
            ladybug_list[1] +=1
        # Rhino Beetle
        elif threadName == "Rhino Beetle":
            rhino_list[0] = timer - rhino_list[1]
            rhino_list[1] +=1
        # Spider
        elif threadName == "Spider":
            spider_list[0] = timer - spider_list[1]
            spider_list[1] +=1
        # Mantis
        elif threadName == "Mantis":
            mantis_list[0] = timer - mantis_list[1]
            mantis_list[1] +=1
        # Scorpion
        elif threadName == "Scorpion":
            scorpion_list[0] = timer - scorpion_list[1]
            scorpion_list[1] +=1
        # Werewolf
        elif threadName == "Werewolf":
            werewolf_list[0] = timer - werewolf_list[1]
            werewolf_list[1] +=1
        # Stump Snail
        elif threadName == "Stump Snail":
            snail_list[0] = timer - snail_list[1]
            snail_list[1] +=1
        # Cave Monster
        elif threadName == "Cave Monster":
            cavemonster_list[0] = timer - cavemonster_list[1]
            cavemonster_list[1] +=1
        # BOSSES
        elif threadName == "King Beetle":
            king_list[0] = timer - king_list[1]
            king_list[1] +=1
        elif threadName == "Tunnel Bear":
            tunnel_list[0] = timer - tunnel_list[1]
            tunnel_list[1] +=1
        elif threadName == "Stick Bug":
            stick_list[0] = timer - stick_list[1]
            stick_list[1] +=1
        # QUESTS
        elif threadName == "Brown Bear Quest":
            brownbear_list[0] = timer - brownbear_list[1]
            brownbear_list[1] +=1
        elif threadName == "Black Bear Quest":
            blackbear_list[0] = timer - blackbear_list[1]
            blackbear_list[1] += 1
        else:
            print ("%s: %s" % (threadName, ": Can't find the time, sorry!"))
        counter += 1

class ProgressBar():
    def __init__(self, root):
        self.root=root
        self.root.title("Bee Swarm Simulator Timers")
        self.root.geometry("150x50+900+100")
        self.q = tk.StringVar()
        tk.Label(root, text="Auto-quit in: ", bg="yellow",
                width=10).grid(row=0, column=0)
        tk.Label(root, textvariable=self.q, bg="yellow",
                width=10).grid(row=0, column=1)
        #tk.Button(self.root, text="Restart", bg="green",
                  #command=self.root.destroy).grid(row=1, column=0)
        tk.Button(self.root, text="Quit", bg="red",
                command=self.root.destroy).grid(row=1, column=1)
        self.ctr = 1000000
        self.update_label()
        self.start_countdown()

        '''   BOOSTERS  '''
    def resetWealth(self):
        global wealth_list
        wealth_list[1] = 0
    def resetField(self):
        global field_list
        field_list[1] = 0
    def resetBlueField(self):
        global blue_field_list
        blue_field_list[1] = 0
    def resetRedField(self):
        global red_field_list
        red_field_list[1] = 0
        '''  DISPENSERS '''
    def resetAnt(self):
        global ant_list;
        ant_list[1] = 0
    def resetJelly(self):
        global jelly_list;
        jelly_list[1] = 0
    def resetBlueberry(self):
        global blueberry_list;
        blueberry_list[1] = 0
    def resetStrawberry(self):
        global strawberry_list;
        strawberry_list[1] = 0
    def resetHoney(self):
        global honey_list;
        honey_list[1] = 0
    def resetTreat(self):
        global treat_list;
        treat_list[1] = 0
    def resetGlue(self):
        global glue_list;
        glue_list[1] = 0
        '''     MOBS    '''
    def resetLadybug(self):
        global ladybug_list;
        ladybug_list[1] = 0
    def resetRhino(self):
        global rhino_list;
        rhino_list[1] = 0
    def resetSpider(self):
        global spider_list;
        spider_list[1] = 0
    def resetMantis(self):
        global mantis_list;
        mantis_list[1] = 0
    def resetScorpion(self):
        global scorpion_list;
        scorpion_list[1] = 0
    def resetWerewolf(self):
        global werewolf_list;
        werewolf_list[1] = 0
    def resetSnail(self):
        global snail_list;
        snail_list[1] = 0
    def resetCavemonster(self):
        global cavemonster_list;
        cavemonster_list[1] = 0
        '''    BOSSES   '''
    def resetKing(self):
        global king_list;
        king_list[1] = 0
    def resetTunnel(self):
        global tunnel_list;
        tunnel_list[1] = 0
    def resetStick(self):
        global stick_list;
        stick_list[1] = 0
        '''    QUESTS   '''
    def resetBrownbear(self):
        global brownbear_list;
        brownbear_list[1] = 0
    def resetBlackbear(self):
        global blackbear_list;
        blackbear_list[1] = 0

    def start_countdown(self):
        """ a separate process to show the timer's threads in a GUI
        """
        top2=tk.Toplevel(self.root, bg="lightyellow")
        top2.geometry("485x695+900+300")
        '''   BOOSTERS  '''
        # Wealth Clock
        self.label_wealth = tk.IntVar()
        self.label_wealth.set(self.ctr)
        tk.Label(top2, text="Wealth Clock", bg="lightblue", width=20, font=("Verdans", 15)).grid(column=0, row=0)
        tk.Label(top2, textvariable=self.label_wealth, bg="lightblue", width=15, font=("Verdans", 15)).grid(column=1, row=0)
        tk.Button(top2, text="Restart", bg="lightblue", width=10, font=("Verdans", 10), command=self.resetWealth).grid(column=2, row=0)
        # Field Boost
        self.label_field = tk.IntVar()
        self.label_field.set(self.ctr)
        tk.Label(top2, text="Field Boost", bg="lightblue", width=20, font=("Verdans", 15)).grid(column=0, row=1)
        tk.Label(top2, textvariable=self.label_field, bg="lightblue", width=15, font=("Verdans", 15)).grid(column=1, row=1)
        tk.Button(top2, text="Restart", bg="lightblue", width=10, font=("Verdans", 10), command=self.resetField).grid(column=2, row=1)
        # Blue Field Boost
        self.label_bluefield = tk.IntVar()
        self.label_bluefield.set(self.ctr)
        tk.Label(top2, text="Blue Field Boost", bg="lightblue", width=20, font=("Verdans", 15)).grid(column=0, row=2)
        tk.Label(top2, textvariable=self.label_bluefield, bg="lightblue", width=15, font=("Verdans", 15)).grid(column=1, row=2)
        tk.Button(top2, text="Restart", bg="lightblue", width=10, font=("Verdans", 10), command=self.resetBlueField).grid(column=2, row=2)
        # Red Field Boost
        self.label_redfield = tk.IntVar()
        self.label_redfield.set(self.ctr)
        tk.Label(top2, text="Red Field Boost", bg="lightblue", width=20, font=("Verdans", 15)).grid(column=0, row=3)
        tk.Label(top2, textvariable=self.label_redfield, bg="lightblue", width=15, font=("Verdans", 15)).grid(column=1, row=3)
        tk.Button(top2, text="Restart", bg="lightblue", width=10, font=("Verdans", 10), command=self.resetRedField).grid(column=2, row=3)
        '''  DISPENSERS '''
        # Star Area Jelly Dispenser
        self.label_jelly = tk.IntVar()
        self.label_jelly.set(self.ctr)
        tk.Label(top2, text="Royal Jelly", bg="lightgreen", width=20, font=("Verdans", 15)).grid(column=0, row=10)
        tk.Label(top2, textvariable=self.label_jelly, bg="lightgreen", width=15, font=("Verdans", 15)).grid(column=1, row=10)
        tk.Button(top2, text="Restart", bg="lightgreen", width=10, font=("Verdans", 10), command=self.resetJelly).grid(column=2, row=10)
        # Ant Pass
        self.label_ant = tk.IntVar()
        self.label_ant.set(self.ctr)
        tk.Label(top2, text="Ant Pass", bg="lightgreen", width=20, font=("Verdans", 15)).grid(column=0, row=11)
        tk.Label(top2, textvariable=self.label_ant, bg="lightgreen", width=15, font=("Verdans", 15)).grid(column=1, row=11)
        tk.Button(top2, text="Restart", bg="lightgreen", width=10, font=("Verdans", 10), command=self.resetAnt).grid(column=2, row=11)
        # Blueberry Dispenser
        self.label_blueberry = tk.IntVar()
        self.label_blueberry.set(self.ctr)
        tk.Label(top2, text="Blueberry Dispenser", bg="lightgreen", width=20, font=("Verdans", 15)).grid(column=0, row=12)
        tk.Label(top2, textvariable=self.label_blueberry, bg="lightgreen", width=15, font=("Verdans", 15)).grid(column=1, row=12)
        tk.Button(top2, text="Restart", bg="lightgreen", width=10, font=("Verdans", 10), command=self.resetBlueberry).grid(column=2, row=12)
        # Strawberry Dispenser
        self.label_strawberry = tk.IntVar()
        self.label_strawberry.set(self.ctr)
        tk.Label(top2, text="Strawberry Dispenser", bg="lightgreen", width=20, font=("Verdans", 15)).grid(column=0, row=13)
        tk.Label(top2, textvariable=self.label_strawberry, bg="lightgreen", width=15, font=("Verdans", 15)).grid(column=1, row=13)
        tk.Button(top2, text="Restart", bg="lightgreen", width=10, font=("Verdans", 10), command=self.resetStrawberry).grid(column=2, row=13)
        # Honey Dispenser
        self.label_honey = tk.IntVar()
        self.label_honey.set(self.ctr)
        tk.Label(top2, text="Honey Dispenser", bg="lightgreen", width=20, font=("Verdans", 15)).grid(column=0, row=14)
        tk.Label(top2, textvariable=self.label_honey, bg="lightgreen", width=15, font=("Verdans", 15)).grid(column=1, row=14)
        tk.Button(top2, text="Restart", bg="lightgreen", width=10, font=("Verdans", 10), command=self.resetHoney).grid(column=2, row=14)
        # Treat Dispenser
        self.label_treat = tk.IntVar()
        self.label_treat.set(self.ctr)
        tk.Label(top2, text="Treat Dispenser", bg="lightgreen", width=20, font=("Verdans", 15)).grid(column=0, row=15)
        tk.Label(top2, textvariable=self.label_treat, bg="lightgreen", width=15, font=("Verdans", 15)).grid(column=1, row=15)
        tk.Button(top2, text="Restart", bg="lightgreen", width=10, font=("Verdans", 10), command=self.resetTreat).grid(column=2, row=15)
        # Glue Dispenser
        self.label_glue = tk.IntVar()
        self.label_glue.set(self.ctr)
        tk.Label(top2, text="Glue Dispenser", bg="lightgreen", width=20, font=("Verdans", 15)).grid(column=0, row=16)
        tk.Label(top2, textvariable=self.label_glue, bg="lightgreen", width=15, font=("Verdans", 15)).grid(column=1, row=16)
        tk.Button(top2, text="Restart", bg="lightgreen", width=10, font=("Verdans", 10), command=self.resetGlue).grid(column=2, row=16)
        '''     MOBS    '''
        self.label_ladybug= tk.IntVar()
        self.label_ladybug.set(self.ctr)
        tk.Label(top2, text="Lady Bug", bg="red", width=20, font=("Verdans", 15)).grid(column=0, row=20)
        tk.Label(top2, textvariable=self.label_ladybug, bg="red", width=15, font=("Verdans", 15)).grid(column=1, row=20)
        tk.Button(top2, text="Restart", bg="red", width=10, font=("Verdans", 10), command=self.resetLadybug).grid(column=2, row=20)
        self.label_rhino= tk.IntVar()
        self.label_rhino.set(self.ctr)
        tk.Label(top2, text="Rhino Beetle", bg="red", width=20, font=("Verdans", 15)).grid(column=0, row=21)
        tk.Label(top2, textvariable=self.label_rhino, bg="red", width=15, font=("Verdans", 15)).grid(column=1, row=21)
        tk.Button(top2, text="Restart", bg="red", width=10, font=("Verdans", 10), command=self.resetRhino).grid(column=2, row=21)
        self.label_spider= tk.IntVar()
        self.label_spider.set(self.ctr)
        tk.Label(top2, text="Spider", bg="red", width=20, font=("Verdans", 15)).grid(column=0, row=22)
        tk.Label(top2, textvariable=self.label_spider, bg="red", width=15, font=("Verdans", 15)).grid(column=1, row=22)
        tk.Button(top2, text="Restart", bg="red", width=10, font=("Verdans", 10), command=self.resetSpider).grid(column=2, row=22)
        self.label_mantis= tk.IntVar()
        self.label_mantis.set(self.ctr)
        tk.Label(top2, text="Mantis", bg="red", width=20, font=("Verdans", 15)).grid(column=0, row=23)
        tk.Label(top2, textvariable=self.label_mantis, bg="red", width=15, font=("Verdans", 15)).grid(column=1, row=23)
        tk.Button(top2, text="Restart", bg="red", width=10, font=("Verdans", 10), command=self.resetMantis).grid(column=2, row=23)
        self.label_scorpion= tk.IntVar()
        self.label_scorpion.set(self.ctr)
        tk.Label(top2, text="Scorpion", bg="red", width=20, font=("Verdans", 15)).grid(column=0, row=24)
        tk.Label(top2, textvariable=self.label_scorpion, bg="red", width=15, font=("Verdans", 15)).grid(column=1, row=24)
        tk.Button(top2, text="Restart", bg="red", width=10, font=("Verdans", 10), command=self.resetScorpion).grid(column=2, row=24)
        self.label_werewolf= tk.IntVar()
        self.label_werewolf.set(self.ctr)
        tk.Label(top2, text="Werewolf", bg="red", width=20, font=("Verdans", 15)).grid(column=0, row=25)
        tk.Label(top2, textvariable=self.label_werewolf, bg="red", width=15, font=("Verdans", 15)).grid(column=1, row=25)
        tk.Button(top2, text="Restart", bg="red", width=10, font=("Verdans", 10), command=self.resetWerewolf).grid(column=2, row=25)
        self.label_snail= tk.IntVar()
        self.label_snail.set(self.ctr)
        tk.Label(top2, text="Stump Snail", bg="red", width=20, font=("Verdans", 15)).grid(column=0, row=26)
        tk.Label(top2, textvariable=self.label_snail, bg="red", width=15, font=("Verdans", 15)).grid(column=1, row=26)
        tk.Button(top2, text="Restart", bg="red", width=10, font=("Verdans", 10), command=self.resetSnail).grid(column=2, row=26)
        self.label_cavemonster= tk.IntVar()
        self.label_cavemonster.set(self.ctr)
        tk.Label(top2, text="Cave Monster", bg="red", width=20, font=("Verdans", 15)).grid(column=0, row=27)
        tk.Label(top2, textvariable=self.label_cavemonster, bg="red", width=15, font=("Verdans", 15)).grid(column=1, row=27)
        tk.Button(top2, text="Restart", bg="red", width=10, font=("Verdans", 10), command=self.resetCavemonster).grid(column=2, row=27)
        '''    BOSSES   '''
        self.label_king = tk.IntVar()
        self.label_king.set(self.ctr)
        tk.Label(top2, text="King Beetle", bg="maroon", width=20, font=("Verdans", 15)).grid(column=0, row=30)
        tk.Label(top2, textvariable=self.label_king, bg="maroon", width=15, font=("Verdans", 15)).grid(column=1, row=30)
        tk.Button(top2, text="Restart", bg="maroon", width=10, font=("Verdans", 10), command=self.resetKing).grid(column=2, row=30)
        self.label_tunnel = tk.IntVar()
        self.label_tunnel.set(self.ctr)
        tk.Label(top2, text="Tunnel Bear", bg="maroon", width=20, font=("Verdans", 15)).grid(column=0, row=31)
        tk.Label(top2, textvariable=self.label_tunnel, bg="maroon", width=15, font=("Verdans", 15)).grid(column=1, row=31)
        tk.Button(top2, text="Restart", bg="maroon", width=10, font=("Verdans", 10), command=self.resetTunnel).grid(column=2, row=31)
        self.label_stick = tk.IntVar()
        self.label_stick.set(self.ctr)
        tk.Label(top2, text="Stick Bug", bg="maroon", width=20, font=("Verdans", 15)).grid(column=0, row=32)
        tk.Label(top2, textvariable=self.label_stick, bg="maroon", width=15, font=("Verdans", 15)).grid(column=1, row=32)
        tk.Button(top2, text="Restart", bg="maroon", width=10, font=("Verdans", 10), command=self.resetStick).grid(column=2, row=32)
        '''    QUESTS   '''
        self.label_brownbear = tk.IntVar()
        self.label_brownbear.set(self.ctr)
        tk.Label(top2, text="Brown Bear Quest", bg="teal", width=20, font=("Verdans", 15)).grid(column=0, row=40)
        tk.Label(top2, textvariable=self.label_brownbear, bg="teal", width=15, font=("Verdans", 15)).grid(column=1, row=40)
        tk.Button(top2, text="Restart", bg="teal", width=10, font=("Verdans", 10), command=self.resetBrownbear).grid(column=2, row=40)
        self.label_blackbear = tk.IntVar()
        self.label_blackbear.set(self.ctr)
        tk.Label(top2, text="Black Bear Quest", bg="teal", width=20, font=("Verdans", 15)).grid(column=0, row=41)
        tk.Label(top2, textvariable=self.label_blackbear, bg="teal", width=15, font=("Verdans", 15)).grid(column=1, row=41)
        tk.Button(top2, text="Restart", bg="teal", width=10, font=("Verdans", 10), command=self.resetBlackbear).grid(column=2, row=41)

        if self.ctr > 0:
            self.update()
        else:
            self.top2.destroy()

    def update(self):
        global all_lists
        if self.ctr > 0:
            self.root.after(1000, self.update) ## 1/2 second
            '''   BOOSTERS  '''
            # Wealth Clock
            if wealth_list[0] < 1:
                self.label_wealth.set((str("Ready")))
            else:
                self.label_wealth.set((str(datetime.timedelta(seconds=wealth_list[0]))))
            self.ctr -= 1
            # Field Booster
            if field_list[0] < 1:
                self.label_field.set((str("Ready")))
            else:
                self.label_field.set((str(datetime.timedelta(seconds=field_list[0]))))
            self.ctr -= 1
            # Blue Field Booster
            if blue_field_list[0] < 1:
                self.label_bluefield.set((str("Ready")))
            else:
                self.label_bluefield.set((str(datetime.timedelta(seconds=blue_field_list[0]))))
            self.ctr -= 1
            # Red Field Booster
            if red_field_list[0] < 1:
                self.label_redfield.set((str("Ready")))
            else:
                self.label_redfield.set((str(datetime.timedelta(seconds=red_field_list[0]))))
            self.ctr -= 1
            '''  DISPENSERS '''
            # Ant Ticket Dispenser
            if ant_list[0] < 1:
                self.label_ant.set((str("Ready")))
            else:
                self.label_ant.set((str(datetime.timedelta(seconds=ant_list[0]))))
            # Royal Jelly Dispenser
            if jelly_list[0] < 1:
                self.label_jelly.set((str("Ready")))
            else:
                self.label_jelly.set((str(datetime.timedelta(seconds=jelly_list[0]))))
            # Blueberry Dispenser
            if blueberry_list[0] < 1:
                self.label_blueberry.set((str("Ready")))
            else:
                self.label_blueberry.set((str(datetime.timedelta(seconds=blueberry_list[0]))))
            # Strawberry Dispenser
            if strawberry_list[0] < 1:
                self.label_strawberry.set((str("Ready")))
            else:
                self.label_strawberry.set((str(datetime.timedelta(seconds=strawberry_list[0]))))
            # Honey Dispenser
            if honey_list[0] < 1:
                self.label_honey.set((str("Ready")))
            else:
                self.label_honey.set((str(datetime.timedelta(seconds=honey_list[0]))))
            # Treat Dispenser
            if treat_list[0] < 1:
                self.label_treat.set((str("Ready")))
            else:
                self.label_treat.set((str(datetime.timedelta(seconds=treat_list[0]))))
            # Glue Dispenser
            if glue_list[0] < 1:
                self.label_glue.set((str("Ready")))
            else:
                self.label_glue.set((str(datetime.timedelta(seconds=glue_list[0]))))
            '''     MOBS    '''
            # Lady Bug
            if ladybug_list[0] < 1:
                self.label_ladybug.set((str("Ready")))
            else:
                self.label_ladybug.set((str(datetime.timedelta(seconds=ladybug_list[0]))))
            # Rhino Beetle
            if rhino_list[0] < 1:
                self.label_rhino.set((str("Ready")))
            else:
                self.label_rhino.set((str(datetime.timedelta(seconds=rhino_list[0]))))
            # Spider
            if spider_list[0] < 1:
                self.label_spider.set((str("Ready")))
            else:
                self.label_spider.set((str(datetime.timedelta(seconds=spider_list[0]))))
            # Mantis
            if mantis_list[0] < 1:
                self.label_mantis.set((str("Ready")))
            else:
                self.label_mantis.set((str(datetime.timedelta(seconds=mantis_list[0]))))
            # Scorpion
            if scorpion_list[0] < 1:
                self.label_scorpion.set((str("Ready")))
            else:
                self.label_scorpion.set((str(datetime.timedelta(seconds=scorpion_list[0]))))
            # Werewolf
            if werewolf_list[0] < 1:
                self.label_werewolf.set((str("Ready")))
            else:
                self.label_werewolf.set((str(datetime.timedelta(seconds=werewolf_list[0]))))
            # Stump Snail
            if snail_list[0] < 1:
                self.label_snail.set((str("Ready")))
            else:
                self.label_snail.set((str(datetime.timedelta(seconds=snail_list[0]))))
            # Cave Monster
            if cavemonster_list[0] < 1:
                self.label_cavemonster.set((str("Ready")))
            else:
                self.label_cavemonster.set((str(datetime.timedelta(seconds=cavemonster_list[0]))))
            '''    BOSSES   '''
            # King Beetle
            if king_list[0] < 1:
                self.label_king.set((str("Ready")))
            else:
                self.label_king.set((str(datetime.timedelta(seconds=king_list[0]))))
            # Tunnel Bear
            if tunnel_list[0] < 1:
                self.label_tunnel.set((str("Ready")))
            else:
                self.label_tunnel.set((str(datetime.timedelta(seconds=tunnel_list[0]))))
            # Stick Bug
            if stick_list[0] < 1:
                self.label_stick.set((str("Ready")))
            else:
                self.label_stick.set((str(datetime.timedelta(seconds=stick_list[0]))))
            '''    QUESTS   '''
            if brownbear_list[0] < 1:
                self.label_brownbear.set((str("Ready")))
            else:
                self.label_brownbear.set((str(datetime.timedelta(seconds=brownbear_list[0]))))
            if blackbear_list[0] < 1:
                self.label_blackbear.set((str("Ready")))
            else:
                self.label_blackbear.set((str(datetime.timedelta(seconds=blackbear_list[0]))))
        else:
            ## sleep for one second to allow any remaining after() to execute
            ## can also use self.root.after_cancel(id)
            self.root.after(1000, self.root.destroy)
    def update_label(self):
        self.q.set(self.ctr)
        ## only call after() while the countdown is running (self.ctr > 0)
        ## to avoid a dangling after() when the program terminates
        if self.ctr > 0:
            self.root.after(1000, self.update_label) ## one second

def startThreads():
    # Create new threads
    '''   BOOSTERS  '''
    thread0 = myThread(4, "Wealth Clock", 1, wealth_list[2])
    thread1 = myThread(4, "Field Boost", 1, field_list[2])
    thread2 = myThread(4, "Blue Field Boost", 1, blue_field_list[2])
    thread3 = myThread(4, "Red Field Boost", 1, red_field_list[2])
    '''  DISPENSERS '''
    thread10 = myThread(2, "Ant Ticket", 1, ant_list[2])
    thread11 = myThread(3, "Royal Jelly", 1, jelly_list[2])
    thread12 = myThread(3, "Blueberry Dispenser", 1, blueberry_list[2])
    thread13 = myThread(3, "Strawberry Dispenser", 1, strawberry_list[2])
    thread14 = myThread(3, "Honey Dispenser", 1, honey_list[2])
    thread15 = myThread(3, "Treat Dispenser", 1, treat_list[2])
    thread16 = myThread(3, "Glue Dispenser", 1, glue_list[2])
    '''     MOBS    '''
    thread20 = myThread(3, "Lady Bug", 1, ladybug_list[2])
    thread21 = myThread(3, "Rhino Beetle", 1, rhino_list[2])
    thread22 = myThread(3, "Spider", 1, spider_list[2])
    thread23 = myThread(3, "Mantis", 1, mantis_list[2])
    thread24 = myThread(3, "Scorpion", 1, scorpion_list[2])
    thread25 = myThread(3, "Werewolf", 1, werewolf_list[2])
    thread26 = myThread(3, "Stump Snail", 1, snail_list[2])
    thread27 = myThread(3, "Cave Monster", 1, cavemonster_list[2])
    '''    BOSSES   '''
    thread30 = myThread(1, "King Beetle", 1, king_list[2])
    thread31 = myThread(1, "Tunnel Bear", 1, tunnel_list[2])
    thread32 = myThread(1, "Stick Bug", 1, stick_list[2])
    '''    QUESTS   '''
    thread40 = myThread(1, "Brown Bear Quest", 1, brownbear_list[2])
    thread41 = myThread(1, "Black Bear Quest", 1, blackbear_list[2])
    # Start new Threads
    '''   BOOSTERS  '''
    thread0.start()
    thread1.start()
    thread2.start()
    thread3.start()
    '''  DISPENSERS '''
    thread10.start()
    thread11.start()
    thread12.start()
    thread13.start()
    thread14.start()
    thread15.start()
    thread16.start()
    '''     MOBS    '''
    thread20.start()
    thread21.start()
    thread22.start()
    thread23.start()
    thread24.start()
    thread25.start()
    thread26.start()
    thread27.start()
    '''    BOSSES   '''
    thread30.start()
    thread31.start()
    thread32.start()
    '''    QUESTS   '''
    thread40.start()
    thread41.start()



def joinThreads():
    thread0.join()
    thread1.join()
    thread2.join()
    thread3.join()
    thread10.join()
    thread11.join()
    thread12.join()
    thread13.join()
    thread14.join()
    thread15.join()
    thread16.join()
    thread20.join()
    thread21.join()
    thread22.join()
    thread23.join()
    thread24.join()
    thread25.join()
    thread26.join()
    thread27.join()
    thread30.join()
    thread31.join()
    thread32.join()
    thread40.join()
    thread41.join()

    print ("Exiting Main Thread")

def doubleTimer():
    root = tk.Tk()
    PB = ProgressBar(root)
    root.mainloop()

startThreads()
doubleTimer()
