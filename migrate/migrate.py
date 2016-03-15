#!/usr/bin/env python3

import os
import sys
import shutil
import argparse


class WindowsMigrate:
    def __init__(self):
        self.changed = 0
        self.home = ''
        self.path = ''
        self.valid_chars = "-_.() abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

    def check_username(self, username):
        if not username:
            print('[ERROR]: You must enter a username!')
            return False

        if os.path.exists('/home/' + username):
            self.home = '/home/' + username
            return True
        else:
            print('[ERROR]: User not found')
            return False

    def initial_cleanup(self):
        # The first thing we need to do is delete .macromedia as it is not needed and
        # usually contains file paths longer than 260 characters.
        shutil.rmtree(self.home + '/.macromedia', ignore_errors=True)
        shutil.rmtree(self.home + '/.cache/mozilla/firefox', ignore_errors=True)

    def check_dupes(self, new_name, ext=''):
        dup_count = 0
        if os.path.exists(self.path + new_name + ext):
            while os.path.exists(self.path + new_name + ext):
                # This removes the dup_count from the filename so that the count is incremental.
                if dup_count > 0:
                    new_name = new_name[:-1]

                dup_count += 1
                new_name += str(dup_count)

        return new_name

    def trim_invalid_chars(self, string):
        return ''.join(c for c in string if c in self.valid_chars)

    def fix_filenames(self):
        for root, dirs, files in os.walk(self.home):
            self.path = root + '/'

            for name in files:
                if len(name) > 255:
                    # TODO: Truncate filename.
                    print('File {0} needs to be shortened.'.format(name))

                # Create a copy of the filename to work with. Next we grab the file extension
                # for use later on. Then we remove any invalid characters.
                new_name, ext = os.path.splitext(name)
                new_name = self.trim_invalid_chars(new_name)
                ext = self.trim_invalid_chars(ext)

                try:
                    if name != (new_name + ext):
                        print('Renaming file {old} to {new}{ext}.'.format(old=name, new=new_name, ext=ext))
                        new_name = self.check_dupes(new_name, ext)
                        os.rename(self.path + name, self.path + new_name + ext)
                        self.changed += 1
                except OSError as e:
                    print('Unable to rename file {0}.'.format(name))
                    print(e)

        for root, dirs, files in os.walk(self.home):
            self.path = root + '/'

            for directory in dirs:
                new_dir = self.trim_invalid_chars(directory)
                try:
                    if new_dir != directory:
                        print('Renaming directory {0} to {1}'.format(directory, new_dir))
                        new_dir = self.check_dupes(new_dir)
                        os.rename(self.path + directory, self.path + new_dir)
                        self.changed += 1
                except OSError as e:
                    print('Unable to rename directory {0}.'.format(directory))
                    print(e)

    def results(self):
        print('A total of {0} files and folders have been renamed.'.format(self.changed))

def main():
    parser = argparse.ArgumentParser(description='Prep files to be moved to Windows from *nix.')
    parser.add_argument('--debug', '-d', action='store_true', help='debug mode is used for testing this script')
    args = parser.parse_args()

    migration = WindowsMigrate()

    if args.debug:
        migration.home = os.path.expanduser('~') + '/test_data'
        migration.fix_filenames()
        sys.exit(0)

    print('Welcome to the Windows Migrate tool. This program will rename folders and files so that', end=' ')
    print('they can be moved to Windows without causing issues due to illegal characters or paths', end=' ')
    print('too long.\n')
    username = input('Please enter the username of the user who you are migrating: ')

    success = migration.check_username(username)
    if not success:
        print('Aborting...')
        sys.exit(1)

    migration.initial_cleanup()
    migration.fix_filenames()
    migration.results()

if __name__ == '__main__':
    main()
