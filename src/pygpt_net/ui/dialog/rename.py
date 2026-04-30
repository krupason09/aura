from pygpt_net.ui.widget.dialog.rename import RenameDialog
from pygpt_net.utils import trans


class Rename:
    def __init__(self, window=None):
        """
        Rename dialog

        :param window: Window instance
        """
        self.window = window

    def setup(self):
        """Setup rename dialog"""
        id = 'rename'
        self.window.ui.dialog[id] = RenameDialog(self.window, id)
        self.window.ui.dialog[id].setWindowTitle(trans("dialog.rename.title"))
