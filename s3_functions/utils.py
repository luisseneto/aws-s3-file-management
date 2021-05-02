import boto3


def upload_file(file_name, bucket):
    """
    Function to upload files to an S3 bucket
    :param file_name:
    :param bucket:
    :return:
    """

    object_name = file_name
    s3_client = boto3.client('s3')
    response = s3_client.upload_file(file_name, bucket, object_name)

    return response


def download_file(file_name, bucket):
    """
    Function to download files from an S3 bucket
    :param file_name:
    :param bucket:
    :return:
    """

    s3 = boto3.resource('s3')
    output = f"downloads/{file_name}"
    s3.bucket(bucket).download_file(file_name, output)

    return output


def list_files(bucket):
    """
    Function to list files in a given bucket
    :param bucket:
    :return:
    """

    s3 = boto3.client('s3')
    contents = []
    try:
        for item in s3.list_objects(Bucket=bucket)['Contents']:
            print(item)
            contents.append(item)
    except Exception as e:
        pass

    return contents
