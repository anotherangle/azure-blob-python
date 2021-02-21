from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, __version__


#Defining connection string
connect_str = 'your_connection_String'

# Create the BlobServiceClient object which will be used to create a container client
blob_service_client = BlobServiceClient.from_connection_string(connect_str)

#define storage_Account_name
st_name = "your_Storage_account_name"

# Defining a container name
container_name = 'your_container_name'

#creating a client for container
container_client = blob_service_client.get_container_client(container_name)

#let's get the list of blobs
blobs_list = container_client.list_blobs()

#let's loop through the list
for blob in blobs_list:
    print(blob.name + '\n')
