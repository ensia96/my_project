import time
def repeater(reps):
    def func_deco(func):
        def wrapper(*args, **kwargs):
            total = 0
            for i in range(reps):
                total += func(*args, **kwargs)
            return total / reps
        return wrapper
    return func_deco
def track_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        func_time = end_time - start_time
        return func_time
    return wrapper