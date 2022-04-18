# This is the client that will perform the request
import requests


def main():
    resp = requests.get("http://127.0.0.1:8080",
                        verify=False)
    print(resp)


if __name__ == "__main__": main()

