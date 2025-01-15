import datetime as dt

def handler(event):
    print("Hello, I'm a cron job")
    print(f"Every hour, I'm printing this message" + str(dt.datetime.now()))
    print("Invoked with event: {}".format(event))