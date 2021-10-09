from azure.storage.fileshare import ShareServiceClient

def main():
    # Create a file share client
    share_client = ShareServiceClient.from_connection_string(
        "DefaultEndpointsProtocol=https;AccountName=<account_name>;AccountKey=<account_key>;EndpointSuffix=core.windows.net")

    # Create a file share
    share_client.create_share("<share_name>")

    # Delete the file share
    share_client.delete_share("<share_name>")