#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket: # this is flight 
    def __init__(self, source, destination):
        self.source = source # start the flight
        self.destination = destination # the next airport 


def reconstruct_trip(tickets, length):

    ''' The
        ticket for your first flight has a destination with a `source` of
        `NONE`, and the ticket for your final flight has a `source` with a
        `destination` of `NONE`. 

        so we need an obj to hold the flight info 
        and list that list the flights where the first flight, its source should be 
        "NONE" --> and last One its destination --> "NONE"
        "NONE" --> string 
    '''
    hash_tick = {}
    route = []

    for ticket in tickets:
        # first flight is None
        # if ticket.source == None:
        if ticket.source == "NONE":
            route.append(ticket.destination)
        hash_tick[ticket.source] = ticket.destination
        
    tick_we_have = hash_tick[route[0]]



    # count the flight and loop over them 
    # until we find the destination is NONE
    count = 1
    while count < length:
        route.append(tick_we_have)
        tick_we_have = hash_tick[tick_we_have]
        count += 1

    return route





'''
tickets = [
    Ticket{ source: "PIT", destination: "ORD" },
    Ticket{ source: "XNA", destination: "CID" },
    Ticket{ source: "SFO", destination: "BHM" },
    Ticket{ source: "FLG", destination: "XNA" },
    Ticket{ source: "NONE", destination: "LAX" }, first fight 
    Ticket{ source: "LAX", destination: "SFO" },
    Ticket{ source: "CID", destination: "SLC" },
    Ticket{ source: "ORD", destination: "NONE" }, last one 
    Ticket{ source: "SLC", destination: "PIT" },
    Ticket{ source: "BHM", destination: "FLG" }
]
'''

ticket_1 = Ticket("NONE", "PDX")
ticket_2 = Ticket("PDX", "DCA")
ticket_3 = Ticket("DCA", "NONE")

tickets = [ticket_1, ticket_2, ticket_3]
print(reconstruct_trip(tickets, len(tickets)))
