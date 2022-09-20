import requests, zipfile, os

download_uris = [
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2018_Q4.zip',
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q1.zip',
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q2.zip',
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q3.zip',
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q4.zip',
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2020_Q1.zip',
    'https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2220_Q1.zip'
]


def main():
    # 1. create the directory downloads if it does not already exist
    dir = 'downloads'
    if not os.path.exists(dir):
        os.mkdir(dir)
    
    os.chdir(dir)
    # 2. Download the Files one by one
    # 3. Split the filename from the uri so the file keeps its original name
    # 4. Each file is a zip, extract the csv from the zip and delete the zip
    for file in download_uris:
        filename = file.split('/')[-1]
        try:
            response = requests.get(file)
            with open(filename, 'wb') as output_file:
                output_file.write(response.content)
            with zipfile.ZipFile(filename, 'r') as zip:
                zip.extractall()
            os.remove(filename)
        except:
            print(f"Error ocurred with {file}")
            if os.path.exists(filename):
                os.remove(filename)

    # 5. EXTRA - download the files in an async manner using package `aiohttp`. Try using `ThreadPoolExecutor` to downloda the files. Write unit tests to improve your skills 

    return


if __name__ == '__main__':
    main()
