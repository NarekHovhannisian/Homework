# Unique Email Addresses
def numUniqueEmails(emails):
    unique = []
    for email in emails:
        local, domain = email.split('@')
        if '+' in local:
            local = local[:local.index('+')]
        local = "".join(local.split('.'))
        unique.append("".join([local, '@', domain]))
    return len(set(unique))
