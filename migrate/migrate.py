#!/usr/bin/env python3

import os
import sys
import shutil
import argparse

HOME = os.path.expanduser('~')
#HOME = '/home' # TODO: Make sure to ignore the lost+found directory.

def initial_cleanup():
    # The first thing we need to do is delete .macromedia as it is not needed and
    # usually contains file paths longer than 260 characters.
    shutil.rmtree(HOME + '/.macromedia', ignore_errors=True)
    shutil.rmtree(HOME + '/.cache/mozilla/firefox', ignore_errors=True)

def fix_filenames(preview=False):
    valid_chars="-_.() abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

    # After I'm finished testing this os.walk will just be called on /home.
    # For now however I'm just calling it on test data.
    for root, dirs, files in os.walk(HOME + '/python/migrate/test_data'):
        dup_count = 0
        path = root + '/'
        for name in files:
            if len(name) > 255:
                # TODO: Truncate filename.
                print(name)

            # Create a copy of the filename to work with. Next we grab the file extension
            # for use later on. Then we remove any invalid characters.
            new_name = name
            ext = os.path.splitext(os.path.basename(path + new_name))[1]
            new_name = ''.join(c for c in new_name if c in valid_chars)

            if os.path.isfile(path + name) and name != new_name:
                if os.path.exists(path + name):
                    dup_count += 1
                new_name = os.path.splitext(os.path.basename(path + new_name))[0]
                new_name += str(dup_count)
                new_name += ext
                print('Renaming {old} -> {new}'.format(old=name, new=new_name))

            try:
                if preview is False:
                    os.rename(path + name, path + new_name)
            except OSError as e:
                print('Unable to rename file {0}.'.format(name))
                print(e)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Prep files to be moved to Windows from *nix.')
    parser.add_argument('--debug', action='store_true', help='debug mode is used for testing this script')
    parser.add_argument('--preview', '-p', action='store_true', help='show what files will be renamed, but does NOT rename them.')
    args = parser.parse_args()
    
    if args.preview:
        fix_filenames(preview=True)
        sys.exit(0)

    if args.debug:
        fix_filenames()
        sys.exit(0)

    print("You should not be running this on your machine. It will delete", end=' ')
    print("several files and rename others.")
