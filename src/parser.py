
def extract_query_arguments(args):
  result = []
  for arg in args:
    current_arg = arg["type"]["name"]
    idx = arg["type"]
    while current_arg == None:
      if idx["name"] != None:
        current_arg = idx["name"]
      else:
        current_arg = idx["name"]
        idx = idx["ofType"]
    result.append([current_arg, arg["name"]])
  return result

def extract_query_types(field):
    current_type = field["type"]["name"]
    idx = field["type"]
    while current_type == None:
        if idx["name"] != None:
            current_type = idx["name"]
        else:
            current_type = idx["name"]
            idx = idx["ofType"]
    
    return [current_type, field["name"]]