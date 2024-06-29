from stop_discord_phishing.list import list_phishing_domains


async def phishing_domain_count():
    domains = await list_phishing_domains()
    return len(domains)
