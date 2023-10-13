import pytest
import datetime
import pytz

# Define a list of timezone names you want to log
timezones_to_log = ["Turkey", "US/Eastern", "Asia/Kolkata"]

@pytest.fixture
def log_execution_time():
    # This fixture will yield the current time in various timezones
    time_in_timezones = [datetime.datetime.now(pytz.timezone(zone)) for zone in timezones_to_log]
    print(time_in_timezones)
    return time_in_timezones
