from setuptools import setup

long_description = """
With the help of an options spec string, easily parse command-line options.

An options spec is made up of two parts, separated by a line with two dashes.
The first part is the synopsis of the command and the second one specifies
options, one per line.

Each non-empty line in the synopsis gives a set of options that can be used
together.

Option flags must be at the begining of the line and multiple flags are
separated by commas. Usually, options have a short, one character flag, and a
longer one, but the short one can be omitted.

Long option flags are used as the option's key for the OptDict produced when
parsing options.

When the flag definition is ended with an equal sign, the option takes one
string as an argument. Otherwise, the option does not take an argument and
corresponds to a boolean flag that is true when the option is given on the
command line.

The option's description is found at the right of its flags definition, after
one or more spaces. The description ends at the end of the line. If the
description contains text enclosed in square brackets, the enclosed text will
be used as the option's default value.

Options can be put in different groups. Options in the same group must be on
consecutive lines. Groups are formed by inserting a line that begins with a
space. The text on that line will be output after an empty line.
"""

setup(
    name='Options',
    version='0.1',
    description='Command-line options parser.',
    long_description=long_description,

    author='Avery Pennarun',
    author_email='apenwarr gmail',
    license='Simplified BSD',
    url='https://github.com/Singletoned/options',

    py_modules=['options'],

    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
