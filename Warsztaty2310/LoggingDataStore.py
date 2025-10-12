from DataStore import DataStore
def log_operation(func):
    def wrapper(*args, **kwargs):
        if func.__name__=="__setitem__":
            print("Zapisuje do slownika")
            func(*args, **kwargs)
        if func.__name__=="get":
            print("Odczytuje  z slownika")
        print("Logging operation")
    return  wrapper

# args[1:]
# {func.__name__} z agrs={args[1:]}
class LoggingDataStore(DataStore):
    # def __init__(self, logger, name, description):
    #     super().__init__(name, description)
    #     self.logger = logger
    @log_operation
    def __setitem__(self, key, value):
        #print(f"Zapisuje {key} = {value}")
        super().__setitem__(key, value)
    @log_operation
    def __getitem__(self, item):
        #print(f" Odczytuje {item} = {self.data[item]}")
        return super().__getitem__(item)
