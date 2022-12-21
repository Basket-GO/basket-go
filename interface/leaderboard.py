# The Leaderboard class
class Leaderboard:
    def __init__(self, path: str = None):
        """
        The leaderboard class
        @param path: The path of the file
        """
        self.leaderboard = {}
        self.path = path

    def add_player(self, player: str, score: int) -> None:
        """
        Add a player to the leaderboard
        @param player: The player name
        @param score: The player score
        @return: None
        """
        if player in self.leaderboard:
            raise ValueError("Player already exists")
        elif len(player) > 10:
            raise ValueError("Player name too long")
        elif len(player) == 0:
            raise ValueError("Player name cannot be empty")
        else:
            self.leaderboard[player] = score
            if self.path:
                with open(self.path, "a") as file:
                    file.write(f"{player}:{score}\n")

    def add_player_from_txt(self, player: str, score: int) -> None:
        """
        Add a player to the leaderboard without writing in the file
        @param player: The player name
        @param score: The player score
        @return: None
        """
        if player in self.leaderboard:
            raise ValueError("Player already exists")
        elif len(player) > 10:
            raise ValueError("Player name too long")
        elif len(player) == 0:
            raise ValueError("Player name cannot be empty")
        else:
            self.leaderboard[player] = score

    def import_player_from_txt(self) -> None:
        """
        Import all players from the file
        @return: None
        """
        if self.path:
            with open(self.path, "r") as file:
                for line in file:
                    player, score = line.split(":")
                    if len(player) > 10:
                        raise ValueError("Player name too long")
                    elif len(player) == 0:
                        raise ValueError("Player name cannot be empty")
                    else:
                        self.add_player_from_txt(player, int(score))
        else:
            raise ValueError("No path specified")

    def remove_player(self, player: str) -> None:
        """
        Remove a player from the leaderboard
        @param player: The player name
        @return: None
        """
        self.leaderboard.pop(player)
        if self.path:
            # delete the line in the file
            with open(self.path, "r") as file:
                lines = file.readlines()
            with open(self.path, "w") as file:
                for line in lines:
                    if line.split(":")[0] != player:
                        file.write(line)

    def get_leaderboard(self) -> dict:
        """
        Get the leaderboard
        @return: The leaderboard
        """
        return self.leaderboard

    def get_player_score(self, player: str) -> int:
        """
        Get the score of a player
        @param player: The player name
        @return: The player score
        """
        return self.leaderboard[player]

    def get_player_rank(self, player: str) -> int:
        """
        Get the rank of a player
        @param player: The player name
        @return: The player rank
        """
        return sorted(self.leaderboard.values(), reverse=True).index(self.leaderboard[player]) + 1

    def get_leaderboard_rank(self) -> list:
        """
        Get the leaderboard sorted by rank
        @return: The leaderboard sorted by rank
        """

        listSorted = sorted(self.leaderboard.items(),
                            key=lambda x: x[1], reverse=True)
        # return only the 5 first entry
        return listSorted[:5]
