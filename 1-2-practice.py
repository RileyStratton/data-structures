class PhoneQueue:

    def __init__(self):
        self.queue = list()

    def request_call(self, number):
        pass

    def process_call(self):
        pass

# Test code

queue = PhoneQueue()
queue.request_call("123-456-7890")
queue.request_call("911")
queue.request_call("123-456-7890")
queue.process_call()
queue.process_call()
queue.process_call()
queue.process_call()

# Should print:
    # Processing call to 911
    # Processing call to 123-456-7890
    # Processing call to 098-765-4321
    # No calls to process