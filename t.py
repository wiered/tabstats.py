import tabstats

with tabstats.Client() as client:
    search_results = client.search(query='python')
    print(search_results)
