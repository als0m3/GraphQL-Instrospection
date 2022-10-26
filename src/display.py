from termcolor import colored

from src.utils import *

MAX_DEPTH = 3

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
        print("\t-", colored(arg_name, "cyan"), ":", colored(arg_type, "yellow"))
        clean_type = arg_type.replace("!", "").replace("[", "").replace("]", "")

        if clean_type  in type_list:
            #   if type_list[arg]["description"]:
            #     print_text_with_width(type_list[arg]["description"], 80)

            if type_list[clean_type]["fields"] != None:
                for arg in type_list[clean_type]["fields"]:
                    print("\t-", colored(arg["name"], "cyan"))
                #   if arg["description"]:
                #     print_text_with_width(arg["description"], 80)


def display_sub_fields(sub_fields, type_list, depth):
    for field in sub_fields:
        if graphql_getType(field) in depth:
          print("\t"*len(depth) + "...", colored(graphql_getType(field), "yellow"))
        else:
          depth.append(graphql_getType(field))
          print("\t"*len(depth)  + "+", colored(field["name"], "cyan"),
              ":" ,
              colored(graphql_getType(field), "yellow")
          )
          # if field["description"]:
          #     print_text_with_width(field["description"], 80)
          clean_type = graphql_getType(field).replace("!", "").replace("[", "").replace("]", "")
          if clean_type in type_list and type_list[clean_type]["kind"] != "SCALAR" and len(depth) < MAX_DEPTH:
              display_sub_fields(type_list[clean_type]["fields"], type_list, depth)



def display_query_types(type, type_list):
    clean_type = type[0].replace("!", "").replace("[", "").replace("]", "")
    if clean_type in type_list:
        print("\n", colored("FIELDS", "white"))
        print("\t+" , colored(type[1], "cyan"), ":" , colored(type[0], "yellow"))
        # if type_list[type]["description"]:
        #     print_text_with_width(type_list[type]["description"], 80)


        if type_list[clean_type]["fields"] != None:
          depth = []
          display_sub_fields(type_list[clean_type]["fields"], type_list, depth)
            # for arg in type_list[clean_type]["fields"]:
                # print("\t\t+", colored(arg["name"], "cyan"),
                #     ":" ,
                #      colored(graphql_getType(arg), "yellow")
                # )
                # if arg["description"]:
                #     print_text_with_width(arg["description"], 80)
