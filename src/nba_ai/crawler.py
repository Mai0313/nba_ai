from nba_api.stats.endpoints import playercareerstats
from nba_api.stats.static import players
from pydantic import BaseModel

class NBACrawler:
    """Fetches data from NBA.com using nba_api."""

    def get_player_id(self, full_name: str) -> int | None:
        """Finds a player's ID by name."""
        nba_players = players.find_players_by_full_name(full_name)
        if not nba_players:
            return None
        return nba_players[0]['id']

    def get_player_stats(self, player_id: int) -> dict:
        """Fetches career stats for a player."""
        career = playercareerstats.PlayerCareerStats(player_id=player_id)
        return career.get_dict()
