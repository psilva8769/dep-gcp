from google.cloud import storage

def delete_bucket(bucket_name: str) -> None:
    client = storage.Client()

    bucket = client.bucket(bucket_name)
    bucket.delete()

delete_bucket()