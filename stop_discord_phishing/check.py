from stop_discord_phishing.list import list_phishing_domains


async def check_message(content: str):
    """
    Check if a message contains a phishing domain
    :param: content: str - the message to check
    :returns: bool - True if the message contains a phishing domain, False otherwise
    """
    domains = await list_phishing_domains()
    return any(domain in content for domain in domains)


async def check_domain(domain: str):
    """
    Check if a domain is a phishing domain
    :param: domain: str - the domain to check
    :returns: bool - True if the domain is a phishing domain, False otherwise
    """
    domains = await list_phishing_domains()
    return domain in domains
