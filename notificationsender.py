import platform
from win10toast import ToastNotifier

# maybe eventually make this call another file for each operating system, so the code can work on any OS
# windowsNotif(notification_content)

# print(platform.system())

def notify(heading, body, icon, time):
    notifier = ToastNotifier()

    notifier.show_toast(
                    heading,
                    body,
                    icon_path = icon,
                    duration = time
                    )