class MassTransitSetting:
    def __init__(self, host: str, virtual_host: str, user_name: str, password: str, 
                 is_ssl_active: bool, ssl_thumbprint: str):
        self.host = host
        self.virtual_host = virtual_host
        self.user_name = user_name
        self.password = password
        self.is_ssl_active = is_ssl_active
        self.ssl_thumbprint = ssl_thumbprint

    def deconstruct(self):
        return self.host, self.virtual_host, self.user_name, self.password, self.is_ssl_active, self.ssl_thumbprint
