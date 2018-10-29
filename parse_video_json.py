import json
import csv

def parse_data(data, write_to_file=True):
    items = data["items"]
    counter = 0

    with open('parsed_data.csv', mode='a') as parsed_data:
        data_writer = csv.writer(parsed_data, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for item in items:
            counter += 1

            if not item["snippet"]["description"] == "This video is unavailable.":
                short_url = "http://youtu.be/{}".format(item["contentDetails"]["videoId"])
                title = item["snippet"]["title"].encode('utf-8')
                description = item["snippet"]["description"].encode('utf-8')
                id = item["id"]
                if write_to_file:
                    data_writer.writerow([title, description, short_url, id])
            else:
                short_url = "http://youtu.be/{}".format(item["contentDetails"]["videoId"])
                print(short_url)

    print("counter", counter)
    pageToken = data.get("nextPageToken", None)
    if pageToken:
        print("pageToken", pageToken)
    return (pageToken)

        
