import os
from subprocess import call

def doWalk(libroot, path = '.', depth = 0):
    cmd = 'sed -i \'s/#include\s\+<' + libroot + '\/\([^>]\+\)>/#include "' + ('..\/'*depth) + '\\1"/\' ' + os.path.join(path, '*.hpp') + ' ' + os.path.join(path, '*.h')
    print cmd
    call(cmd, shell=True)
    for root, subFolders, files in os.walk(path):
        for folder in subFolders:
            doWalk(libroot, os.path.join(path, folder), depth + 1)

doWalk('websocketpp', os.path.join('.', 'websocketpp'))
