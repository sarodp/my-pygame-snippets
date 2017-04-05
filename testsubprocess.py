# execute shell command
#
# An example in `python 2` on how you can run a shell command 
# from within your python program. 
# Further examples can be found in 
# the python 2 documentary on subprocess.
#
###############################################################################

#==================
# utils.py
#===================

# imports

import subprocess
from threading import Lock

# shell command execution

def run_command(command):
    # run command (can be an array (for parameters))
    p = subprocess.Popen(command, shell=True, \
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    # capture output and error
    (output, err) = p.communicate()
    # wait for command to end
    # TODO: really long running?
    status = p.wait()

    # decode output from byte string
    if output is not None:
        output = output.decode('utf-8')
    if err is not None:
        err = err.decode('utf-8')
    # return stdout, stderr, status code
    return (output, err, status)

def execute(command):
    debug('run command:', command)
    out, err, status = run_command(command)
    debug('-> exit status:', status)
    debug('output:', out)
    debug('error:', err)

###############################################################################
# logging

log_lock = Lock()

def log(level, msg, *args, **kwargs):
    log_lock.acquire(True)
    print '[' + level + ']', msg,
    for arg in args:
        print arg,
    for k, w in kwargs:
        print '[', k, '=', w, ']',
    print
    log_lock.release()

def info(msg, *args, **kwargs):
    log('INFO   ', msg, *args, **kwargs)

def verbose(msg, *args, **kwargs):
    log('VERBOSE', msg, *args, **kwargs)

def debug(msg, *args, **kwargs):
    log('DEBUG  ', msg, *args, **kwargs)

def error(msg, *args, **kwargs):
    log('ERROR  ', msg, *args, **kwargs)

def warning(msg, *args, **kwargs):
    log('WARNING', msg, *args, **kwargs)

'''
### file: program.py
```
python
#!/usr/bin/python
# -*- coding: utf-8 -*-

#
# program.py
#

# TODO: in the first line "/usr/bin/python" should point to your python binary
#       then you can execute the file with "./program.py"

###############################################################################
# imports

from utils import info, debug, error, \
                  execute, run_command
'''
###############################################################################
# functions

def main():
    # build your command
    command = 'ls -l'
    # run the command
    execute(command) 
    # or: run_command(command) if you don't want the logging
    run_command(command)

###############################################################################
# Entry-Point

if __name__ == '__main__':
    main()
