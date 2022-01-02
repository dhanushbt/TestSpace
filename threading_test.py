import threading 

def lock(node_id, user_id):
    #insert lock logic here
    pass

def unlock(node_id, user_id):
    #insert unlock logic here
    pass

def upgrade(node_id, user_id):
    #insert upgrade logic here
    pass

class Node:
    def __init__(self, data):
        self.Data = data
        self.ThreadLock = True

#get the data out of the query
def parse_query(query):
    operation, node_id, user_id = map(str, query.split())
    node_id = int(node_id)
    return operation, node_id, user_id

def execute_queries(thread_id, queries):
    for query in queries:
        op, node_id, user_id = parse_query(query)
        if op == "lock":
            lock(node_id, user_id)
        elif op == "unlock":
            unlock(node_id, user_id)
        elif op == "upgrade":
            upgrade(node_id, user_id)
        else:
            print("Invalid Operation -> ", op)
            return
        print(f"Thread {thread_id} : {op}ed {node_id} by {user_id} \n")


queries = [
    "lock 1 john",
    "lock 1 sherlock",
    "unlock 2 john",
    "lock 3 mary"
]
#splitting up the queries for the two threads below
queries_first_half = queries[0:2]
queries_second_half = queries[2:4]

## Represting tree as an array of nodes so easier to explain.
nArrayTree = [ Node(10), Node(20), Node(23), Node(12), Node(2) ]

thread1 = threading.Thread(target=execute_queries, args=(1, queries_first_half))
thread2 = threading.Thread(target=execute_queries, args=(2, queries_second_half))

thread1.start()
thread2.start()


