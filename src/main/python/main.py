from fbs_runtime.application_context.PySide6 import ApplicationContext, cached_property
from PySide6.QtWidgets import QMainWindow
from PySide6 import QtGui

import sys

from package.main_window import MainWindow


class AppContext(ApplicationContext):
    def run(self):
        window = MainWindow(ctx=appctxt)
        window.show()
        return self.app.exec()

    @cached_property
    def img_checked(self):
        return QtGui.QIcon(self.get_resource("images/checked.png"))

    @cached_property
    def img_unchecked(self):
        return QtGui.QIcon(self.get_resource("images/unchecked.png"))


if __name__ == '__main__':
    appctxt = AppContext()
    sys.exit(appctxt.run())

