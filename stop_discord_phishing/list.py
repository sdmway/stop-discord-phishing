import aiohttp
from cachetools import TTLCache

PHISHING_LINKS = "https://raw.githubusercontent.com/sdmway/stop-discord-phishing/main/domain_list.json"

cache = TTLCache(maxsize=1, ttl=1800)


async def fetch_phishing_domains():
    if "phishing_domains" in cache:
        return cache["phishing_domains"]

    async with aiohttp.ClientSession() as session:
        async with session.get(url=PHISHING_LINKS) as response:
            data = await response.json(content_type=None)
            cache["phishing_domains"] = data
            return data


async def list_phishing_domains():
    return (await fetch_phishing_domains())["domains"]
