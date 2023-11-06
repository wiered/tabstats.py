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

""" Get variable from json

    Args:
        _json (dict): json with player data

    Returns:
        typed variable
"""  

def parse_str(key) -> str:
    if not key:
        return "N/A"
    
    if isinstance(key, str):
        return key
    
    return "N/A"

def parse_int(key) -> int:
    if not key:
        return 0
    
    if isinstance(key, int):
        return key
    
    if key[0] == "-":
        key = key[1:]
        
    if key.isnumeric():
        return int(key)
    
    return 0

def parse_float(key) -> float:
    if not key:
        return 0.0
    
    if isinstance(key, float) or isinstance(key, int):
        return key  
    
    _key = key.replace(".", "", 1)
    if key[0] == "-":
        _key = _key[1:]
        
    if _key.isnumeric():
        return float(key)
    
    return 0.0

def parse_bool(key) -> bool:
    if not key:
        return False
    
    if isinstance(key, bool):
        return key
    
    if key == "true":
        return True
    
    return False
