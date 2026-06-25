def format_duration(seconds):
    
    result = []
    
    if seconds == 0:
        return "now"
​
    minute = 60
    hour = 60 * minute
    day = 24 * hour
    year = 365 * day
​
    years = seconds // year
    seconds = seconds % year
    days = seconds // day
    seconds = seconds % day
    hours = seconds // hour
    seconds = seconds % hour
    minutes = seconds // minute
    seconds = seconds % minute
    
    if years == 1:
        result.append(f"{years} year")
    elif years > 1:
        result.append(f"{years} years")
    
    if days == 1:
        result.append(f"{days} day")
    elif days > 1:
        result.append(f"{days} days")
​
    if hours == 1:
        result.append(f"{hours} hour")
    elif hours > 1:
        result.append(f"{hours} hours")
​
    if minutes == 1:
        result.append(f"{minutes} minute")
    elif minutes > 1:
        result.append(f"{minutes} minutes")
​
    if seconds == 1:
        result.append(f"{seconds} second")
    elif seconds > 1:
        result.append(f"{seconds} seconds")
        
    if len(result) == 1:
        return result[0]
    if len(result) == 2:
        return " and ".join(result)
​
    return ", ".join(result[:-1]) + " and " + result[-1]
    