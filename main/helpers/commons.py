from models import TimeStamp


def save_to_db(timestamp, value):
    ts = TimeStamp(timestamp, value)
    ts.save()
