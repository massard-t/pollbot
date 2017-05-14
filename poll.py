#!/usr/bin/env python3.5
import sys
import argparse
import subprocess
from time import sleep
import requests

URL = "https://strawpoll.de/vote"
HEADERS = {'x-requested-with': "XMLHttpRequest"}

def check_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--poll_id", required=True, type=str)
    parser.add_argument("-c", "--checkbox_id", required=True, type=str)
    parser.add_argument("-n", "--number_of_vote", required=True, type=int)
    parser.add_argument("-d", "--container-name", required=True, type=str)
    parser.add_argument('-s', '--sleep-time', default=10, type=int)
    args = parser.parse_args()
    return (args.poll_id,
        args.checkbox_id,
        args.number_of_vote,
        args.container_name,
        args.sleep_time)


def get_session():
    session = requests.session()
    session.proxies = {
            "http": "socks5://127.0.0.1:9050",
            "https": "socks5://127.0.0.1:9050"
            }
    return session


def renew_ip(container_name):
    p = subprocess.Popen(['docker', 'restart', container_name])
    if p.wait():
        print("Something went wrong while restarting the container.")
        sys.exit(1)
    print("Successfully restart {}".format(container_name))


def main():
    poll_id, checkbox_id, i, container_name, sleep_time = check_args()
    query_parameters = {
            "pid": poll_id, 
            "oids": "check{}".format(checkbox_id)
            }

    session = get_session()
    for proxy in range(0, i):
        try:
            response = session.post(URL,
                    headers=HEADERS,
                    params=query_parameters)
        except Exception as e:
            print("Undetermined error", e, file=sys.stderr)
        print(response.json())
        print("Renewing ip...")
        renew_ip(container_name)
        sleep(sleep_time)

if __name__ == "__main__":
    main()
