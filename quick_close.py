import sublime_plugin

class QuickCloseEmptyTab(sublime_plugin.EventListener):

    def on_window_command(self, window, command_name, args):
        if command_name == 'close':
            view = window.active_view()
            # Check to see if file is empty. If so, set its scratch value so it will close without prompting to save.
            if view.size() == 0:
                view.set_scratch(True)
