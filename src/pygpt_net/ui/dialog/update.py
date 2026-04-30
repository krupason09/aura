from pygpt_net.ui.widget.dialog.update import UpdateDialog


class Update:
    def __init__(self, window=None):
        """
        Updater dialog

        :param window: Window instance
        """
        self.window = window

    def setup(self):
        """Setup updater dialog"""
        self.window.ui.dialog['update'] = UpdateDialog(self.window)
