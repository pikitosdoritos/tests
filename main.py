def was_package_received_yesterday(tz_from, tz_to, start, duration):
    finish = (start - (tz_from - tz_to)) + duration
     
    return finish < 0

print(was_package_received_yesterday(6, 3, 1, 1))

describe_age=lambda a:f"You're a(n) {'kid' if a < 13 else 'teenager' if a < 18 else 'adult' if a < 65 else 'elderly'}" 

describe_age=lambda a:f"You're a(n) {'kid' if a<13 else 'teenager' if a<18 else 'adult' if a<65 else 'elderly'}"