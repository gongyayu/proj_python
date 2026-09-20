from py_mod import line_print,st_print,st_code,codelines

### StartofFunc###

def pysignal():
    from signal import signal, SIGINT

    def pysignal_handler(signal_received, frame):
        # Handle any cleanup here
        print('SIGINT or CTRL-C detected. Exiting gracefully')
        exit(0)
        # called in dunder section via signal(SIGINT, handler)
### EndofCodeSection###