"""
This file stores server, such as 'cn', 'en'.
Use 'import module.config.server as server' to import, don't use 'from xxx import xxx'.
"""
server = 'cn'  # Setting default to cn, will avoid errors when using dev_tools


def set_server(target):
    global server
    server = target

    from module.base.resource import release_resources
    release_resources()
