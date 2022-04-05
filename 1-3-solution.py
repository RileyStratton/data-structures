class PhoneQueue:

    def __init__(self):
        self.queue = list()

    def request_call(self, number):
        if number == "911":
            self.queue.insert(0, number)
        else:
            self.queue.append(number)

    def process_call(self):
        if len(self.queue) > 0:
            print(f"Processing call to {self.queue[0]}")
            self.queue.pop(0)
        else:
            print("No calls to process")

queue = PhoneQueue()
queue.request_call("123-456-7890")
queue.request_call("911")
queue.request_call("098-765-4321")
queue.process_call()
queue.process_call()
queue.process_call()
queue.process_call()