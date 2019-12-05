from setuptools import setup

setup(
    name='F20SC-CW2',
    version='1',
    packages=['Logic', 'Testing', 'ErrorHandling'],
    url='https://github.com/jackow98/F20SC-CW2',
    license='',
    author='Jack Walker, Paul Cockburn',
    author_email='jw50@hw.ac.uk, psc4@hw.ac.uk',
    description='Data Analytics application',
    install_requires=[
        'mplcursors',
        'matplotlib',
        'pycountry',
        'pycountry-convert',
        'pydot',
        'user-agents',
        'Click'
    ],
)
