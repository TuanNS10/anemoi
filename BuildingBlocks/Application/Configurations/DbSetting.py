class DbSetting:
    def __init__(self, connection_string: str, pool_size: int):
        self.connection_string = connection_string
        self.pool_size = pool_size
        