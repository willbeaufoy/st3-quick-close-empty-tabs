import os
import sublime_plugin

class QuickCloseEmptyTab(sublime_plugin.EventListener):

    def on_window_command(self, window, command_name, args):
        if command_name == 'close':
            view = window.active_view()
            # Ensure file does not exist where it has been 'created'
            # (we don't want this behaviour for existing files),
            # and that it is empty. If so, set its scratch value so it
            # will close without prompting to save.
            if not os.path.isfile(view.file_name()) and view.size() == 0:
                view.set_scratch(True)
