from setuptools import setup, find_packages

with open('requirements.txt') as fh:
    reqs = fh.read().splitlines()

setup(

    name='newproject',
    version='0.0.1',
    url='https://github.com/jlandercy/newproject',
    license='GPL v.3',
    author='Jean Landercy',
    author_email='jeanlandercy@live.com',
    description='Minimal Python 3 Package',

    packages=find_packages(exclude=[]),
    package_data={
       'newproject': ['resources/*']
    },
    scripts=[],
    python_requires='>=3.6',
    install_requires=reqs,
    classifiers=[
         "Intended Audience :: Science/Research",
         "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
         "Operating System :: OS Independent",
         "Topic :: Scientific/Engineering",
    ],
    entry_points={
        'console_scripts': ['newproject=neproject._new:main']
    },
    zip_safe=False,

)
