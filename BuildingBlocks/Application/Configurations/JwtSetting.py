from datetime import timedelta

class JwtSetting:
    def __init__(self, private_key_path: str, public_key_path: str, token_lifetime: timedelta, refresh_token_lifetime: timedelta):
        self.private_key_path = private_key_path
        self.public_key_path = public_key_path
        self.token_lifetime = token_lifetime
        self.refresh_token_lifetime = refresh_token_lifetime
