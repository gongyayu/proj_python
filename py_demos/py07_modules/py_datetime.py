from datetime import datetime, timedelta
from py_mod import st_code,st_markline

### StartofFunc###

def py_datetime():
    # Calculate dates
    today = datetime.now()
    week_ago = today - timedelta(days=7)

    # Format dates for API (YYYY-MM-DD)
    start_date = week_ago.strftime("%Y-%m-%d")
    end_date = today.strftime("%Y-%m-%d")
    st_code(f"today: {today}, week_ago: {week_ago}, start_date: {start_date}")
### EndofCodeSection###

def py_ts_local():
    # In Python, datetime.fromtimestamp() converts a Unix timestamp (seconds since Jan 1, 1970) into a local datetime object.
    from datetime import datetime, timezone
    ts = 1700000000
    def ts_local():
        # Local time
        dt_local = datetime.fromtimestamp(ts)
        st_code(f"datetime.fromtimestamp(ts): {dt_local}")
    ts_local()
    st_markline()

    def ts_utc():
        dt_utc = datetime.fromtimestamp(ts, tz=timezone.utc)
        st_code(f"datetime.fromtimestamp(ts,tz=timezone.utc): {dt_utc}")
    ts_utc()
### EndofCodeSection###

def py_datetimeformat():
    from datetime import datetime

    timestamp = 1700000000

    # Option 1: Returns a date object (YYYY-MM-DD)
    just_date = datetime.fromtimestamp(timestamp).date()

    # Option 2: Returns a formatted string
    formatted_date = datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d")

    st_code(f"just_date: {just_date}, formatted_date: {formatted_date}")  # Output: 2023-11-14
### EndofCodeSection###

def pydate_difference():
    # find files modified in the last 4 days
    # Just replace search_directory = "." with the path to the folder you want to scan (e.g., "C:/Users/YourName/Documents" or "/home/user/documents").
    import os
    import time

    # Set directory to search and days threshold
    search_directory = "."  # Change to your folder path
    days = 4

    # Calculate cutoff time in seconds
    cutoff_time = time.time() - (days * 86400)

    print(f"Files modified in the last {days} days:\n")

    for root, _, files in os.walk(search_directory):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                # Check modification time
                if os.path.getmtime(file_path) >= cutoff_time:
                    print(file_path)
            except OSError:
                # Skip files that can't be accessed
                continue
### EndofCodeSection###

def py_date_compare():
    from datetime import datetime

    # via string comparison (easiest)
    date1 = "2023-10-25"
    date2 = "2023-10-20"

    if date1 > date2:
        st_code(f"via string compare: date1 is later than date2")

    # via datetime (best Practice)
    date1 = datetime.strptime("2023-10-25", "%Y-%m-%d")
    date2 = datetime.strptime("2023-10-20", "%Y-%m-%d")

    # Python 3.7+ shortcut: datetime.fromisoformat('2023-10-25')

    if date1 > date2:
        st_code(f"via datetime: date1 is later than date2")
### EndofCodeSection###




