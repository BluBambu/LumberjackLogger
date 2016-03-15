logs = {}
log_arg_map = {}

class Log:
    def __init__(self, log_name):
        self.log_name = log_name
        self.entries = []
        self.callback_func = None

    def append(self, obj):
        if self.callback_func is not None:
            self.callback_func((obj, str(obj)))
        self.entries.append((obj, str(obj)))
        return self

    def to_string(self):
        str = ''
        for entry in self.entries:
            str += entry[1] + '\n'
        return str

    def print_log(self):
        print self.to_string()
        return self

    def filter(self, func):
        self.entries = [entry for entry in self.entries if func(entry)]
        return self

    def sort(self, func):
        self.entries.sort(func)
        return self

    def map(self, func):
        self.entries = [func(entry) for entry in self.entries]
        return self

    def callback(self, func):
        self.callback_func = func
        return self

def log(log_name, obj):
    if log_name not in logs:
        logs[log_name] = Log(log_name)
    logs[log_name].append(obj)
    return obj

def log_arg(log_name, obj, arg_counter):
    if log_name not in logs:
        logs[log_name] = Log(log_name)
    if log_name not in log_arg_map:
        log_arg_map[log_name] = {}
    if arg_counter not in log_arg_map[log_name]:
        log_arg_map[log_name][arg_counter] = len(logs[log_name].entries)
        logs[log_name].append((obj))
    else:
        logs[log_name].entries[log_arg_map[log_name][arg_counter]] = \
            (logs[log_name].entries[log_arg_map[log_name][arg_counter]][0],
             logs[log_name].entries[log_arg_map[log_name][arg_counter]][1] + (obj))
    return obj

def get_log(log_name):
    if log_name not in logs:
        logs[log_name] = Log(log_name)
    return logs[log_name]
