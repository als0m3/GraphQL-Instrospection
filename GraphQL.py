from termcolor import colored
import argparse

# Utils

from src.display import *
from src.parser import *
from src.request import graphql_get_all_types


def display_script_header():
    print(colored("Starting the Graphql analyse...", "green"))
    print(colored("Getting the Queries...", "green"))


def display_query(query, type_list):
    print("----------------------------------------")
    args = extract_query_arguments(query["args"])
    type = extract_query_fields(query)

    print(colored(query["name"], "green"), ":", colored(type[0], "yellow"))

    display_query_arguments(args, type_list)
    display_query_types(type, type_list)

    print("")


def main(args):
    display_script_header()

    types = graphql_get_all_types(args.url, args.token)
    type_list = {t["name"]: t for t in types if t["name"] != "Query"}

    print(colored("GraphQL Queries for", "white"), colored(args.url, "yellow"))

    [
        display_query(q, type_list)
        for t in types
        if t["name"] == "Query"
        for q in t["fields"]
    ]


def parse_args():
    """Parse the arguments."""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-u",
        "--url",
        help="GraphQL URL",
        required=True,
    )
    parser.add_argument(
        "-t", "--token", help="GraphQL token", required=False, default=""
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    main(args)
