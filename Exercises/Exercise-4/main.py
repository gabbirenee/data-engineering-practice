import glob, json, csv

def crawl(path):
    print('path: '+ path)
    # get list of files
    files = glob.glob(path + '*')
    # iterate through items in list
    for file in files:
        # if file, then receursivley call with new path
        if file.find('.') == -1:
            newpath = file + '/'
            crawl(newpath)
        # if json, then convert and write to directory
        elif file[-5:] == '.json':
            json_to_csv(file)
            # print('json file: ' + file)
    # if other than skip
    # if end of list then end function

def flatten_json(y):
    out = {}
 
    def flatten(x, name=''):
        # dictionary
        if type(x) is dict:
            for a in x:
                flatten(x[a], name + a + '_')
 
        # list
        elif type(x) is list:
            i = 0
            for a in x:
                flatten(a, name + str(i) + '_')
                i += 1
        else:
            out[name[:-1]] = x
 
    flatten(y)
    return out

def json_to_csv(file):
    # read json
    with open(file) as f:
        data = json.load(f)

    # normalize json
    data = flatten_json(data)
    header = list(data.keys())
    values = list(data.values())

    # write json to csv
    filename = ((file.split('/')[-1]).split('.')[0]) + '.csv'
    with open(filename, 'w', newline="") as fcsv:
        csvwriter = csv.writer(fcsv)
        csvwriter.writerow(header)
        csvwriter.writerow(values)


def main():
    # 1. Crawl the data directory with Python and identify all the json files
    path = 'data/'
    crawl(path)


if __name__ == '__main__':
    main()
