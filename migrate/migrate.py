#!/usr/bin/env python3

import os
import sys
import shutil
import argparse


class WindowsMigrate:
    HOME = os.path.expanduser('~')
    path = ''
    dup_count = 0

    def __init__(self):
        pass

    def initial_cleanup(self):
        # The first thing we need to do is delete .macromedia as it is not needed and
        # usually contains file paths longer than 260 characters.
        shutil.rmtree(self.HOME + '/.macromedia', ignore_errors=True)
        shutil.rmtree(self.HOME + '/.cache/mozilla/firefox', ignore_errors=True)

    def check_dupes(self, name, new_name, ext):
        if os.path.isfile(self.path + new_name + ext) and name != (new_name + ext):
            self.dup_count += 1
            new_name += str(self.dup_count)

    def fix_filenames(self, preview=False):
        valid_chars="-_.() abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

        # After I'm finished testing this os.walk will just be called on /home.
        # For now however I'm just calling it on test data.
        for root, dirs, files in os.walk(self.HOME + '/python/migrate/test_data'):
            self.dup_count = 0
            self.path = root + '/'
            for name in files:
                if len(name) > 255:
                    # TODO: Truncate filename.
                    print('File {0} needs to be shortened.'.format(name))

                # Create a copy of the filename to work with. Next we grab the file extension
                # for use later on. Then we remove any invalid characters.
                new_name, ext = os.path.splitext(name)
                new_name = ''.join(c for c in new_name if c in valid_chars)
                ext = ''.join(c for c in ext if c in valid_chars)

                self.check_dupes(name, new_name, ext)

                try:
                    if name != (new_name + ext):
                        print('Renaming {old} -> {new}{ext}'.format(old=name, new=new_name, ext=ext))
                        self.check_dupes(name, new_name, ext)
                        if preview is False:
                            os.rename(self.path + name, self.path + new_name + ext)
                except OSError as e:
                    print('Unable to rename file {0}.'.format(name))
                    print(e)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Prep files to be moved to Windows from *nix.')
    parser.add_argument('--debug', action='store_true', help='debug mode is used for testing this script')
    parser.add_argument('--preview', '-p', action='store_true', help='show what files will be renamed, but does NOT rename them.')
    args = parser.parse_args()

    migration = WindowsMigrate()

    if args.preview:
        migration.fix_filenames(preview=True)
        sys.exit(0)

    if args.debug:
        migration.fix_filenames()
        sys.exit(0)

    print("You should not be running this on your machine. It will delete", end=' ')
    print("several files and rename others.")
