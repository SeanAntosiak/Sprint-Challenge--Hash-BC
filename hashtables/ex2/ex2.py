#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * (length - 1)  # started code with off by one error ??????

    for ticket in tickets:
        hash_table_insert(hashtable,
                          ticket.source,
                          (ticket.source, ticket.destination)
                          )
    # the first current destination starts from NONE
    current_dest = hash_table_retrieve(hashtable, "NONE")[1]
    route[0] = current_dest
    current_index = 1
    while current_dest != "NONE":
        current_dest = hash_table_retrieve(hashtable, current_dest)[1]
        if (current_dest != "NONE"):
            route[current_index] = current_dest
            current_index += 1
    return(route)
