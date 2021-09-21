import time
from plyer import notification


if _name_ == "_main_":
  while True:
     notification.notify(
        title = "Hey! welcome to new dawn of exploring" ,
        message = "Let your unique awesomeness and positive energy inspire confidence in others" ,
        app_icon = "E:\Desktop\icon.ico",
        timeout = 2,

    ) 
     time .sleep(60)
