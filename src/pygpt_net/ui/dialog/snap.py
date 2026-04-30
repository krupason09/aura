from pygpt_net.ui.widget.dialog.snap import SnapDialogCamera, SnapDialogAudioInput, SnapDialogAudioOutput


class Snap:
    def __init__(self, window=None):
        """
        Snap dialogs

        :param window: Window instance
        """
        self.window = window

    def setup(self):
        """Setup snap dialog"""
        self.window.ui.dialog['snap_camera'] = SnapDialogCamera(self.window)
        self.window.ui.dialog['snap_audio_input'] = SnapDialogAudioInput(self.window)
        self.window.ui.dialog['snap_audio_output'] = SnapDialogAudioOutput(self.window)
