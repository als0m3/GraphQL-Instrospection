from termcolor import colored

from src.utils import *

MAX_DEPTH = 10


def print_text_with_width(text, width):
    """Print text with a given width."""
    for i in range(0, len(text), width):
        print("/".join([a.strip() for a in text[i : i + width].split("/")]))


def display_query_arguments(args, type_list):
    if len(args) > 0:
        print("\n", colored("ARGUMENTS", "white"))
    else:
        print("\n", colored("NO ARGUMENTS", "white"))
    for arg_type, arg_name in args:
        print("\t+", colored(arg_name, "cyan"), ":", colored(arg_type, "yellow"))
        clean_type = arg_type.replace("!", "").replace("[", "").replace("]", "")
        if clean_type in type_list:
            if type_list[clean_type]["inputFields"] != None:
                display_sub_fields(
                    type_list[clean_type]["inputFields"], type_list, 2, []
                )


def display_query_types(type, type_list):
    clean_type = type[0].replace("!", "").replace("[", "").replace("]", "")
    if clean_type in type_list:
        print("\n", colored("FIELDS", "white"))
        if type_list[clean_type]["fields"] != None:
            display_sub_fields(type_list[clean_type]["fields"], type_list, 1, [])
