# The Leaderboard class
class Leaderboard:
    def __init__(self, path: str = None):
        self.leaderboard = {}
        self.path = path

    def add_player(self, player: str, score: int):
        self.leaderboard[player] = score
        if self.path:
            with open(self.path, "a") as file:
                file.write(f"{player}:{score}\n")

    def get_leaderboard(self):
        return self.leaderboard

    def get_player_score(self, player):
        return self.leaderboard[player]

    def get_player_rank(self, player):
        return sorted(self.leaderboard.values(), reverse=True).index(self.leaderboard[player]) + 1

    def get_leaderboard_rank(self):
        return sorted(self.leaderboard.items(), key=lambda x: x[1], reverse=True)

    def import_player_from_txt(self):
        if self.path:
            with open(self.path, "r") as file:
                for line in file:
                    player, score = line.split(":")
                    self.add_player(player, int(score))
        else:
            raise ValueError("No path specified")

    def remove_player(self, player):
        self.leaderboard.pop(player)
        if self.path:
            with open(self.path, "w") as file:
                for player in self.leaderboard:
                    file.write(f"{player}:{self.leaderboard[player]}\n")
