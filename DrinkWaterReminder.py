# For Mac 
import os
import time 

REPEAT_INTERVAL = 3600 # Repeat frequency in seconds

while True:
  command = "osascript -e \'say \"Hey Harry drink water\"\'; osascript -e \'display alert \"Hey Harry, Drink water\"\'"
  os.system(command)
  time.sleep(REPEAT_INTERVAL)




# For windows
from winotify import Notification, audio
import time

while True:

    toast = Notification(app_id="IMPORTANT",
                         title="Message", msg="please drink water",
                         duration="short", icon="C:\water.jpeg")
    toast.set_audio(audio.LoopingAlarm, loop=False)

    toast.show()
    time.sleep(3600)


# For windows (2)
from plyer import notification  # pip install plyer
import time


# Set up the notification
notification_title = "Notification Title"
notification_message = "Drink water"

notification_timeout = 5  # in seconds

# Display the notification
for i in range(5):
    notification.notify(
        title=notification_title,
        message=notification_message,
        timeout=notification_timeout,
    )