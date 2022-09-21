import requests
import pandas as pd



def main():
    url = 'https://www.ncei.noaa.gov/data/local-climatological-data/access/2021/'
    # 1. Attempt to web scrape/pull down the contents of the website
    response = requests.get(url)

    # 2. Analyze the structure, determine how to find the corresponding file using Python
    filename = response.text[0:response.text.find('2022-02-07 14:03')]
    filename = filename[filename.rfind('href=\"'):]
    filename = filename[filename.find('\"')+1:]
    filename = filename[:filename.find('\"')]
    # print(filename)

    # 3. Build the URL required to download this file and write the file locally
    file_url = url + filename
    # print(file_url)

    file = requests.get(file_url)
    with open(filename, 'wb') as output_file:
                output_file.write(file.content)

    # 4. Open the file with Pandas to find the records with the highest HourlyDryBulbTemperature
    df = pd.read_csv(filename, usecols=['STATION', 'DATE', 'HourlyDryBulbTemperature'])
    # print(df.head())
    max = df['HourlyDryBulbTemperature'].max()
    df = df[df.HourlyDryBulbTemperature == max]

    # 5. Print these records
    print(df)


if __name__ == '__main__':
    main()
