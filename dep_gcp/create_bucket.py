from google.cloud import storage

def create_bucket(bucket_name: str) -> None:
    client = storage.Client()

    client.create_bucket(bucket_or_name=bucket_name)

create_bucket('video-games-bucket-dep-gcp')