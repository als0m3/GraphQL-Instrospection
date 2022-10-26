from termcolor import colored


def print_text_with_width(text, width):
    """Print text with a given width."""
    for i in range(0, len(text), width):
      print("/".join([a.strip() for a in text[i : i + width].split("/")]))
      

def display_query_arguments(args, type_list):
  for arg_type, arg_name in args:
    # print("\t-", colored(arg_name, "cyan"), colored(arg_type, "yellow"))

    print("\n", colored("ARGUMENTS", "white"))

    if arg_type in type_list:
      print("\t-", colored(type_list[arg_type]["name"], "white"), ":",  colored(arg_name, "cyan"))

    #   if type_list[arg]["description"]:
    #     print_text_with_width(type_list[arg]["description"], 80)

      if type_list[arg_type]["fields"] != None:
        for arg in type_list[arg_type]["fields"]:
          print("\t-", colored(arg["name"], "cyan"))
        #   if arg["description"]:
        #     print_text_with_width(arg["description"], 80)

def display_query_types(type, type_list):
    if type[0] in type_list:
        print("\n", colored("FIELDS", "white"))
        print("\t-", colored(type[0], "white"), ":", colored(type[1], "cyan"))
        # if type_list[type]["description"]:
        #     print_text_with_width(type_list[type]["description"], 80)

        if type_list[type[0]]["fields"] != None:
            
            for arg in type_list[type[0]]["fields"]:
                print("\t\t-", colored(arg["name"], "cyan"))
                # if arg["description"]:
                #     print_text_with_width(arg["description"], 80)
    