#snippet
A simple program that allows you to choose from a list of templates and copy a snippet of text to your clipboard. Replaces `$name` with the name of the user who you are addressing. `$tech` is replaced with your name.

##Requirements
- You will need pyperclip in order for this program to work. You can install it like so `sudo pip install pyperclip`. 
- Please see template_example for the format that templates need to be in.
- I keep my `~/.config/snippets/` backed up in git so I have to remove files like README.md, .gitignore, etc. To do that I use a file called `non_template_files` that contains a `\n` separated list of files to be removed from the list that is generated when reading that directory into memory.
