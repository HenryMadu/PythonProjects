from plyer import notification
import time

while True:
    notification.notify(
    title= 'Hi There',
    message= 'Hey Henry, Take a Break from your computer',
    app_name= 'Python Clcoding'
    )
    time.sleep(5)
