
def parse_sys_args(args):
    output = {}

    for arg in args:
        spliter_pos = arg.find('=')
        if (spliter_pos !=  -1):
            key = arg[:spliter_pos]
            value = arg[spliter_pos + 1:]
            output[key] = value

    return output
