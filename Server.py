import json


class Server:
    MinecraftServers = []

    def __init__(self, ip, port, **kwargs):
        self.ip = ip
        self.port = port
        self.username = kwargs.get("username")
        self.password = kwargs.get("password")


    def add_game_server(self, server):
        self.MinecraftServers.append(server)

    def remove_game_server(self, server):
        self.MinecraftServers.remove(server)


class MinecraftServer:

    def __init__(self, **kwargs):
        self.server_folder = kwargs.get("server_folder")
        self.folders_to_sync = kwargs.get("folders_to_sync")
        self.server_core = kwargs.get("server_core")
        self.server_memory = kwargs.get("server_memory")
        self.server_process = None
        self.server_status = "stopped"
        self.start_command = kwargs.get("start_command")

    def save_config(self):
        open(self.server_folder + "server_config.json", "w").write(json.dumps(self.__dict__))




