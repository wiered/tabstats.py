# Tabstats.py - simple tabstats.com parser
Tabstats.py will extract the players statistics from tabstats.com for you to use it. 

It will make object from raw json, so it will be easier for you to use it.

# How to use

## Instalation

```
# from github.com/
git clone https://github.com/wiered/tabstatspy.git
cd tabstatspy
pip install .
```

## Usage

```python
import tabstats

query = "Some username"

with tabstats.Client() as client:
    search-results = client.search(query)
    user = client.get_player(search-results[0].get("name"))
```

The result will contain User object. If parser will unable to find player, it will be empty User object.

## [API References](docs/API.md)
