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

def parse_str(value) -> str:
    if not value:
        return "N/A"
    
    if isinstance(value, str):
        return value
    
    return "N/A"

def parse_int(value) -> int:
    if not value:
        return 0
    
    if isinstance(value, int):
        return value
    
    if value[0] == "-":
        value = value[1:]
        
    if value.isnumeric():
        return int(value)
    
    return 0

def parse_float(value) -> float:
    if not value:
        return 0.0
    
    if isinstance(value, float) or isinstance(value, int):
        return value  
    
    _key = value.replace(".", "", 1)
    if value[0] == "-":
        _key = _key[1:]
        
    if _key.isnumeric():
        return float(value)
    
    return 0.0

def parse_bool(value) -> bool:
    """At all costs, tries to return boolean value, even if not boolean value given"""
    if not value:
        return False
    
    if isinstance(value, bool):
        return value
    
    if value == "true":
        return True
        
    return False
    