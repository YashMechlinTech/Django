from django.dispatch import Signal, receiver

#Creating signals
notification =Signal()




#receiver function

@receiver(notification)
def show_notification(sender,**kwargs):
    print(sender)
    print(f'{kwargs}')
    print("Notification")