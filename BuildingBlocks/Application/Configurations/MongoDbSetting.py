from BuildingBlocks.Application.Configurations.DbSetting import DbSetting


class MongoDbSetting(DbSetting):
    def __init__(self, connection_string: str, pool_size: int, mongo_database: str):
        super().__init__(connection_string, pool_size)
        self.mongo_database = mongo_database
        