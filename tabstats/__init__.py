"""
Tabstatspy: Tabstats parser
Copyright (C) 2023 Artem Babka
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

import requests
from ._user import User

__VERSION__ = '0.1.2'

SEARCH_API = "https://r6.apitab.net/website/search"
PROFILE_API = "https://r6.apitab.net/website/profiles/{}"
DEFAULT_USER_CARD = {
            "name": "N/A",
            "id": "N/A",
            "level": "N/A",
            "rank": "N/A",
            }

class Client():
    def __init__(self):
        self.session = requests.Session()
        
    
    def get_player(self, player_id: str) -> User:
        """_summary_ : Parse overall player data by player id

        Args:
            playerid (str): Rainbow Six Siege player id

        Returns:
            User: overall player data
        """

        response: requests.Response = self.session.get(PROFILE_API.format(player_id))

        if response.status_code != 200:
            return User({})

        return User(response.json())
    

    def search(self, query: str) -> list[dict]:
        """_summary_ : Parse search results from query
        
        Args:
            query (str): Rainbow Six Siege user name
        
        Returns:
            list: list of search results, if not found anything will return empty list
        """

        if not isinstance(query, str):
            raise ValueError("query must be a string")

        response = self.session.get(SEARCH_API, params={"display_name": query, "platform": "uplay"})
        if response.status_code != 200:
            return []
        
        search_engine_resultant = self._get_search_engine_resultant(response)
        return search_engine_resultant


    def _extract_rank_from_resultant(self, resultant: dict) -> int:
        """extracts rank from resultant"""

        rank = None
        rank_record = resultant.get("current_season_ranked_record")
        if not rank_record:
            return "Unranked"

        rank = rank_record.get("rank_slug")[3:]
        if not rank:
            return "Unranked"
        
        del rank_record
        return rank
        

    def _extract_user_card_from_resultant(self, resultant: dict) -> dict:
        """extracts user's card from resultant"""

        profile: dict = resultant.get("profile")
        if not profile:
            raise ValueError("Wrong resultant was given")
        
        rank = self._extract_rank_from_resultant(resultant)
        name = profile.get("display_name")
        id = profile.get("user_id")
        level = profile.get("level")
        if not name or not id or not level:
            raise ValueError("Wrong resultant was given")

        user_card: dict = {}
        user_card.update({"name": name})
        user_card.update({"id": id})
        user_card.update({"level": level})
        user_card.update({"rank": rank})

        del name, id, level, rank, profile
        return user_card
    

    def _get_search_engine_resultant(self, response: requests.Response) -> list[dict]:
        """Unpack search engine resultant from response

        Args:
            response (requests.Response)

        Returns:
            list[dict]: list of users cards
        """

        search_engine_resultant = []

        for resultant in response.json():
            user_card = self._extract_user_card_from_resultant(resultant)
            search_engine_resultant.append(user_card)

        return search_engine_resultant


    def __enter__(self):
        return self
     

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.session.close()
        del self.session
