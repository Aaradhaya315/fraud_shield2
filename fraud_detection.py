def is_fraudulent_website(url):
    # Basic placeholder logic
    fraudulent_keywords = ['scam', 'fraud', 'phishing']
    return any(keyword in url.lower() for keyword in fraudulent_keywords)

def is_fraudulent_message(message):
    # Basic placeholder logic
    fraudulent_keywords = ['lottery', 'win', 'prize', 'money', 'urgent']
    return any(keyword in message.lower() for keyword in fraudulent_keywords)
