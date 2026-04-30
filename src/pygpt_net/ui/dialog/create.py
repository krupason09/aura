from pygpt_net.ui.widget.dialog.create import CreateDialog
from pygpt_net.utils import trans


class Create:
    def __init__(self, window=None):
        """
        Create dialog

        :param window: Window instance
        """
        self.window = window

    def setup(self):
        """Setup create dialog"""
        id = 'create'
        self.window.ui.dialog[id] = CreateDialog(self.window, id)
        self.window.ui.dialog[id].setWindowTitle(trans("dialog.create.title"))
