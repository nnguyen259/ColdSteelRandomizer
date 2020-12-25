import tkinter as tk
from tkinter import font
import tkinter.ttk as ttk
import tkinter.filedialog as filedialog
import tkinter.messagebox as messagebox
import os, threading

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
        self.entryDirectory.config(textvariable=self.gameDirectory, width='100')
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
        self.entrySeed.config(textvariable=self.seed, width='100')
        self.entrySeed.grid(column='1', padx='5', pady='5', row='1', sticky='ew')
        self.entrySeed.columnconfigure('1', minsize='0')
        self.frameGeneral.config(height='200', text='General Information', width='200')
        self.frameGeneral.grid(columnspan='3', padx='5', pady='5', sticky='ew')

        # character randomizer frame
        # base stat
        self.frameCharacter = ttk.Labelframe(self.frameMain)
        self.cbtnBase = ttk.Checkbutton(self.frameCharacter)
        self.randomizeBase = tk.IntVar()
        self.cbtnBase.config(state='normal', text='Randomize Base Stat', variable=self.randomizeBase)
        self.cbtnBase.grid(columnspan='3', padx='5', pady='5', sticky='w')
        self.lbBaseVariance = ttk.Label(self.frameCharacter)
        self.lbBaseVariance.config(text='Variance (10-100)')
        self.lbBaseVariance.grid(column='0', padx='5', pady='5', row='2', sticky='w')
        self.spinBase = ttk.Spinbox(self.frameCharacter)
        self.baseVariance = tk.IntVar(value=20)
        self.spinBase.config(from_='10', increment='5', justify='left', textvariable=self.baseVariance)
        self.spinBase.config(to='100', width='5', wrap='true')
        self.spinBase.grid(column='1', padx='5', pady='5', row='2', sticky='e')
        self.increaseBase = tk.IntVar()
        self.cbtnIncreaseBase = ttk.Checkbutton(self.frameCharacter)
        self.cbtnIncreaseBase.config(state='normal', text='Increase Base Stat', variable=self.increaseBase)
        self.cbtnIncreaseBase.grid(columnspan='3', padx='25', pady='5', sticky='w', row='1', column='0')
        # stat growth
        self.cbtnGrowth = ttk.Checkbutton(self.frameCharacter)
        self.randomizeGrowth = tk.IntVar()
        self.cbtnGrowth.config(text='Randomize Stat Growth', variable=self.randomizeGrowth)
        self.cbtnGrowth.grid(column='0', columnspan='3', padx='5', pady='5', row='3', sticky='w')
        self.lbGrowthVariance = ttk.Label(self.frameCharacter)
        self.lbGrowthVariance.config(text='Variance (10-100)')
        self.lbGrowthVariance.grid(column='0', padx='5', pady='5', row='4', sticky='w')
        self.spinGrowth = ttk.Spinbox(self.frameCharacter)
        self.growthVariance = tk.IntVar(value=20)
        self.spinGrowth.config(from_='10', increment='5', justify='left', textvariable=self.growthVariance)
        self.spinGrowth.config(to='100', width='5', wrap='true')
        self.spinGrowth.grid(column='1', padx='5', pady='5', row='4', sticky='e')
        # craft
        self.cbtnCraft = ttk.Checkbutton(self.frameCharacter)
        self.randomizeCraft = tk.IntVar()
        self.cbtnCraft.config(text='Randomize Craft (EXPERIMENTAL)', variable=self.randomizeCraft)
        self.cbtnCraft.grid(column='0', columnspan='3', padx='5', pady='5', row='5', sticky='w')
        self.cbtnOrginalCraft = ttk.Checkbutton(self.frameCharacter)
        self.originalCraft = tk.IntVar()
        self.cbtnOrginalCraft.config(text='Add Original Crafts', variable=self.originalCraft)
        self.cbtnOrginalCraft.grid(column='0', columnspan='3', padx='25', pady='5', row='6', sticky='w')
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
        self.spinMaxLine.config(from_='1', increment='1', justify='left', textvariable=self.maxLine)
        self.spinMaxLine.config(to='8', width='5', wrap='true')
        self.spinMaxLine.grid(column='1', padx='5', pady='5', row='3', sticky='e')
        self.lbMinSlot = ttk.Label(self.frameOrbment)
        self.lbMinSlot.config(text='Min amount of element slot (0-8)')
        self.lbMinSlot.grid(column='0', padx='5', pady='5', row='4', sticky='w')
        self.spinMinSlot = ttk.Spinbox(self.frameOrbment)
        self.minSlot = tk.IntVar(value=0)
        self.spinMinSlot.config(from_='0', increment='1', justify='left', textvariable=self.minSlot)
        self.spinMinSlot.config(to='8', width='5', wrap='true')
        self.spinMinSlot.grid(column='1', padx='5', pady='5', row='4', sticky='e')
        self.lbMaxSlot = ttk.Label(self.frameOrbment)
        self.lbMaxSlot.config(text='Max amount of element slot (0-8)')
        self.lbMaxSlot.grid(column='0', padx='5', pady='5', row='5', sticky='w')
        self.spinMaxSlot = ttk.Spinbox(self.frameOrbment)
        self.maxSlot = tk.IntVar(value=4)
        self.spinMaxSlot.config(from_='0', increment='1', justify='left', textvariable=self.maxSlot)
        self.spinMaxSlot.config(to='8', width='5', wrap='true')
        self.spinMaxSlot.grid(column='1', padx='5', pady='5', row='5', sticky='e')
        self.frameOrbment.config(height='200', text='Orbment', width='200')
        self.frameOrbment.grid(column='1', padx='5', pady='5', row='1', sticky='nsew')

        # enemy randomizer frame
        # enemy stat
        self.frameEnemy = ttk.Labelframe(self.frameMain)
        self.cbtnEnemyStat = ttk.Checkbutton(self.frameEnemy)
        self.randomizeEnemyStat = tk.IntVar()
        self.cbtnEnemyStat.config(text='Randomize Enemy Stat', variable=self.randomizeEnemyStat)
        self.cbtnEnemyStat.grid(columnspan='2', padx='5', pady='5', sticky='w')
        self.lbEnemyStatVariance = ttk.Label(self.frameEnemy)
        self.lbEnemyStatVariance.config(text='Variance (10-100)')
        self.lbEnemyStatVariance.grid(column='0', padx='5', pady='5', row='1', sticky='w')
        self.spinEnemyStat = ttk.Spinbox(self.frameEnemy)
        self.enemyStatVariance = tk.IntVar(value=20)
        self.spinEnemyStat.config(from_='10', increment='5', justify='left', textvariable=self.enemyStatVariance)
        self.spinEnemyStat.config(to='100', width='5', wrap='true')
        self.spinEnemyStat.grid(column='1', padx='5', pady='5', row='1', sticky='w')
        # enemy ele res
        self.cbtnEnemyEleRes = ttk.Checkbutton(self.frameEnemy)
        self.randomizeEnemyEleRes = tk.IntVar()
        self.cbtnEnemyEleRes.config(text='Randomize Enemy Elemental Efficacy', variable=self.randomizeEnemyEleRes)
        self.cbtnEnemyEleRes.grid(columnspan='2', padx='5', pady='5', row='2', sticky='w')
        # enemy affliction res
        self.cbtnEnemyAfflictionRes = ttk.Checkbutton(self.frameEnemy)
        self.randomizeEnemyAfflictionRes = tk.IntVar()
        self.keepDeathBlow = tk.IntVar()
        self.cbtnKeepDeathBlow = ttk.Checkbutton(self.frameEnemy)
        self.cbtnEnemyAfflictionRes.config(text='Randomize Enemy Aliment Efficacy', variable=self.randomizeEnemyAfflictionRes)
        self.cbtnEnemyAfflictionRes.grid(columnspan='2', padx='5', pady='5', row='3', sticky='w')
        self.cbtnKeepDeathBlow.config(text='Keep Deathblow/Vanish/Petrify Efficacy', variable=self.keepDeathBlow)
        self.cbtnKeepDeathBlow.grid(columnspan='2', padx='25', pady='5', row='4', sticky='w')
        # enemy unbalance res
        self.cbtnEnemyUnbalanceRes = ttk.Checkbutton(self.frameEnemy)
        self.randomizeEnemyUnbalanceRes = tk.IntVar()
        self.cbtnEnemyUnbalanceRes.config(text='Randomize Enemy Unbalance Efficacy', variable=self.randomizeEnemyUnbalanceRes)
        self.cbtnEnemyUnbalanceRes.grid(columnspan='2', padx='5', pady='5', row='5', sticky='w')
        self.frameEnemy.config(height='200', text='Enemy', width='200')
        self.frameEnemy.grid(column='0', padx='5', pady='5', row='2', sticky='nsew')

        # misc frame
        self.frameMisc = ttk.Labelframe(self.frameMain)
        self.cbtnIncreaseEXP = ttk.Checkbutton(self.frameMisc)
        self.increaseEXP = tk.IntVar()
        self.cbtnIncreaseEXP.config(text='Increase EXP Gain', variable=self.increaseEXP)
        self.cbtnIncreaseEXP.grid(padx='5', pady='5', row='0', sticky='w')

        self.cbtnIncreaseSepith = ttk.Checkbutton(self.frameMisc)
        self.increaseSepith = tk.IntVar()
        self.cbtnIncreaseSepith.config(text='Increase Sepith Gain', variable=self.increaseSepith)
        self.cbtnIncreaseSepith.grid(padx='5', pady='5', row='1', sticky='w')

        self.cbtnIncreaseSepithMass = ttk.Checkbutton(self.frameMisc)
        self.increaseSepithMass = tk.IntVar()
        self.cbtnIncreaseSepithMass.config(text='Increase Sepith Mass Gain', variable=self.increaseSepithMass)
        self.cbtnIncreaseSepithMass.grid(padx='5', pady='5', row='2', sticky='w')

        self.cbtnReduceSlotCost = ttk.Checkbutton(self.frameMisc)
        self.reduceSlotCost = tk.IntVar()
        self.cbtnReduceSlotCost.config(text='Reduce Slot Unlocking Cost', variable=self.reduceSlotCost)
        self.cbtnReduceSlotCost.grid(padx='5', pady='5', row='3', sticky='w')

        self.cbtnReplaceNeedleShoot = ttk.Checkbutton(self.frameMisc)
        self.replaceNeedleShoot = tk.IntVar()
        self.cbtnReplaceNeedleShoot.config(text='Replace Needle Shoot with La Forte', variable=self.replaceNeedleShoot)
        self.cbtnReplaceNeedleShoot.grid(padx='5', pady='5', row='4', sticky='w')

        self.cbtnRandomizeCook = ttk.Checkbutton(self.frameMisc)
        self.randomizeCook = tk.IntVar()
        self.cbtnRandomizeCook.config(text='Randomize Cookbook', variable=self.randomizeCook)
        self.cbtnRandomizeCook.grid(padx='5', pady='5', row='5', sticky='w')

        self.frameMisc.config(text='Misc.')
        self.frameMisc.grid(column='1', row='2', padx='5', pady='5', sticky='nsew')

        # master quartz frame
        self.frameMasterQuartz = ttk.Labelframe(self.frameMain)
        # shuffle master quartz
        self.randomizeMasterQuartz = tk.IntVar()
        self.cbtnMasterQuartz = ttk.Checkbutton(self.frameMasterQuartz)
        self.cbtnMasterQuartz.config(text='Reshuffle Master Quartz (EXPERIMENTAL)', variable=self.randomizeMasterQuartz)
        self.cbtnMasterQuartz.grid(column='0', columnspan='2', padx='5', pady='5', row='0', sticky='w')
        # normalize master quartz
        self.normalizeMasterQuartz = tk.IntVar()
        self.cbtnNormalizeMasterQuartz = ttk.Checkbutton(self.frameMasterQuartz)
        self.cbtnNormalizeMasterQuartz.config(text='Normalize Master Quartz Stats', variable=self.normalizeMasterQuartz)
        self.cbtnNormalizeMasterQuartz.grid(column='0', columnspan='2', padx='5', pady='5', row='1', sticky='w')
        # randomize master quartz art
        self.randomizeMQArt = tk.IntVar()
        self.cbtnRandomizeMQArt = ttk.Checkbutton(self.frameMasterQuartz)
        self.cbtnRandomizeMQArt.config(text='Randomize Master Quartz Arts', variable=self.randomizeMQArt)
        self.cbtnRandomizeMQArt.grid(column='0', columnspan='2', padx='5', pady='5', row='2', sticky='w')
        self.lbArtGainChance = ttk.Label(self.frameMasterQuartz)
        self.lbArtGainChance.config(text='Art Gain Chance (0-100)%')
        self.lbArtGainChance.grid(column='0', padx='5', pady='5', row='3', sticky='w')
        self.spinArtGain = ttk.Spinbox(self.frameMasterQuartz)
        self.artGainChance = tk.IntVar(value=60)
        self.spinArtGain.config(from_='0', increment='5', justify='left', textvariable=self.artGainChance)
        self.spinArtGain.config(to='100', width='5', wrap='true')
        self.spinArtGain.grid(column='1', padx='5', pady='5', row='3', sticky='w')

        # randomize chest
        self.randomizeChest = tk.IntVar()
        self.randomizeChestMode = tk.IntVar()
        self.randomizeChestMode.set(0)
        self.cbtnRandomizeChest = ttk.Checkbutton(self.frameMasterQuartz)
        self.cbtnRandomizeChest.config(text='Shuffle Chest Contents', variable=self.randomizeChest)
        self.rbtnMode1 = ttk.Radiobutton(self.frameMasterQuartz)
        self.rbtnMode1.config(text='Separated Pools', variable=self.randomizeChestMode, value=0)
        self.rbtnMode2 = ttk.Radiobutton(self.frameMasterQuartz)
        self.rbtnMode2.config(text='Combine Rare and Monster', variable=self.randomizeChestMode, value=1)
        self.rbtnMode3 = ttk.Radiobutton(self.frameMasterQuartz)
        self.rbtnMode3.config(text='Combine Everything', variable=self.randomizeChestMode, value=2)

        self.cbtnRandomizeChest.grid(column='0', row='4', padx='5', pady='5', sticky='w')
        self.rbtnMode1.grid(column='0', row='5', padx='25', pady='5', sticky='w')
        self.rbtnMode2.grid(column='0', row='6', padx='25', pady='5', sticky='w')
        self.rbtnMode3.grid(column='0', row='7', padx='25', pady='5', sticky='w')

        self.frameMasterQuartz.config(text='Master Quartz & Chest')
        self.frameMasterQuartz.grid(column='2', row='1', padx='5', pady='5', sticky='nsew')

        # button frame
        self.styleButton = ttk.Style()
        self.styleButton.configure('my.TButton', font=('Helvetica', 16))
        self.frameButton = ttk.Frame(self.frameMain)
        self.btnRandomize = ttk.Button(self.frameButton)
        self.btnRandomize.config(text='Randomize!')
        self.btnRandomize.pack(anchor='center', padx='5', pady='5', side='top', expand=True, fill='both')
        self.btnRandomize.configure(command=self.randomize, style='my.TButton')
        self.frameButton.grid(column='2', padx='5', pady='5', row='2', sticky='nsew', columnspan='2')
        self.frameMain.config(height='200', width='200')
        self.frameMain.grid(sticky='nsew')

        # progress frame
        self.frameProgress = ttk.Frame(self.frameMain)
        self.progressValue = tk.StringVar(value='Ready')
        self.lbProgress = ttk.Label(self.frameProgress)
        self.lbProgress.config(textvariable=self.progressValue)
        self.lbProgress.grid(column='0', row='0', columnspan='2', padx='5', pady='5', sticky='w')
        self.frameProgress.grid(column='0', row='4', padx='5', pady='5', columnspan='2', sticky='nsew')

        # Main widget
        self.mainwindow = self.frameMain

        # setup
        self.randomizeBase.set(1)
        self.randomizeGrowth.set(1)
        self.randomizeCraft.set(0)

        self.randomizeBaseEP.set(1)
        self.randomizeEPGrowth.set(1)
        self.randomizeOrbmentLine.set(1)

        self.randomizeEnemyStat.set(1)
        self.randomizeEnemyEleRes.set(1)
        self.randomizeEnemyAfflictionRes.set(1)
        self.keepDeathBlow.set(0)
        self.randomizeEnemyUnbalanceRes.set(1)

        self.increaseEXP.set(0)
        self.increaseSepith.set(0)
        self.increaseSepithMass.set(0)
        self.reduceSlotCost.set(0)

        self.randomizeMasterQuartz.set(0)
        self.normalizeMasterQuartz.set(0)
        self.randomizeMQArt.set(0)

    def updateCraft(self, quiet=True):
        def realUpdate():
            self.progressValue.set('Updating Craft Database...')
            with open('input/Crafts/crafts.csv', 'r+b') as craftFile, open('input/Crafts/original.csv', 'r+b') as orginalFile:
                import urllib3
                http = urllib3.PoolManager(timeout=5.0)
                try:
                    r = http.request('GET', 'https://github.com/nnguyen259/ColdSteelCrafts/raw/main/crafts.csv')

                    if r.status == 200:
                        craftFile.seek(0)
                        craftFile.truncate()
                        craftFile.write(r.data)
                    else:
                        raise Exception
                    
                    r = http.request('GET', 'https://github.com/nnguyen259/ColdSteelCrafts/raw/main/original.csv')

                    if r.status == 200:
                        orginalFile.seek(0)
                        orginalFile.truncate()
                        orginalFile.write(r.data)
                    else:
                        raise Exception

                    if not quiet:
                            messagebox.showinfo('Craft Updater', 'Succesfully update crafts database')
                except Exception:
                    print('Unexpected Error. Database not updated.')
                    if not quiet:
                        messagebox.showerror('Craft Updater', 'Unexpected Error.\nPlease try again later.')
            self.btnBrowse['state'] = 'normal'
            self.btnRandomize['state'] = 'normal'
            self.progressValue.set('Ready')

        self.btnBrowse['state'] = 'disabled'
        self.btnRandomize['state'] = 'disabled'
        threading.Thread(target=realUpdate).start()

    def selectDirectory(self):
        directory = filedialog.askdirectory()
        self.gameDirectory.set(directory)

    def randomize(self):
        def realRandomize():
            if not self.gameDirectory.get():
                messagebox.showerror('No Directory', 'No game directory selected')
            else:
                if not os.path.exists(self.gameDirectory.get() + "/data"):
                    messagebox.showerror('Invalid Directory', 'Invalid game directory')
                else:
                    try:
                        with open('result.txt', 'w') as resultfile:
                            resultfile.write('Randomizer Result\n')
                        if self.randomizeBase.get():
                            self.progressValue.set('Randomizing Base Stat...')
                            import randomizer.status
                            randomizer.status.randomizeBase(path=self.gameDirectory.get() + '/data/text/dat_us/', seed=self.seed.get(), 
                                                            variance=self.baseVariance.get(), increaseBase=self.increaseBase.get())
                        if self.randomizeGrowth.get():
                            self.progressValue.set('Randomizing Stat Growth...')
                            import randomizer.status
                            randomizer.status.randomizeGrowth(path=self.gameDirectory.get() + '/data/text/dat_us/', seed=self.seed.get(), variance=self.growthVariance.get())
                        if self.randomizeCraft.get():
                            self.progressValue.set('Randomizing Craft...')
                            import randomizer.craft
                            randomizer.craft.randomize(path=self.gameDirectory.get() + '/', seed=self.seed.get(), original=self.originalCraft.get())
                        if self.randomizeBaseEP.get() or self.randomizeEPGrowth.get():
                            self.progressValue.set('Randomizing EP...')
                            import randomizer.slot
                            randomizer.slot.randomizeEP(path=self.gameDirectory.get() + '/data/text/dat_us/', seed=self.seed.get(), 
                                                        randomizeBase=self.randomizeBaseEP.get(), randomizeGrowth=self.randomizeEPGrowth.get())
                        if self.randomizeOrbmentLine.get():
                            self.progressValue.set('Randomizing Orbment Line...')
                            import randomizer.orb
                            randomizer.orb.randomize(path=self.gameDirectory.get() + '/data/text/dat_us/', seed=self.seed.get(), 
                                                    maxEleSlot=self.maxSlot.get(), minEleSlot=self.minSlot.get(), maxLine=self.maxLine.get())
                        if self.randomizeMasterQuartz.get():
                            self.progressValue.set('Reshuffling Master Quartz...')
                            import randomizer.masterquartz
                            randomizer.masterquartz.randomizeMasterQuartzLocation(path=self.gameDirectory.get() + '/', seed=self.seed.get())

                        if self.randomizeChest.get():
                            self.progressValue.set('Reshuffling Chest Contents...')
                            import randomizer.chest
                            randomizer.chest.randomize(path=self.gameDirectory.get() + '/data/scripts/scena/dat_us/', seed=self.seed.get(), mode=self.randomizeChestMode.get())

                        if self.randomizeEnemyStat.get() or self.randomizeEnemyEleRes.get() or self.randomizeEnemyAfflictionRes.get() or self.randomizeEnemyUnbalanceRes.get() \
                            or self.increaseEXP.get() or self.increaseSepith.get() or self.increaseSepithMass.get():
                            self.progressValue.set('Randomizing Enemies...')
                            import randomizer.mons
                            randomizer.mons.randomize(path=self.gameDirectory.get() + '/data/text/dat_us/', seed=self.seed.get(), 
                                                    randomStat=self.randomizeEnemyStat.get(), randomEleRes=self.randomizeEnemyEleRes.get(), 
                                                    randomAfflictionRes=self.randomizeEnemyAfflictionRes.get(), randomUnbalance=self.randomizeEnemyUnbalanceRes.get(), 
                                                    keepDeathblow=self.keepDeathBlow.get(), increaseExp=self.increaseEXP.get(), 
                                                    increaseSepith=self.increaseSepith.get(), increaseMass=self.increaseSepithMass.get())
                        
                        if self.reduceSlotCost.get():
                            self.progressValue.set('Reducing Slot Cost...')
                            import randomizer.qol
                            randomizer.qol.reduceSlotCost(path=self.gameDirectory.get() + '/data/text/dat_us/', seed=self.seed.get())

                        if self.replaceNeedleShoot.get():
                            self.progressValue.set('Replacing Needle Shoot')
                            import randomizer.qol
                            randomizer.qol.replaceNeedleShoot(path=self.gameDirectory.get() + '/')

                        if self.randomizeCook.get():
                            self.progressValue.set('Randomizing Cook Book...')
                            import randomizer.notecook
                            randomizer.notecook.randomize(path=self.gameDirectory.get() + '/', seed=self.seed.get())

                        if self.normalizeMasterQuartz.get() or self.randomizeMQArt.get():
                            self.progressValue.set('Building Master Quartz')
                            import randomizer.masterquartz
                            randomizer.masterquartz.buildMasterQuartz(path=self.gameDirectory.get() + '/data/text/dat_us/', seed=self.seed.get(), 
                                                                    normalize=self.normalizeMasterQuartz.get(), randomizeArts=self.randomizeMQArt.get(), 
                                                                    artGainChance=self.artGainChance.get())

                        messagebox.showinfo('Finished!', 'All Done!')
                    except Exception as err:
                        import traceback
                        print(traceback.format_exc())
                        messagebox.showerror('FATAL ERROR', str(err))
            self.progressValue.set('Ready')
            self.btnRandomize['state'] = 'normal'

        self.btnRandomize['state'] = 'disabled'
        threading.Thread(target=realRandomize).start()

    def run(self):
        self.updateCraft()
        self.mainwindow.mainloop()

if __name__ == '__main__':
    import tkinter as tk
    root = tk.Tk()
    root.title('ColdSteelRandomizer')
    root.iconbitmap('icon.ico')
    root.resizable(False, False)
    app = ColdSteelApp(root)
    app.run()

