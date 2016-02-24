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
import shutil

def initial_cleanup():
	# The first thing we need to do is delete .macromedia as it is not needed and
	# usually contains file paths longer than 260 characters.
	home = os.path.expanduser('~')
	shutil.rmtree(home + '/.macromedia', ignore_errors=True)

	valid_chars="-_.() abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

	for root, dirs, files in os.walk(home + '/python/migrate/'):
		for name in files:
			if len(name) > 255:
				print name

			new_name = ''.join(c for c in name if c in valid_chars)
			if os.path.exists(new_name):
				print 'Filename is already being used. Adding a 1'
				new_name += '1'
			os.rename(name, new_name)

if __name__ == '__main__':
	initial_cleanup()
