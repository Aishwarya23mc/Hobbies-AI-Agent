import requests

MCP_URL = "http://127.0.0.1:9000"


def get_linkedin(name):

    r = requests.get(f"{MCP_URL}/linkedin/{name}")
    return r.json()["data"]


def get_instagram(name):

    r = requests.get(f"{MCP_URL}/instagram/{name}")
    return r.json()["data"]


def get_resume(name):

    r = requests.get(f"{MCP_URL}/resume/{name}")
    return r.json()["data"]