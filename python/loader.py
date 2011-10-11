import os
import re

class EulerExcercise:
    def __init__(self, module):
        self.__module = None
        if type(module) == str:
            exec 'import {0}'.format(module)
            self.__module = eval(module)
        elif type(module).__name__ == 'module':
            self.__module = module
        if not self.__module:
            raise Exception('Failed to load module {0}'.format(module))
        docs = self.__module.__doc__.strip()
        self.__info = docs.split('\n')[0]
        self.__description = '\n'.join(docs.split('\n')[1:])
    def info(self):
        return self.__info
    def description(self):
        return self.__description
    def run(self):
        return self.__module.main()

# Load in all Project Euler exercises
pattern = re.compile('^e\d{3}\.py$')
modules = {}
for file_name in os.listdir('.'):
    if not os.path.isfile(file_name) or not pattern.match(file_name):
        continue
    module_name = file_name.split('.')[0]
    module_number = int(module_name.split('e')[1])
    modules[module_number] = EulerExcercise(module_name)

def main_loop():
    print 'Project Euler Excercises:\n\n'
    for i in sorted(modules.keys()):
        print '{0:03d} - {1}'.format(i, modules[i].info())
    selection = None
    while not selection in modules.keys():
        input = raw_input('Select a problem, or type q to quit: ').strip().lower()
        if input == 'q':
            exit()
        try:
            selection = int(input, 10)
        except:
            selection = 0
        if selection not in modules.keys():
            print '>>>Invalid selection<<<'
    module = modules[selection]
    print '\nMODULE: e{0}'.format(selection)
    print 'INFO: {0}\n\n{1}\n'.format(module.info(), module.description())
    raw_input('Press enter to run...')
    print
    module.run()
    raw_input('Press enter to continue...')

if __name__ == '__main__':
    while True:
        main_loop()
