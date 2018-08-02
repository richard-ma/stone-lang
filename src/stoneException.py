class StoneException(Exception):
    def __init__(self, errmsg):
        super(StoneException, self).__init__()
        self.errmsg = errmsg

    def __str__(self):
        return self.errmsg

# Testing and Usage
if __name__ == '__main__':
    try:
        raise StoneException("This is a StoneException")
    except StoneException as e:
        print(e)
        raise
