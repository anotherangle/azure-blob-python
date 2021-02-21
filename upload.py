from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, __version__


#Defining connection string
connect_str = 'your_Connection_String' 

# Create the BlobServiceClient object which will be used to create a container client
blob_service_client = BlobServiceClient.from_connection_string(connect_str)

#define storage_Account_name
st_name = "your_Storage_Account_name"

# Defining a container name
container_name = 'your_container_name'

#Defining a file which we wish to copy to azure blob storage
file_path = 'somefile2.txt'


# Create a blob client using the local file name as the name for the blob
blob_client = blob_service_client.get_blob_client(container=container_name, blob=file_path)

print("\nUploading to Azure Storage as blob:\n\t" + file_path)

with open(file_path,"rb") as data:
    blob_client.upload_blob(data)

blob_url = "https://"+st_name+".blob.core.windows.net/"+container_name+"/"+file_path+""

print(blob_url)
