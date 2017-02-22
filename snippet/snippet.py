#!/usr/bin/env python

import os
import sys
import operator
import argparse
from color import Color
c = Color()
try:
    import pyperclip
except ImportError:
    print c.colorize('You need to install pyperclip. sudo pip install pyperclip', Color.ERROR)
    print 'If you do not have pip installed you will need to install that', \
    'using your systems package manager.'
    sys.exit(9)

home = os.path.expanduser('~')
config_path = home + '/.config/snippets/'
config_filename = 'tech'
snippet_path = home + '/.config/snippets/'

class Snippet:
    def __init__(self, title, tag, text, user='$user', tech='$tech', extra_args=[]):
        self.user = user
        self.title = title
        self.tag = tag
        self.text = text
        self.tech = tech
        self.extra_args = extra_args
        self.expected_args = self.text.count('$arg')
        self.rows, self.cols = os.popen('stty size', 'r').read().split()
        self.rows = int(self.rows)
        self.cols = int(self.cols)

    def get_snippet(self):
        self.text = self.text.replace('$user', str(self.user))
        self.text = self.text.replace('$tech', str(self.tech))

        self.__replace_extra_args()

        return [self.title, self.text]

    def get_snippet_text(self):
        self.text = self.text.replace('$user', str(self.user))
        self.text = self.text.replace('$tech', str(self.tech))
        
        self.__replace_extra_args()
        
        return self.text

    def __replace_extra_args(self):
        if self.expected_args > len(self.extra_args):
            print c.colorize('You did not provide enough arguments to use this template.',
                            Color.WARNING)
            print 'This template expects {0} argument(s).'.format(self.expected_args)
            print '-' * self.cols
            self.text = self.text.replace('$arg', c.colorize('$arg', Color.RED))
            print self.text
            sys.exit(2)
            
        if self.extra_args:
            for i, arg in enumerate(self.extra_args):
                arg_to_replace = '$arg{0}'.format(i + 1)
                self.text = self.text.replace(arg_to_replace, arg)

    def __str__(self):
        title, text = self.get_snippet()
        return '-' * self.cols + '\n' + title + '-' * self.cols + '\n' + text

def missing_config():
    print c.colorize('You must have a config file located at ~/.config/snippets/tech that contains '
    'your full name as the only line of text. This will be used as your signature when signing '
    'templates.', Color.ERROR)
    choice = raw_input('Would you like to create this file now (y\\N): ')
    if choice != 'y':
        sys.exit(1)
    if not os.path.exists(config_path):
        os.makedirs(config_path)
    name = raw_input('Please enter your name as you would like it to ' +
            'appear in your signature: ')
    if not name:
        print 'You did not enter anything.'
        sys.exit(8)
    with open(config_path + config_filename, 'w') as tech_file:
        tech_file.write(name)
    print 'Now rerun this program and it should work! :)'
    sys.exit(2)

def choose_snippet(name, tech, silent, extra_args):
    snippet_files = [f for f in os.listdir(snippet_path) 
                    if os.path.isfile(os.path.join(snippet_path, f))]
    # Because the $tech file lives in ~/.config/snippets as well, we must
    # remove it, otherwise the program is a little off. 
    snippet_files.remove('tech')

    # The non_template_files is a text file that gets read if it exist and
    # contains things like .gitignore, a README, etc. You can add anything you
    # like to yours. This is to remove anything that is not a template from
    # ~/.config/snippets, if non_template_files does not exist then this will
    # assume that you do not have anything that needs to be removed.

    # This line is here because I discovered a bug that if you make a symlink
    # and then run this program it looked for the ntf file in the symlinks path
    # instead of where the program was actually being run from. To fix that we
    # use the realpath which follows symlinks correctly. The last 10 characters
    # are trimmed off because it contains the filename of this program which is
    # not needed.
    ntf_path = os.path.realpath(__file__)[:-10] 
    
    if os.path.isfile(ntf_path + '/non_template_files'):
        with open(ntf_path + '/non_template_files', 'r') as ntf:
            for line in ntf.readlines():
                snippet_files.remove(line.strip())

    snippets = []
    for snippet in snippet_files:
        with open(snippet_path + snippet, 'r') as s:
            snippets.append(Snippet(s.readline(), s.readline(), s.read(), 
                                    name, tech, extra_args))

    snippets.sort(key=operator.attrgetter('tag'))
    if len(snippets) == 0:
        print c.colorize('You do not have any snippets in ~/.config/snippets/', Color.ERROR)
        sys.exit(3)

    for i, snippet in enumerate(snippets):
        print "{0:20} {1:3}: {2}".format(snippet.tag.strip(), i + 1, 
                                         snippet.title),

    choice = raw_input('Which snippet would you like to use? ')
    try:
        choice = int(choice)
        if choice < 1:
            print c.colorize('You must enter a positive number.', Color.ERROR)
            sys.exit(4)
    except ValueError:
        print c.colorize('You must enter a number.', Color.ERROR)
        sys.exit(5)

    if not silent:
        print snippets[int(choice) - 1]
    pyperclip.copy(snippets[int(choice) - 1].get_snippet_text())

def load_snippet_from_file(snippet, name, tech, extra_args):
    try:
        with open(snippet_path + snippet) as s:
            snippet = Snippet(s.readline(), s.readline(), s.read(), name, tech, extra_args)
            pyperclip.copy(snippet.get_snippet_text())
    except IOError:
        print c.colorize('Sorry that file could not be found.', Color.ERROR)

def main():
    parser = argparse.ArgumentParser(description='Copies snippets into your clipboard and addresses user personally. Signs snippets with your signature.')
    parser.add_argument('--name', '-n', nargs='?', help='first or full name of the user, if using full name add double quotes (ie. "Lucas McCoy")')
    parser.add_argument('--file', '-f', nargs='?', help='provide a filename to skip prompts, requires -n and implies -s')
    parser.add_argument('--silent', '-s', action='store_true', help='only copy to clipboard, do not display in terminal') 
    args, unknown = parser.parse_known_args()

    if not os.path.exists(config_path + config_filename):
        missing_config()

    # --file requires -n because this is meant to be used for aliases.
    if args.file and not args.name:
        print c.colorize('If you use --file or -f you must provide -n as well.', Color.ERROR)
        sys.exit(6)

    name = '$user'
    if args.name:
        name = args.name
    else:
        name = raw_input('Who are you sending this snippet to? ')
        
    tech = ''
    with open(config_path + config_filename, 'r') as config:
        tech = config.readline() 
        tech = tech.strip()

    if args.file:
        load_snippet_from_file(args.file, name, tech, unknown) 
        sys.exit(0)

    if args.silent:
        choose_snippet(name, tech, True, unknown)
    else:
        choose_snippet(name, tech, False, unknown)

if __name__ == '__main__':
    try:
        main() 
    except KeyboardInterrupt as e:
        # I still cannot figure out why hitting Ctrl-C does not kill this
        # program immediately. It seems to be implementation specific and
        # related to readline. See the linked mailing list for more info:
        # https://mail.python.org/pipermail/python-list/1999-October/011368.html
        # I even tried implementing my own signal handler and this did not force
        # the program to terminate when Ctrl-C was pressed. I've spent more time
        # trying to find a solution to this than I did on this entire script.
        sys.exit(100)
