from setuptools import setup, find_packages

with open('requirements.txt') as fh:
    reqs = fh.read().splitlines()

setup(

    name='newapp',
    version='0.0.1',
    url='https://github.com/jlandercy/newapp',
    license='GPL v.3',
    author='Jean Landercy',
    author_email='jeanlandercy@live.com',
    description='Minimal Django Package',

    packages=find_packages(exclude=[]),
    package_data={
       'newapp': []
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
        'console_scripts': []
    },
    zip_safe=False,

)
