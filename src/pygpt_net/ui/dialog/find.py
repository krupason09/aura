from pygpt_net.ui.widget.dialog.find import FindDialog
from pygpt_net.utils import trans


class Find:
    def __init__(self, window=None):
        """
        Find dialog

        :param window: Window instance
        """
        self.window = window

    def setup(self):
        """Setup find dialog"""
        id = 'find'
        self.window.ui.dialog[id] = FindDialog(self.window, id)
        self.window.ui.dialog[id].setWindowTitle(trans("dialog.find.title"))
