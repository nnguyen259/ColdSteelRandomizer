from cx_Freeze import setup, Executable
import sys

# Dependencies are automatically detected, but it might need
# fine tuning.
buildOptions = dict(packages = ['randomizer'], excludes = [])

base = 'Win32GUI' if sys.platform=='win32' else None

executables = [
    Executable(script = 'coldsteelapp.py', base=base, targetName = 'CSRandomizer', icon = 'icon.ico')
]

setup(name='ColdSteelRandomizer',
      version = '1.0',
      description = 'Randomizer for Trails of Cold Steel 1',
      options = dict(build_exe = buildOptions),
      executables = executables)