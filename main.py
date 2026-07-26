from config import DESIGNATIONS, LOCATIONS
from search import search_jobs

for designation in DESIGNATIONS:
    for location in LOCATIONS:

        query = f'site:linkedin.com "{designation}" "{location}" hiring'

        print("=" * 80)
        print(query)

        results = search_jobs(query)

        print(f"Found {len(results)} results")

        for link in results[:5]:
            print(link)
