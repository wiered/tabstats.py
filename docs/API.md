# API References

## Table of Contents
- [tabstats.**Client**](#class-tabstatsclient)
    + [tabstats.Client.**search**](#tabstatsclientsearch)
    + [tabstats.Client.**get_player**](#tabstatsclientget_player)
- [tabstats.**User**](#class-tabstatsuser)
    + [tabstats.User.**Profile**](#class-tabstatsuserprofile)
    + [tabstats.User.**SummaryGraphData**](#class-tabstatsusersummarygraphdata)
    + [tabstats.User.SummaryGraphData.**GraphData**](#class-tabstatsusersummarygraphdatagraphdata)
    + [tabstats.User.**GeneralRecords**](#class-tabstatsusergeneralrecords)
    + [tabstats.User.GeneralRecords.**Record**](#class-tabstatsusergeneralrecordsrecord)
    + [tabstats.User.**CurrentSeasonRecords**](#class-tabstatsusercurrentseasonrecords)
    + [tabstats.User.CurrentSeasonRecords.**Record**](#class-tabstatsusercurrentseasonrecordsrecord)
    + [tabstats.User.**PastSeasonRecords**](#class-tabstatsuserpastseasonrecords)
    + [tabstats.User.PastSeasonRecords.**Season**](#class-tabstatsuserpastseasonrecordsseason)
    + [tabstats.User.**Alias**](#class-tabstatsuseralias)

## class tabstats.Client

### Methods: 
- [**search**](#tabstatsclientsearch)
- [**get_player**](#tabstatsclientget_player)

## tabstats.Client.search

```py
Search user by name

Args: 
    query(str): search query

Returns:
    list[dict]: search results
```

### search result looks like this:

```py
[
    {
        'name': 'Username', 
        'id': 'fake-ubi-id', 
        'level': 0, 
        'rank': 'N/A'
    },
    {
        'name': 'Username2', 
        'id': 'fake-ubi-id2', 
        'level': 0, 
        'rank': 'N/A'
    },
]
```

## tabstats.Client.get_player

```py
Parse player statistics by his ubisoft id

Args:
    player_id(str): ubisoft id of player

Returns:
    User: overall player data
```

## class tabstats.User

```python
Attributes:
    profile: User.Profile
    name: str
    social_profile: dict
    game_bans: list
    profile_bans: list
    top_region: str
    region_breakdown: dict
    last_played_at: datetime.datetime
    summary_graph_data: User.SummaryGraphData
    general_records: User.GeneralRecords
    current_season_records: User.CurrentSeasonRecords
    past_season_ranked_records: User.PastSeasonRecords
    aliases: list[User.Alias]
    
```

## class tabstats.User.Profile

```python
Attributes:
    display_name: str
    profile_views: int
    user_id: str
    player_id: str
    level: int
    kd: float
    is_cheater: bool
    is_vereified: bool
    display_ban: str
    json_url: str
    avatar_url: str
    profile_url: str
    platform_slug: str
    updated_at: datetime.datetime
    can_update_at: datetime.datetime
```

## class tabstats.User.SummaryGraphData

```python
Attributes:
    ranked: list[User.SummaryGraphData.GraphData]
    casual: list[User.SummaryGraphData.GraphData]
    deathmatch: list[User.SummaryGraphData.GraphData]
```

## class tabstats.User.SummaryGraphData.GraphData

```python
Attributes:
    kills: int
    deaths: int
    wins: int
    losses: int
    abandons: int
    lowest_mmr: int
    highest_mmr: int
    mode_slug: str
    _date
```

## class tabstats.User.GeneralRecords

```python
Attributes:
    ranked: User.GeneralRecords.Record
    records: dict
```

## class tabstats.User.GeneralRecords.Record

```python
Attributes:
    mode_slug: str
    kills: int
    deaths: int
    kd: float
    wins: int
    losses: int
    wl: float
    abandons: int
    max_mmr: int
    matched_count: int
```

## class tabstats.User.CurrentSeasonRecords

```python
Attributes:
    ranked: User.CurrentSeasonRecords.Record
    casual: User.CurrentSeasonRecords.Record
    deathmatch: User.CurrentSeasonRecords.Record
```

## class tabstats.User.CurrentSeasonRecords.Record

```python
Attributes:
    mode_slug:str
    season_slug:str
    region_slug:str
    rank_slug:str
    max_rank_slug:str
    kills:int
    deaths:int
    kd:float
    wins:int
    losses:int
    wl:float
    abandons:int
    mmr:int 
    max_mmr:int
    mmr_change:int
    champion_position:int
```

## class tabstats.User.PastSeasonRecords

```python
Attributes:
    seasons: list[User.PastSeasonRecords.Season]
    keys: list
```

## class tabstats.User.PastSeasonRecords.Season

```python
Attributes:
    mode_slug: str
    season_slug: str
    region_slug: str
    rank_slug: str
    max_rank_slug: str
    kills: int
    deaths: int
    kd: float
    wins: int
    losses: int
    wl: float
    abandons: int
    mmr: int
    max_mmr: int
    mmr_change: int
    champion_position: int
```

## class tabstats.User.Alias

```python
Attributes:
    display_name: str
    created_at: datetime.datetime
```
