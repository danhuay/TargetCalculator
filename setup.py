from distutils.core import setup
import py2exe
setup(console=['atom_mass.py'],
        data_files = ['atomicmass.txt'])