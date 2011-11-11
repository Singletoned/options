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

>>> import options
>>> o = options.Options('''
... prog <options> [stuff...]
... --
... t test
... q,quiet quiet
... l,longoption= long option with parameters
... p= short option with parameters
... onlylong  long option with no short
... ''')
>>> o.show_usage()
usage: prog <options> [stuff...]

    -t                    test
    -q, --quiet           quiet
    -l, --longoption ...  long option with parameters
    -p ...                short option with parameters
    --onlylong            long option with no short
>>> opts, flags, extra = o.parse(
...       ["-t", "flange", "-p", "flibble", "--longoption=flimble"])
>>> opts
<OptDict {'onlylong': None, 'quiet': None, 'l': 'flimble', 'q': None, 'p': 'flibble', 't': 1, 'longoption': 'flimble'}>
>>> flags
[('-t', ''), ('-p', 'flibble'), ('--longoption', 'flimble')]
>>> extra
['flange']
>>> 
>>> opts.t
1
>>> opts.p
'flibble'
>>> opts.longoption
'flimble'
>>> opts.no_longoption
False
