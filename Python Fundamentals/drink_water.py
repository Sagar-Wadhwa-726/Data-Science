import time
from plyer import notification

def remind_to_drink_water():
    while True:
        notification.notify(
            title="Drink Water Reminder",
            message="It's time to drink water! Stay hydrated for better health.",
            app_name="Water Reminder",
            timeout=10  # Notification will stay for 10 seconds
        )
        time.sleep(3)  # Wait for 1 hour (3600 seconds)

if __name__ == "__main__":
    remind_to_drink_water()