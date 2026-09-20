from datetime import datetime, timedelta
from py_mod import st_code

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


