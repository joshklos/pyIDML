from setuptools import setup

setup(name='pyidml',
      version='0.01',
      description='Python library for reading and manipulating IDML and ICML files',
      url='https://gitlab.com/joshklos/pyIDML/',
      author='Josh Klos',
      license='MIT',
      packages=['pyidml'],
      install_requires = [
          'lxml',
      ],
      zip_safe=False
)