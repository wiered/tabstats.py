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

import copy
import requests
from ._user import User

__VERSION__ = '0.1.1'

SEARCH_API = "https://r6.apitab.net/website/search"
PROFILE_API = "https://r6.apitab.net/website/profiles/{}"
DEFAULT_SEARCH_JSON = {
            "name": "N/A",
            "id": "N/A",
            "level": "N/A",
            "rank": "N/A",
            }

class Client():
    def __init__(self):
        self.session = requests.Session()
        
    
    def get_player(self, player_id: str) -> User:
        """_summary_ : Parse overall player data from player id

        Args:
            playerid (str): Rainbow Six Siege player id

        Returns:
            User: overall player data
        """

        response = self.session.get(PROFILE_API.format(player_id))

        if response.status_code != 200:
            return {}

        return User(response.json())
    

    def search(self, query):
        """_summary_ : Parse search results from query
        
        Args:
            query (str): Rainbow Six Siege user name
        
        Returns:
            list: list of search results
        """

        response = self.session.get(SEARCH_API, params={"display_name": query, "platform": "uplay"})
        if response.status_code != 200:
            return []
        return [self._unpack_json(_json) for _json in response.json()]


    def _extract_rank(self, response, _json) -> dict:
        """_summary_ : extracts rank from json"""
        rank = None
        cssr = response.get("current_season_ranked_record")
        if cssr:
            rank = cssr.get("rank_slug")[3:]
            
        if rank:
            _json.update({"rank": rank})
            
        return _json


    def _extract_profile(self, _json: dict, response: dict) -> dict:
        """_summary_ : extracts profile from json"""
        profile = response.get("profile")
        if profile:
            _json.update({"name": profile.get("display_name")})
            _json.update({"id": profile.get("user_id")})
            _json.update({"level": profile.get("level")})
        
        return _json


    def _unpack_json(self, response, full=False) -> dict:
        """Unpack json from api to dict

        Args:
            response (_type_): raw json from api
            full (bool, optional): if true, unpacking from full json. Defaults to False.

        Returns:
            dict: unpacked json with player data
        """

        if not response:
            return {}

        _json = copy.copy(DEFAULT_SEARCH_JSON)
        _json = self._extract_profile(_json, response)
        _json = self._extract_rank(response, _json)

        return _json


    def __enter__(self):
        return self
     

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.session.close()
