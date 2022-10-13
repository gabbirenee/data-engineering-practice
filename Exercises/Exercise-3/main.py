import boto3
import botocore


def main():
    bucket = "commoncrawl"
    key = "crawl-data/CC-MAIN-2022-05/wet.paths.gz"
    filename = key[key.rfind("/")+1:]
    print(filename)
    
    # 1. Use boto3 to download the file from the s3 bucket
    s3 = boto3.resource('s3', config=botocore.client.Config(signature_version=botocore.UNSIGNED))
    # s3.download_file(Bucket = bucket, Key = key, Filename = filename)
    s3.Bucket(bucket).download_file(Key = key, Filename = filename)


    # 2. Extract an open this file with Python

    # 4. Pull the uri from the first line of the file

    # 5. Download the uri of the new file using boto 3 again

    # 6. Print each line

    # Extra: Do not load the entire file into memory before printing each line, stream the file
    #### Do not download the initial gz file onto disk: download, extract, and read it in memory


if __name__ == '__main__':
    main()
