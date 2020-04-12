import subprocess

import mcstatus


class MinecraftServer:

    def __init__(self, ip):
        self.ip = ip

    def player_list(self, input):
        index = input.find("[")

        if index == -1:
            return []

        lst_string = input[index+1:-4]
        lst = lst_string.split(", ")
        lst = [s.split(" ")[0][2:] for s in lst]

        return lst


    def server_lookup(self):
        server = mcstatus.MinecraftServer.lookup(self.ip)
        status = server.status()
        player_count = status.players.online

        command = "mcstatus {} status".format(self.ip)
        output = str(subprocess.check_output(command, shell=True))
        players_online = self.player_list(output)

        return (player_count, players_online)
