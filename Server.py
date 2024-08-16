import json


class Server:
    MinecraftServers = []

    def __init__(self, ip, port, **kwargs):
        if kwargs.get("config_file") is not None:
            self.__dict__ = json.loads(open(kwargs.get("config_file")).read())
        else:
            self.ip = ip
            self.port = port
            self.username = kwargs.get("username")
            self.password = kwargs.get("password")


    def add_game_server(self, server):
        self.MinecraftServers.append(server)

    def remove_game_server(self, server):
        self.MinecraftServers.remove(server)

class frpServer:

        def __init__(self, **kwargs):
            self.server_ip = kwargs.get("server_ip")
            self.server_port = kwargs.get("server_port")
            self.server_token = kwargs.get("server_token")
            self.server_status = "stopped"

        def save_config(self):
            open("frp_config.json", "w").write(json.dumps(self.__dict__))

        def start(self):
            self.server_status = "running"

        def stop(self):
            self.server_status = "stopped"

        def get_status(self):
            return self.server_status

        def get_config(self):
            return self.__dict__


class MinecraftServer:

    def __init__(self, **kwargs):
        if kwargs.get("config_file") is not None:
            self.__dict__ = json.loads(open(kwargs.get("config_file")).read())
        else:
            self.server_folder = kwargs.get("server_folder")
            self.folders_to_sync = kwargs.get("folders_to_sync")
            self.server_core = kwargs.get("server_core")
            self.server_memory = kwargs.get("server_memory")
            self.server_process = None
            self.server_status = "stopped"
            self.start_command = kwargs.get("start_command")




    def save_config(self):
        open(self.server_folder + "server_config.json", "w").write(json.dumps(self.__dict__))






