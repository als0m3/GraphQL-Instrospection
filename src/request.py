import requests


def graphql_request(url, query, token, variables=None):
    response = requests.post(
        url,
        json={"query": query, "variables": variables},
        headers={
            "Content-Type": "application/json",
            "Authorization": "Bearer " + token,
        },
    )
    return response.json()


def graphql_get_all_types(url, token):
    query = open("request.graphql", "r").read()
    response = graphql_request(url, query, token)
    try:
        return response["data"]["__schema"]["types"]
    except:
        print("Network error")
