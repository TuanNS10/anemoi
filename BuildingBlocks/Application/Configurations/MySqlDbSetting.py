from BuildingBlocks.Application.Configurations.DbSetting import DbSetting


class MySqlDbSetting(DbSetting):
    def __init__(self, connection_string: str, pool_size: int, major_version: int, minor_version: int,  build_version:int):
        super().__init__(connection_string, pool_size)
        self.major_version = major_version
        self.minor_version = minor_version
        self.build_version = build_version

    def deconstruct(self):
        return self.major_version, self.minor_version, self.build_version, self.connection_string