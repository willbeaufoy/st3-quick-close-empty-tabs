# Sublime Text 3 - Quick close empty tabs

- By default, Sublime Text 3 (ST3) will close a new tab opened with Ctrl+n without prompting to save it if the tab is empty (whether the tab has had text in it previously or not).
- However, if the new tab is a new file opened from the command line with the `subl` command, e.g. `subl newfile.md`, ST3 will prompt to save the file on closing even if it is empty.
- This can be annoying if you mistype a command intended to open an existing file, e.g. if the file is called `existingfile.md` but you type `subl existingfil.md`. To close this tab you then need to select 'Close Without Saving' when prompted.
- This package ensures newly created empty files will always be closed without prompting to save, even if opened using the `subl` command.

Installation
---------------

- This package is not in Package Control, so to install it, create a `quick-close-empty-tabs` directory in your `Packages` directory, and put the `quick_close.py` file in it.
- Tested with Sublime Text 3 Ubuntu 17.04.
