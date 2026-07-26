raise Exception("NEW MAIN IS RUNNING")
from config import DESIGNATIONS, LOCATIONS
from search import search_jobs
from telegram_sender import send_message

send_message("🚀 NEW VERSION RUNNING")

for designation in DESIGNATIONS[:1]:
    for location in LOCATIONS[:1]:

        query = f'site:linkedin.com "{designation}" "{location}" hiring'

        results = search_jobs(query)

        if not results:
            send_message("❌ No results found.")
        else:
            send_message(
                f"✅ Found {len(results)} results.\n\nFirst Link:\n{results[0]}"
            )
