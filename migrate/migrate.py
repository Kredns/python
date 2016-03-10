#!/usr/bin/env python

import os
import sys
import shutil

HOME = os.path.expanduser('~')
#HOME = '/home' # TODO: Make sure to ignore the lost+found directory.

def initial_cleanup():
    # The first thing we need to do is delete .macromedia as it is not needed and
    # usually contains file paths longer than 260 characters.
    shutil.rmtree(HOME + '/.macromedia', ignore_errors=True)
    shutil.rmtree(HOME + '/.cache/mozilla/firefox', ignore_errors=True)

def fix_filenames():
    valid_chars="-_.() abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

    # After I'm finished testing this os.walk will just be called on /home.
    # For now however I'm just calling it on test data.
    for root, dirs, files in os.walk(HOME + '/python/migrate/test_data'):
        dup_count = 0
        path = root + '/'
        for name in files:
            if len(name) > 255:
                # TODO: Truncate filename.
                print name

        # Create a copy of the filename to work with. Next we grab the file extension
        # for use later on. Then we remove any invalid characters.
        new_name = name
        ext = os.path.splitext(os.path.basename(path + new_name))[1]
        new_name = ''.join(c for c in new_name if c in valid_chars)

        # It's possible that the new name we have given the file could already be in
        # in use by another file that we have previously renamed. Consider the following:
        # bob::.txt and bob:.txt are files in a directory. When we rename the first file
        # it would be renamed to bob.txt, the next file would also be renamed to bob.txt
        # overwriting the data. To avoid loss of data we will check for this scenario and
        # if it occurs we add a 1 to the filename before the extension.
        if os.path.isfile(path + name) and name != new_name:
            new_name = os.path.splitext(os.path.basename(path + new_name))[0]
            new_name += str(dup_count)
            dup_count += 1
            new_name += ext
            print new_name

        try:
            os.rename(path + name, path + new_name)
        except OSError as e:
            print 'Unable to rename file %s.' % name
            print e

if __name__ == '__main__':
    print "You should not be running this on your machine. It will delete",
    print "several files and rename others."
    sys.exit(0)
