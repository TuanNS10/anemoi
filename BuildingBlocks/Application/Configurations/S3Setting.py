class S3Setting:
    def __init__(self, service_url: str, access_key: str, secret_key: str, bucket_name: str):
        self.service_url = service_url
        self.access_key = access_key
        self.secret_key = secret_key
        self.bucket_name = bucket_name
