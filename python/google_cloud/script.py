from google.cloud import storage
from google.oauth2 import service_account

BUCKET_NAME = "example-bucket-vitaly-test"

def listFiles(bucket, storage_client):
    bucket = storage_client.get_bucket(bucket)
    return [blob.name for blob in bucket.list_blobs()]

def readFile(bucket, storage_client, file_name):
    bucket = storage_client.get_bucket(bucket)
    blob = bucket.blob(file_name)
    return blob.download_as_string().decode("utf-8")

credentials = service_account.Credentials.from_service_account_file("key.json")
storage_client = storage.Client(credentials=credentials)

for filename in listFiles(BUCKET_NAME, storage_client):
    print(readFile(BUCKET_NAME, storage_client, filename))
