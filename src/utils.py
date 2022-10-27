from termcolor import colored

MAX_DEPTH = 10


def graphql_getType(arg):
    dimention = []
    arg_name = None
    idx = arg["type"]
    while arg_name == None:
        arg_name = idx["name"]
        dimention.append(idx["kind"])
        if arg_name == None:
            idx = idx["ofType"]

    for i in dimention:
        if i == "NON_NULL":
            arg_name = arg_name + "!"
        elif i == "LIST":
            arg_name = "[" + arg_name + "]"
    return [arg_name, dimention[-1]]


def display_sub_fields(sub_fields, type_list, depth, history):
    for field in sub_fields:
        clean_type = (
            graphql_getType(field)[0].replace("!", "").replace("[", "").replace("]", "")
        )
        if clean_type in history:
            print(
                "\t" * depth + "+",
                colored(field["name"], "cyan"),
                ":",
                colored(graphql_getType(field)[0], "yellow"),
                "...",
            )
        else:
            print(
                "\t" * depth + "+",
                colored(field["name"], "cyan"),
                ":",
                colored(graphql_getType(field)[0], "yellow"),
            )
            clean_type = (
                graphql_getType(field)[0]
                .replace("!", "")
                .replace("[", "")
                .replace("]", "")
            )
            if not graphql_getType(field)[1] == "SCALAR":
                history.append(clean_type)

            if (
                clean_type in type_list
                and type_list[clean_type]["kind"] != "SCALAR"
                and depth < MAX_DEPTH
            ):
                display_sub_fields(
                    type_list[clean_type]["fields"], type_list, depth + 1, history
                )


def display_sub_arguments(sub_fields, type_list, depth, history):
    for field in sub_fields:
        clean_type = (
            graphql_getType(field)[0].replace("!", "").replace("[", "").replace("]", "")
        )
        if clean_type in history:
            print(
                "\t" * depth + "+",
                colored(field["name"], "cyan"),
                ":",
                colored(graphql_getType(field)[0], "yellow"),
                "...",
            )
        else:
            print(
                "\t" * depth + "+",
                colored(field["name"], "cyan"),
                ":",
                colored(graphql_getType(field)[0], "yellow"),
            )
            clean_type = (
                graphql_getType(field)[0]
                .replace("!", "")
                .replace("[", "")
                .replace("]", "")
            )
            if not graphql_getType(field)[1] == "SCALAR":
                history.append(clean_type)

            if (
                clean_type in type_list
                and type_list[clean_type]["kind"] != "SCALAR"
                and depth < MAX_DEPTH
            ):
                display_sub_arguments(
                    type_list[clean_type]["inputFields"], type_list, depth + 1, history
                )
