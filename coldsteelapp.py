import tkinter as tk
import tkinter.ttk as ttk
import tkinter.filedialog as filedialog
import tkinter.messagebox as messagebox
import os

class ColdSteelApp:
    def __init__(self, master=None):
        # build ui
        # main frame
        self.frameMain = ttk.Frame(master)

        # general information frame
        # game directory
        self.frameGeneral = ttk.Labelframe(self.frameMain)
        self.lbDirectory = ttk.Label(self.frameGeneral)
        self.lbDirectory.config(text='Game Location')
        self.lbDirectory.grid(padx='5', pady='5', sticky='w')
        self.lbDirectory.rowconfigure('0', minsize='0')
        self.entryDirectory = ttk.Entry(self.frameGeneral)
        self.gameDirectory = tk.StringVar()
        self.entryDirectory.config(textvariable=self.gameDirectory, width='60')
        self.entryDirectory.grid(column='1', padx='5', pady='5', row='0', sticky='ew')
        self.btnBrowse = ttk.Button(self.frameGeneral)
        self.btnBrowse.config(text='Browse')
        self.btnBrowse.grid(column='2', padx='5', pady='5', row='0', sticky='ew')
        self.btnBrowse.configure(command=self.selectDirectory)
        # randomizer seed
        self.lbSeed = ttk.Label(self.frameGeneral)
        self.lbSeed.config(text='Randomizer Seed')
        self.lbSeed.grid(column='0', padx='5', pady='5', row='1', sticky='w')
        self.entrySeed = ttk.Entry(self.frameGeneral)
        self.seed = tk.StringVar()
        self.entrySeed.config(textvariable=self.seed, width='60')
        self.entrySeed.grid(column='1', padx='5', pady='5', row='1', sticky='ew')
        self.entrySeed.columnconfigure('1', minsize='0')
        self.frameGeneral.config(height='200', text='General Information', width='200')
        self.frameGeneral.grid(columnspan='2', padx='5', pady='5', sticky='ew')

        # character randomizer frame
        # base stat
        self.frameCharacter = ttk.Labelframe(self.frameMain)
        self.cbtnBase = ttk.Checkbutton(self.frameCharacter)
        self.randomizeBase = tk.IntVar()
        self.cbtnBase.config(state='normal', text='Randomize Base Stat', variable=self.randomizeBase)
        self.cbtnBase.grid(columnspan='3', padx='5', pady='5', sticky='w')
        self.lbBaseVariance = ttk.Label(self.frameCharacter)
        self.lbBaseVariance.config(text='Variance (10-100)')
        self.lbBaseVariance.grid(column='0', padx='5', pady='5', row='1', sticky='w')
        self.spinBase = ttk.Spinbox(self.frameCharacter)
        self.baseVariance = tk.IntVar(value=20)
        self.spinBase.config(from_='10', increment='5', justify='right', textvariable=self.baseVariance)
        self.spinBase.config(to='100', width='5', wrap='true')
        self.spinBase.grid(column='1', padx='5', pady='5', row='1', sticky='e')
        # stat growth
        self.cbtnGrowth = ttk.Checkbutton(self.frameCharacter)
        self.randomizeGrowth = tk.IntVar()
        self.cbtnGrowth.config(text='Randomize Stat Growth', variable=self.randomizeGrowth)
        self.cbtnGrowth.grid(column='0', columnspan='3', padx='5', pady='5', row='2', sticky='w')
        self.lbGrowthVariance = ttk.Label(self.frameCharacter)
        self.lbGrowthVariance.config(text='Variance (10-100)')
        self.lbGrowthVariance.grid(column='0', padx='5', pady='5', row='3', sticky='w')
        self.spinbase_2 = ttk.Spinbox(self.frameCharacter)
        self.growthVariance = tk.IntVar(value=20)
        self.spinbase_2.config(from_='10', increment='5', justify='right', textvariable=self.growthVariance)
        self.spinbase_2.config(to='100', width='5', wrap='true')
        self.spinbase_2.grid(column='1', padx='5', pady='5', row='3', sticky='e')
        # craft
        self.cbtnCraft = ttk.Checkbutton(self.frameCharacter)
        self.randomizeCraft = tk.IntVar()
        self.cbtnCraft.config(text='Randomize Craft (EXPERIMENTAL)', variable=self.randomizeCraft)
        self.cbtnCraft.grid(column='0', columnspan='3', padx='5', pady='5', row='4', sticky='w')
        self.frameCharacter.config(height='200', text='Character', width='200')
        self.frameCharacter.grid(column='0', padx='5', pady='5', row='1', sticky='nsew')

        # orbment randomizer frame
        # base EP
        self.frameOrbment = ttk.Labelframe(self.frameMain)
        self.cbtnBaseEP = ttk.Checkbutton(self.frameOrbment)
        self.randomizeBaseEP = tk.IntVar()
        self.cbtnBaseEP.config(text='Randomize Base EP', variable=self.randomizeBaseEP)
        self.cbtnBaseEP.grid(columnspan='2', padx='5', pady='5', sticky='w')
        # EP growth
        self.cbtnEPGrowth = ttk.Checkbutton(self.frameOrbment)
        self.randomizeEPGrowth = tk.IntVar()
        self.cbtnEPGrowth.config(text='Randomize EP Growth', variable=self.randomizeEPGrowth)
        self.cbtnEPGrowth.grid(column='0', columnspan='2', padx='5', pady='5', row='1', sticky='w')
        # orbment line
        self.cbtnOrbmentLine = ttk.Checkbutton(self.frameOrbment)
        self.randomizeOrbmentLine = tk.IntVar()
        self.cbtnOrbmentLine.config(text='Randomize Orbment Line', variable=self.randomizeOrbmentLine)
        self.cbtnOrbmentLine.grid(column='0', columnspan='2', padx='5', pady='5', row='2', sticky='w')
        self.lbMaxLine = ttk.Label(self.frameOrbment)
        self.lbMaxLine.config(text='Max amount of lines (1-8)')
        self.lbMaxLine.grid(column='0', padx='5', pady='5', row='3', sticky='w')
        self.spinMaxLine = ttk.Spinbox(self.frameOrbment)
        self.maxLine = tk.IntVar(value=4)
        self.spinMaxLine.config(from_='1', increment='1', justify='right', textvariable=self.maxLine)
        self.spinMaxLine.config(to='8', width='5', wrap='true')
        self.spinMaxLine.grid(column='1', padx='5', pady='5', row='3', sticky='e')
        self.lbMinSlot = ttk.Label(self.frameOrbment)
        self.lbMinSlot.config(text='Min amount of element slot (0-8)')
        self.lbMinSlot.grid(column='0', padx='5', pady='5', row='4', sticky='w')
        self.spinMinSlot = ttk.Spinbox(self.frameOrbment)
        self.minSlot = tk.IntVar(value=0)
        self.spinMinSlot.config(from_='0', increment='1', justify='right', textvariable=self.minSlot)
        self.spinMinSlot.config(to='8', width='5', wrap='true')
        self.spinMinSlot.grid(column='1', padx='5', pady='5', row='4', sticky='e')
        self.lbMaxSlot = ttk.Label(self.frameOrbment)
        self.lbMaxSlot.config(text='Max amount of element slot (0-8)')
        self.lbMaxSlot.grid(column='0', padx='5', pady='5', row='5', sticky='w')
        self.spinMaxSlot = ttk.Spinbox(self.frameOrbment)
        self.maxSlot = tk.IntVar(value=4)
        self.spinMaxSlot.config(from_='0', increment='1', justify='right', textvariable=self.maxSlot)
        self.spinMaxSlot.config(to='8', width='5', wrap='true')
        self.spinMaxSlot.grid(column='1', padx='5', pady='5', row='5', sticky='e')
        # master quartz
        self.randomizeMasterQuartz = tk.IntVar()
        self.cbtnOrbmentLine.config(text='Reshuffle Master Quartz (EXPERIMENTAL)', variable=self.randomizeMasterQuartz)
        self.cbtnOrbmentLine.grid(column='0', columnspan='2', padx='5', pady='5', row='6', sticky='w')
        self.frameOrbment.config(height='200', text='Orbment', width='200')
        self.frameOrbment.grid(column='1', padx='5', pady='5', row='1', sticky='nsew')

        # enemy randomizer frame
        # enemy stat
        self.lbEnemy = ttk.Labelframe(self.frameMain)
        self.cbtnEnemyStat = ttk.Checkbutton(self.lbEnemy)
        self.randomizeEnemyStat = tk.IntVar()
        self.cbtnEnemyStat.config(text='Randomize Enemy Stat', variable=self.randomizeEnemyStat)
        self.cbtnEnemyStat.grid(columnspan='2', padx='5', pady='5', sticky='w')
        self.lbEnemyStatVariance = ttk.Label(self.lbEnemy)
        self.lbEnemyStatVariance.config(text='Variance (10-100)')
        self.lbEnemyStatVariance.grid(column='0', padx='5', pady='5', row='1', sticky='w')
        self.spinEnemyStat = ttk.Spinbox(self.lbEnemy)
        self.enemyStatVariance = tk.IntVar(value=20)
        self.spinEnemyStat.config(from_='10', increment='5', justify='right', textvariable=self.enemyStatVariance)
        self.spinEnemyStat.config(to='100', width='5', wrap='true')
        self.spinEnemyStat.grid(column='1', padx='5', pady='5', row='1', sticky='w')
        # enemy ele res
        self.cbtnEnemyEleRes = ttk.Checkbutton(self.lbEnemy)
        self.randomizeEnemyEleRes = tk.IntVar()
        self.cbtnEnemyEleRes.config(text='Randomize Enemy Elemental Efficacy', variable=self.randomizeEnemyEleRes)
        self.cbtnEnemyEleRes.grid(columnspan='2', padx='5', pady='5', row='2', sticky='w')
        # enemy affliction res
        self.cbtnEnemyAfflictionRes = ttk.Checkbutton(self.lbEnemy)
        self.randomizeEnemyAfflictionRes = tk.IntVar()
        self.keepDeathBlow = tk.IntVar()
        self.cbtnEnemyAfflictionRes.config(text='Randomize Enemy Aliment Efficacy', variable=self.randomizeEnemyAfflictionRes)
        self.cbtnEnemyAfflictionRes.grid(columnspan='2', padx='5', pady='5', row='3', sticky='w')
        self.cbtnEnemyAfflictionRes.config(text='Keep Deathblow/Vanish/Petrify Efficacy', variable=self.keepDeathBlow)
        self.cbtnEnemyAfflictionRes.grid(columnspan='2', padx='25', pady='5', row='4', sticky='w')
        # enemy unbalance res
        self.cbtnEnemyUnbalanceRes = ttk.Checkbutton(self.lbEnemy)
        self.randomizeEnemyUnbalanceRes = tk.IntVar()
        self.cbtnEnemyUnbalanceRes.config(text='Randomize Enemy Unbalance Efficacy', variable=self.randomizeEnemyUnbalanceRes)
        self.cbtnEnemyUnbalanceRes.grid(columnspan='2', padx='5', pady='5', row='5', sticky='w')
        self.lbEnemy.config(height='200', text='Enemy', width='200')
        self.lbEnemy.grid(column='0', padx='5', pady='5', row='2', sticky='nsew')

        # button frame
        self.frameButton = ttk.Frame(self.frameMain)
        self.btnRandomize = ttk.Button(self.frameButton)
        self.btnRandomize.config(text='Randomize!')
        self.btnRandomize.pack(anchor='center', expand='true', fill='both', padx='5', pady='5', side='top')
        self.btnRandomize.configure(command=self.randomize)
        self.frameButton.config(height='200', width='200')
        self.frameButton.grid(column='1', padx='5', pady='5', row='2', sticky='nsew')
        self.frameMain.config(height='200', width='200')
        self.frameMain.grid(sticky='nsew')

        # progress frame
        self.frameProgress = ttk.Frame(self.frameMain)
        self.progressValue = tk.StringVar(value='Ready')
        self.lbProgress = ttk.Label(self.frameProgress)
        self.lbProgress.config(textvariable=self.progressValue)
        self.lbProgress.grid(column='0', row='0', columnspan='2', padx='5', pady='5', sticky='w')
        self.frameProgress.grid(column='0', row='3', padx='5', pady='5', columnspan='2', sticky='nsew')

        # Main widget
        self.mainwindow = self.frameMain

        # setup
        self.randomizeBase.set(1)
        self.randomizeGrowth.set(1)
        self.randomizeCraft.set(0)

        self.randomizeBaseEP.set(1)
        self.randomizeEPGrowth.set(1)
        self.randomizeOrbmentLine.set(1)
        self.randomizeMasterQuartz.set(0)

        self.randomizeEnemyStat.set(1)
        self.randomizeEnemyEleRes.set(1)
        self.randomizeEnemyAfflictionRes.set(1)
        self.keepDeathBlow.set(0)
        self.randomizeEnemyUnbalanceRes.set(1)

    def selectDirectory(self):
        directory = filedialog.askdirectory()
        self.gameDirectory.set(directory)

    def randomize(self):
        if not self.gameDirectory.get():
            messagebox.showerror('No Directory', 'No game directory selected')
        else:
            if not os.path.exists(self.gameDirectory.get() + "/data"):
                messagebox.showerror('Invalid Directory', 'Invalid game directory')
            else:
                with open('result.txt', 'w') as resultfile:
                    resultfile.write('Randomizer Result\n')
                if self.randomizeBase.get():
                    self.progressValue.set('Randomizing Base Stat...')
                    import randomizer.status
                    randomizer.status.randomizeBase(self.gameDirectory.get() + '/data/text/dat_us/', self.seed.get(), self.baseVariance.get())
                if self.randomizeGrowth.get():
                    self.progressValue.set('Randomizing Stat Growth...')
                    import randomizer.status
                    randomizer.status.randomizeGrowth(self.gameDirectory.get() + '/data/text/dat_us/', self.seed.get(), self.growthVariance.get())
                if self.randomizeCraft.get():
                    self.progressValue.set('Randomizing Craft...')
                    import randomizer.craft
                    randomizer.craft.randomize(self.gameDirectory.get() + '/data/text/dat_us/', self.seed.get())
                if self.randomizeBaseEP.get() or self.randomizeEPGrowth.get():
                    self.progressValue.set('Randomizing EP...')
                    import randomizer.slot
                    randomizer.slot.randomizeEP(self.gameDirectory.get() + '/data/text/dat_us/', self.seed.get(), randomizeBase=self.randomizeBaseEP.get(), randomizeGrowth=self.randomizeEPGrowth.get())
                if self.randomizeOrbmentLine.get():
                    self.progressValue.set('Randomizing Orbment Line...')
                    import randomizer.orb
                    randomizer.orb.randomize(self.gameDirectory.get() + '/data/text/dat_us/', self.seed.get(), maxEleSlot=self.maxSlot.get(), minEleSlot=self.minSlot.get(), maxLine=self.maxLine.get())
                if self.randomizeMasterQuartz.get():
                    self.progressValue.set('Reshuffling Master Quartz...')
                    import randomizer.masterquartz
                    randomizer.masterquartz.randomizeMasterQuartzLocation(self.gameDirectory.get() + '/', self.seed.get())
                if self.randomizeEnemyStat.get() or self.randomizeEnemyEleRes.get() or self.randomizeEnemyAfflictionRes.get() or self.randomizeEnemyUnbalanceRes.get():
                    self.progressValue.set('Randomizing Enemies...')
                    import randomizer.mons
                    randomizer.mons.randomize(self.gameDirectory.get() + '/data/text/dat_us/', self.seed.get(), randomStat=self.randomizeEnemyStat.get(), randomEleRes=self.randomizeEnemyAfflictionRes.get(), randomAfflictionRes=self.randomizeEnemyAfflictionRes.get(), randomUnbalance=self.randomizeEnemyUnbalanceRes.get(), keepDeathblow=self.keepDeathBlow.get())

                messagebox.showinfo('Finished!', 'All Done!')
                self.progressValue.set('Ready')

    def run(self):
        self.mainwindow.mainloop()

if __name__ == '__main__':
    import tkinter as tk
    root = tk.Tk()
    root.title('ColdSteelRandomizer')
    root.resizable(False, False)
    app = ColdSteelApp(root)
    app.run()

