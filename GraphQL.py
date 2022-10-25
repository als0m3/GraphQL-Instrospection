import requests
import json

# Utils


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
    print(fields)
    """Display the available fields."""
    for type_name, type_ in fields.items():
        print(type_name)
        print(type_["type_description"])
        if type_["type_fields"]:
            for field in type_["type_fields"]:
                print("  -", field["name"])


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


if __name__ == "__main__":
    url = "http://challenge01.root-me.org/web-serveur/ch66/api/graphql"
    token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MywiaWF0IjoxNjY2NTQ1MzU4LCJleHAiOjE2NjY1NTYxNTh9.GvfQqr8s-309SBTjSleR0OFGtvis0PhDf3KYF89m91E"
    # types = graphql_get_types(url, token)
    # types = graphql_get_type_fields(url, token, "User")

    fields = graphql_get_available_fields(url, token)

    # print("Available fields:", fields)
    # print(fields)
    # display_fields(fields)

    write_json_file("fields.json", fields)
