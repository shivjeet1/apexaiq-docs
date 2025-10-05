import datetime
import functools

class ActivityLogger:
    """A singleton-like class to handle all logging operations to a file."""
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(ActivityLogger, cls).__new__(cls)
        return cls._instance

    def __init__(self, filename="default_log.txt"):
        if not hasattr(self, '_file_handle'):
            self._filename = filename
            self._file_handle = open(self._filename, 'a', encoding='utf-8')
            self.log(f"--- Log Session Started: {datetime.datetime.now():%Y-%m-%d %H:%M:%S} ---")

    def log(self, message):
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log_entry = f"[{timestamp}] {message}"
        print(log_entry)
        self._file_handle.write(log_entry + '\n')
        self._file_handle.flush()

    def close(self):
        self.log(f"--- Log Session Ended: {datetime.datetime.now():%Y-%m-%d %H:%M:%S} ---")
        self._file_handle.close()

def log_activity(func):
    """Decorator to log the execution of a method."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        logger = ActivityLogger()
        func_name = func.__name__
        try:
            logger.log(f"Executing '{func_name}'...")
            result = func(*args, **kwargs)
            logger.log(f"Finished '{func_name}' successfully.")
            return result
        except Exception as e:
            logger.log(f"ERROR during '{func_name}': {e}")
            raise e
    return wrapper
