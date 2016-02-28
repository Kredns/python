#migrate.py

This program is meant to allow the copying of files from RHEL 7 onto Windows
and checks to make sure that no illegal characters are used. It also checks
to make sure the paths and filenames are not over the character limit
imposed by Windows. It's entirely possible this will work on other distros
as well however I do not need this to work on them and will only ensure that
it works for RHEL 7. If it works on anything else that is great, but it is
entirely unsupported.

Windows limits a single path to 260 characters. The following characters in a
filename are illegal: \ / ? : * " > < |
Also worth noting is that folders have a max length of 247 characters + <null>.
