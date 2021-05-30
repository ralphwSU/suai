from setuptools import setup

setup(
   name='suai',
   version='0.1.0',
   author='Ralph Wojtowicz',
   author_email='rwojtowi@su.edu',
   packages=['suai', 'suai.base', 'suai.util', 'suai.search'],
   scripts=[],
   url='https://github.com/ralphwSU/suai',
   license='LICENSE.txt',
   description='Artificial Intelligence at Shenandoah University',
   long_description=open('README.txt').read(),
   install_requires=[
       "pytest",
   ],
)
