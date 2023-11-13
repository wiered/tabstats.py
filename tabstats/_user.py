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

from datetime import datetime, date
from ._type_helpers import parse_str, parse_int, parse_float, parse_bool

API_URL = "https://r6.apitab.net/website/profiles/{}"
AVATAR_URL = "https://ubisoft-avatars.akamaized.net/{}/default_146_146.png"
PROFILE_URL = "https://tabstats.com/siege/player/{}/{}"
CHAMP_API = "https://img-gen.apitab.com/{}"

class User:
    def __init__(self, _json: dict):
        self.is_empty = True

        self.profile: User.Profile = User.Profile(_json.get('profile'))
        self.name = ""
        self.summary_graph_data: User.SummaryGraphData = User.SummaryGraphData(_json.get('summary_graph_data'))
        self.social_profile = {}
        self.game_bans = []
        self.profile_bans = []
        self.aliases: list[User.Alias] = []
        self.general_records: User.GeneralRecords = (
            User.GeneralRecords(_json.get('general_records')))
        self.current_season_records: User.CurrentSeasonRecords = (
            User.CurrentSeasonRecords(_json.get('current_season_records')))
        self.past_season_ranked_records: User.PastSeasonRecords = (
            User.PastSeasonRecords(_json.get('past_season_ranked_records')))
        self.top_region: str = "N/A"
        self.region_breakdown: dict = {}
        self.last_played_at = datetime.fromisoformat("1970-01-01T00:00:00+00:00")

        if not _json:
            return

        self.is_empty = False
        self._unpack(_json)

    def _unpack(self, _json: dict):
        self.profile: User.Profile = User.Profile(_json.get('profile'))
        self.name = self.profile.display_name
        self.summary_graph_data: User.SummaryGraphData = User.SummaryGraphData(_json.get('summary_graph_data'))
        self.social_profile = _json.get('social_profile') if _json.get('social_profile') else {}
        self.game_bans = _json.get('game_bans')
        self.profile_bans = _json.get('profile_bans')
        self.external_bans = _json.get('external_bans')
        
        if _json.get("aliases") is not None:
            self.aliases: list[User.Alias] = [User.Alias(x) for x in _json.get("aliases")]
        
        self.general_records: User.GeneralRecords = (
            User.GeneralRecords(_json.get('general_records'))
            )
        self.current_season_records: User.CurrentSeasonRecords = (
            User.CurrentSeasonRecords(_json.get('current_season_records'))
            )
        self.past_season_ranked_records: User.PastSeasonRecords = (
            User.PastSeasonRecords(_json.get('past_season_ranked_records'))
            )
        self.top_region: str = _json.get('top_region')
        self.region_breakdown = _json.get('region_breakdown')

        if _json.get("last_played_at") is not None:
            self.last_played_at: datetime = datetime.fromisoformat(_json.get('last_played_at'))

    class Profile():
        def __init__(self, _json: dict):
            self.display_name: str  = "N/A"
            self.profile_views: int = 0
            self.user_id: str = "N/A"
            self.player_id: str = "N/A"
            self.level: int = 0
            self.kd: float = 0.0
            self.is_cheater = False
            self.is_vereified = False
            self.display_ban: str = "N/A"
            self.json_url = "N/A"
            self.avatar_url = "N/A"
            self.profile_url = "N/A"
            self.platform_slug: str = "N/A"
            self.updated_at: datetime = datetime.fromisoformat("1970-01-01T00:00:00+00:00")
            self.can_update_at: datetime = datetime.fromisoformat("1970-01-01T00:00:00+00:00")

            if _json:
                self._unpack(_json)

            
        def _unpack(self, _json: dict):    
            self.display_name: str  = parse_str(_json.get("display_name"))
            self.profile_views: int = parse_int(_json.get("profile_views"))
            self.user_id: str = parse_str(_json.get("user_id"))
            self.player_id: str = parse_str(_json.get("profile_id"))
            self.level: int = parse_int(_json.get("level"))
            self.kd: float = parse_float(_json.get("kd"))
            self.is_cheater = parse_bool(_json.get("is_cheater"))
            self.is_vereified = parse_bool(_json.get("is_verified"))
            self.display_ban: str = parse_str(_json.get("display_ban"))
            self.json_url = API_URL.format(self.user_id)
            self.avatar_url = AVATAR_URL.format(self.user_id)
            self.profile_url = PROFILE_URL.format(self.display_name, self.user_id)
            self.platform_slug: str = parse_str(_json.get("platform_slug"))
            self.updated_at: datetime = datetime.fromisoformat(
                _json.get("updated_at"))
            self.can_update_at : datetime = datetime.fromisoformat(
                _json.get("can_update_at"))
    

    class SummaryGraphData():
        def __init__(self, _json: dict):
            if not _json:
                self._set_defaults()
                return

            self.ranked:list[User.SummaryGraphData.GraphData] = User.SummaryGraphData.GraphData.generate(_json.get('ranked'))
            self.casual:list[User.SummaryGraphData.GraphData] = User.SummaryGraphData.GraphData.generate(_json.get('casual'))
            self.deathmatch:list[User.SummaryGraphData.GraphData] = User.SummaryGraphData.GraphData.generate(_json.get('deathmatch'))


        def _set_defaults(self):
            self.ranked = User.SummaryGraphData.GraphData({})
            self.casual = User.SummaryGraphData.GraphData({})
            self.deathmatch = User.SummaryGraphData.GraphData({})


        class GraphData():
            def __init__(self, _json: dict):
                self.kills: int  = 0
                self.deaths: int = 0
                self.wins: int = 0
                self.losses: int = 0
                self.abandons: int = 0
                self.lowest_mmr: int = 0
                self.highest_mmr: int = 0
                self.mode_slug: str = ""
                self.date = 0

                if not _json:  
                    return
                self._unpack(_json)

            def _unpack(self, _json: dict):
                self.kills: int  = parse_int(_json.get("kills"))
                self.deaths: int = parse_int(_json.get("deaths"))
                self.wins: int   = parse_int(_json.get("wins"))
                self.losses: int = parse_int(_json.get("losses"))
                self.abandons: int    = parse_int(_json.get("abandons"))
                self.lowest_mmr: int  = parse_int(_json.get("lowest_mmr"))
                self.highest_mmr: int = parse_int(_json.get("highest_mmr"))
                self.mode_slug: str   = parse_str(_json.get("mode_slug"))
                self.date = date.fromisoformat(_json.get("date"))
            

            @classmethod
            def generate(cls, _json):
                if not _json or len(_json) == 0:
                    return [cls(None)]
                return [cls(json) for json in _json]
    

    class GeneralRecords():
        def __init__(self, _json: dict):
            self.ranked:User.GeneralRecords.Record = User.GeneralRecords.Record(None)
            self.records:dict = {}

            if not _json or not isinstance(_json, dict):
                return
        
            self.ranked  = User.GeneralRecords.Record(_json.get('ranked'))
            self.records = _json
        

        class Record():
            def __init__(self, _json: dict):
                self.mode_slug: str = "N/A"
                self.kills: int     = 0
                self.deaths: int    = 0
                self.kd: float      = 0.0
                self.wins: int      = 0
                self.losses: int    = 0
                self.wl: float      = 0.0
                self.abandons: int  = 0
                self.max_mmr: int   = 0
                self.matched_count: int = 0

                if not _json:
                    return
                self._unpack(_json)

            def _unpack(self, _json: dict):    
                self.mode_slug: str = _json.get("mode_slug")
            
                self.kills: int     = int(_json.get("kills"))
                self.deaths: int    = int(_json.get("deaths"))
                self.kd: float      = float(_json.get("kd"))

                self.wins: int      = int(_json.get("wins"))
                self.losses: int    = int(_json.get("losses"))
                self.wl: float      = float(_json.get("wl"))
                self.abandons: int  = int(_json.get("abandons"))
                self.matched_count: int = self.wins + self.losses + self.abandons

                self.max_mmr: int   = int(_json.get("max_mmr"))
    

    class CurrentSeasonRecords():
        def __init__(self, _json: dict):
            self.ranked: User.CurrentSeasonRecords.Record = User.CurrentSeasonRecords.Record(None)
            self.casual: User.CurrentSeasonRecords.Record = User.CurrentSeasonRecords.Record(None)
            self.deathmatch: User.CurrentSeasonRecords.Record = User.CurrentSeasonRecords.Record(None)
            
            if not _json or isinstance(_json, list):
                return
            self.ranked = User.CurrentSeasonRecords.Record(_json.get('ranked'))
            self.casual = User.CurrentSeasonRecords.Record(_json.get('casual'))
            self.deathmatch = User.CurrentSeasonRecords.Record(_json.get('deathmatch'))


        class Record():
            def __init__(self, _json: dict):
                self.mode_slug:str       = ""
                self.season_slug:str     = ""
                self.region_slug:str     = ""
                self.rank_slug:str       = ""
                self.max_rank_slug:str   = ""
                self.kills:int           = 0
                self.deaths:int          = 0
                self.kd:float            = 0.0
                self.wins:int            = 0
                self.losses:int          = 0
                self.wl:float            = 0.0
                self.abandons:int        = 0
                self.mmr:int             = 0
                self.max_mmr:int         = 0
                self.mmr_change:int      = 0
                self.champion_position:int = 0
            
            def _unpack(self, _json: dict):
                self.mode_slug:str       = parse_str(_json.get("mode_slug"))
                self.season_slug:str     = parse_str(_json.get("season_slug"))
                self.region_slug:str     = parse_str(_json.get("region_slug"))
                self.rank_slug:str       = parse_str(_json.get("rank_slug"))[3:]
                self.max_rank_slug:str   = parse_str(_json.get("max_rank_slug"))[3:]
                self.kills:int           = parse_int(_json.get("kills"))
                self.deaths:int          = parse_int(_json.get("deaths"))
                self.kd:float            = parse_float(_json.get("kd"))
                self.wins:int            = parse_int(_json.get("wins"))
                self.losses:int          = parse_int(_json.get("losses"))
                self.wl:float            = parse_float(_json.get("wl"))
                self.abandons:int        = parse_int(_json.get("abandons"))
                self.mmr:int             = parse_int(_json.get("mmr"))
                self.max_mmr:int         = parse_int(_json.get("max_mmr"))
                self.mmr_change:int      = parse_int(_json.get("mmr_change"))
                self.mmr_change = abs(self.mmr_change)
                self.champion_position:int = parse_int(_json.get("champion_position"))
    
    class PastSeasonRecords():
        def __init__(self, seasons):
            self.seasons: list[User.PastSeasonRecords.Season] = []
            self.keys = []
            if not isinstance(seasons, list):
                return

            self.seasons:list[User.PastSeasonRecords.Season] = [User.PastSeasonRecords.Season(season) for season in seasons]
            self.keys = [record.season_slug for record in self.seasons]

        class Season():
            def __init__(self, season):
                season = season[0]
                self.mode_slug: str     = ""
                self.season_slug: str   = ""
                self.region_slug: str   = ""
                self.rank_slug: str     = ""
                self.max_rank_slug: str = ""
                self.kills: int  = 0
                self.deaths: int = 0
                self.kd: float   = 0.0
                self.wins: int     = 0
                self.losses: int   = 0
                self.wl: float     = 0.0
                self.abandons: int = 0
                self.mmr: int        = 0
                self.max_mmr: int    = 0
                self.mmr_change: int = 0
                self.champion_position: int = 0

                if not isinstance(season, list):
                    return
                
                self._unpack()


            def _unpack(self, _json: dict):
                season = season[0]
                self.mode_slug: str     = parse_str(season.get("mode_slug"))
                self.season_slug: str   = parse_str(season.get("season_slug"))
                self.region_slug: str   = parse_str(season.get("region_slug"))
                self.rank_slug: str     = parse_str(season.get("rank_slug"))[3:]
                self.max_rank_slug: str = parse_str(season.get("max_rank_slug"))[3:]
                self.rank_image_url     = "N/A"
                
                self.kills: int  = parse_int(season.get("kills"))
                self.deaths: int = parse_int(season.get("deaths"))
                self.kd: float   = parse_float(season.get("kd"))
                
                self.wins: int     = parse_int(season.get("wins"))
                self.losses: int   = parse_int(season.get("losses"))
                self.wl: float     = parse_float(season.get("wl"))
                self.abandons: int = parse_int(season.get("abandons"))
                
                self.mmr: int        = parse_int(season.get("mmr"))
                self.max_mmr: int    = parse_int(season.get("max_mmr"))
                self.mmr_change: int = parse_int(season.get("mmr_change"))
                self.mmr_point: str  = "ᐃ" if self.mmr_change > 0 else "ᐁ" if self.mmr_change < 0 else "ᐅ"
                self.mmr_change = abs(self.mmr_change)
                
                self.champion_position: int = parse_int(season.get("champion_position"))
                if self.champion_position > 0:
                    self.rank_image_url = CHAMP_API.format(self.champion_position)

    class Alias():
        def __init__(self, _json: dict):
            self.display_name: str = "N/A"
            self.created_at: datetime = datetime.fromisoformat("1970-01-01T00:00:00+00:00")

            if not _json:
                return
            self.display_name: str = parse_str(_json.get("display_name"))
            self.created_at: datetime = datetime.fromisoformat(_json.get("created_at"))
