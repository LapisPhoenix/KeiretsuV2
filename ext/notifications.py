import platform
import win10toast

try:
    from desktop_notify.aio import Notify
    DESKTOP_NOTIFY_INSTALLED = True
except ImportError:
    DESKTOP_NOTIFY_INSTALLED = False


class Notifications:
    def show(self, title, message):
        if platform.system() == 'Windows':
            toaster = win10toast.ToastNotifier()
            toaster.show_toast(title, message, icon_path='keiretsu_v2.ico', duration=5)
        elif platform.system() == 'Linux' and DESKTOP_NOTIFY_INSTALLED:
            notify = Notify(summary=title, body=message, icon='keiretsu_v2.ico', timeout=5)
            notify.show()
