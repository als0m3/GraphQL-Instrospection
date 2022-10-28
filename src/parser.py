from src.utils import *


def extract_query_arguments(args):
    return [[graphql_getType(arg)[0], arg["name"]] for arg in args]


def extract_query_fields(field):
    return [graphql_getType(field)[0], field["name"]]
