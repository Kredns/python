#!/usr/bin/env python

# This program is meant to allow the copying of files from RHEL 7 onto Windows
# and checks to make sure that no illegal characters are used. It also checks
# to make sure the paths and filenames are not over the character limit
# imposed by Windows. It's entirely possible this will work on other distros
# as well however I do not need this to work on them and will only ensure that
# it works for RHEL 7. If it works on anything else that is great, but it is
# entirely unsupported.
#
# Windows limits a single path to 260 characters. The following characters in a
# filename are illegal: \ / ? : * " > < |
# Also worth noting is that folders have a max length of 247 characters + <null>.

import os
import sys
import shutil

HOME = os.path.expanduser('~')

def initial_cleanup():
	# The first thing we need to do is delete .macromedia as it is not needed and
	# usually contains file paths longer than 260 characters.
	shutil.rmtree(HOME + '/.macromedia', ignore_errors=True)
	shutil.rmtree(HOME + '/.cache/mozilla/firefox', ignore_errors=True)

def fix_filenames():
	valid_chars="-_.() abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

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
	print "You should not be running this on your machine. It will delete your firefox cache."
	sys.exit(0)
