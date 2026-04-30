from pygpt_net.ui.widget.dialog.url import UrlDialog
from pygpt_net.utils import trans


class Url:
    def __init__(self, window=None):
        """
        URL dialog

        :param window: Window instance
        """
        self.window = window

    def setup(self):
        """Setup URL dialog"""
        id = 'url'
        self.window.ui.dialog[id] = UrlDialog(self.window, id)
        self.window.ui.dialog[id].setWindowTitle(trans("dialog.url.title"))
