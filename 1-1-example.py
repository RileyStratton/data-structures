class CustomerService:

    class Ticket:

        def __init__(self, name, problem):

            self.name = name
            self.problem = problem

        def __str__(self):

            return self.name + ": " + self.problem

    def __init__(self):

        self.queue = list()

    def create_ticket(self, name, problem):

        ticket = CustomerService.Ticket(name, problem)
        self.queue.append(ticket)

    def process_ticet(self):

        if len(self.queue) > 0:
            print(self.queue.pop(0))
        else:
            print ("There are no tickets to process")

    def __str__(self):

        result = "["
        for ticket in self.queue:
            result += "{"+str(ticket)+"}"
            result += ", "
        result += "]"
        return result



# Test code

customer_service = CustomerService()
customer_service.create_ticket("John", "iPhone not working")
customer_service.create_ticket("Mary", "Broken monitor")
customer_service.create_ticket("Peter", "No internet")
print(customer_service)
customer_service.process_ticet()
customer_service.process_ticet()
customer_service.process_ticet()
customer_service.process_ticet()
print(customer_service)