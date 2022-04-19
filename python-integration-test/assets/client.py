#!/usr/bin/env python3

import urllib.request


def main():
    # Opens the localhost address on port 8080 and decodes the data
    client = urllib.request.urlopen("http://localhost:8080/")
    resp_text = client.read().decode("utf8")

    print(resp_text)

    client.close()


if __name__ == "__main__":
    main()
