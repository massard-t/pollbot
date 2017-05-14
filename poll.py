import requests
import argparse

# this list needs to be updated everytime :(
proxies = [
	"104.198.212.210",
	"35.187.25.201",
	"130.211.55.208",
	"130.211.117.26",
	"104.199.113.158",
	"35.187.31.4",
	"35.185.208.24",
	"35.185.117.175",
	"35.185.209.35",
	"35.185.59.98"
]

headers = {'x-requested-with': "XMLHttpRequest"}

def check_args():
	parser = argparse.ArgumentParser()
	parser.add_argument("poll_id")
	parser.add_argument("checkbox_id")
	parser.add_argument("number_of_vote")
	args = parser.parse_args()
	return args.poll_id, args.checkbox_id, int(args.number_of_vote)


def main():
	poll_id, checkbox_id, i = check_args()
	url = "https://strawpoll.de/vote"
	querystring = {"pid":poll_id,"oids":"check" + checkbox_id}

	for x in range(0, i):
		proxy = "https://" + proxies[x] + ":80"
		print("sending request to " + url + "/" + poll_id + " from " + proxy)
		response = requests.request("POST", url, headers=headers, params=querystring, proxies={"https": proxies[x]})
		print(response.json())

if __name__ == "__main__":
    main()