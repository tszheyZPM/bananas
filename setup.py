from setuptools import setup

setup(name='bananas',
      version='0.1',
      # description='The funniest joke in the world',
      # url='http://github.com/storborg/funniest',
      # author='Flying Circus',
      # author_email='flyingcircus@example.com',
      # license='MIT',
      packages=['bananas'],
      # zip_safe=False
      )


'''
Note for Tsz 

the 'packages' key is used to list out all the modules and submodules you want to install. Instead of manually 
putting in every module (python script) you want users to install when they perform a `import bananas`, many 
people choose to use the `find_package()` from setup_tools to automatically identify all the modules. 

More documentation can be found here: https://setuptools.pypa.io/en/latest/userguide/quickstart.html
'''