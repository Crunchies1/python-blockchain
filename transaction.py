class Transaction(dict):
    '''
    Example transaction:
    {   
        "author": "author_name",
        "timestamp": "transaction_time", 
        "data": "transaction_data"
    }
'''
    def __init__(self, author, timestamp, data):
        dict.__init__(
            self, 
            author=author,
            timestamp = timestamp,
            data = data
            )
        