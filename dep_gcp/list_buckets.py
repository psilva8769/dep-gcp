from google.cloud import storage

def list_buckets() -> None:
    client = storage.Client()

    buckets = client.list_buckets()

    for bucket in buckets:
        print(bucket.name)

list_buckets()