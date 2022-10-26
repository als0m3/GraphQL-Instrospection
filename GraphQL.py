import requests
import json
from termcolor import colored

# Utils

from src.display import *
from src.parser import *


def print_text_with_width(text, width):
    """Print text with a given width."""
    for i in range(0, len(text), width):
        print("/".join([a.strip() for a in text[i : i + width].split("/")]))

    # print(text.ljust(width), end="")


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


def write_json_file(filename, data):
    """Write data to a JSON file."""
    with open(filename, "w") as f:
        json.dump(data, f, indent=2)


# ------------------------------------------------------------------------------


def display_fields(fields):
    # print(fields)
    """Display the available fields."""
    for type_name, type_ in fields.items():
        print(type_name)
        if type_["type_fields"]:
            for field in type_["type_fields"]:
                print("\t-", field["name"])
        if type_["type_description"]:
            print("(", type_["type_description"] + ")")


def graphql_get_types(url, token):
    """Get the types from the GraphQL schema."""
    query = """
    {
      __schema {
        types {
          name
          description
        }
      }
    }
    """
    response = graphql_request(url, query, token)
    return response["data"]["__schema"]["types"]


def graphql_get_request_types(url, token):
    """Get the request types from the GraphQL schema."""
    query = open("request.graphql", "r").read()
    # print(query)
    response = graphql_request(url, query, token)
    # print(response)
    return response["data"]


def graphql_get_type_fields(url, token, type_name):
    """Get the fields for a given type."""
    query = (
        """
    {
      __type(name: "%s") {
        name
        description
        fields {
          name
          type {
            name
            kind
            ofType {
              name
              kind
            }
          }
        }
      }
    }
    """
        % type_name
    )
    response = graphql_request(url, query, token)
    return response["data"]["__type"]["fields"]


def graphql_get_available_fields(url, token):
    """Get the available fields for all types."""
    types = graphql_get_types(url, token)
    fields = {}
    for type_ in types:
        type_name = type_["name"]
        fields[type_name] = dict(
            {
                "type_fields": graphql_get_type_fields(url, token, type_name),
                "type_description": type_["description"],
            }
        )
    return fields


def display_request_types(request_types):
    write_json_file("request_types.graphql", request_types)
    """Display the available request types."""

    type_list = dict()
    for type in request_types["__schema"]["types"]:
        if type["name"] != "Query":
            type_list[type["name"]] = type
            # print(colored(type["name"], "green"))

    for query in request_types["__schema"]["types"]:
        if query["name"] == "Query":

            for field in query["fields"]:
                # # if field["description"]:
                # #     print_text_with_width(field["description"], 80)
                # for arg in field["args"]:
                #     # print("\t", colored(arg["name"], "red"))
                #     if arg["description"]:
                #         print_text_with_width(arg["description"], 80)
                #     # print("\t\t", colored(arg["type"]["name"], "blue"))

                print("----------------------------------------")
                args = extract_query_arguments(field["args"])
                type = extract_query_types(field)

                print(
                    colored(field["name"], "green"),
                    ":"
                    , colored(
                        type[0],
                        "yellow",
                    )
                   
                )

                display_query_arguments(args, type_list)
                display_query_types(type, type_list)

                print("")


if __name__ == "__main__":
    url = "https://countries.trevorblades.com/"
    token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MywiaWF0IjoxNjY2NjkyNjgyLCJleHAiOjE2NjY3MDM0ODJ9.Fkz5rpGQNUsP9mLQSP9RU3yAr6GByA3ehfY5K9q5W5E"

    print(colored("Starting the Graphql analyse...", "green"))

    print(colored("Getting the Queries...", "green"))
    display_request_types(graphql_get_request_types(url, token))
