from src.utils import *


def extract_query_arguments(args):
    result = []
    for arg in args:
        result.append([graphql_getType(arg)[0], arg["name"]])
    return result


def extract_query_types(field):
    return [graphql_getType(field)[0], field["name"]]
