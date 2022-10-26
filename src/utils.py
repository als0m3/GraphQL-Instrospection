
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
    return arg_name