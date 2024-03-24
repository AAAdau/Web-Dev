def alarm_clock(day, vacation):
    # Check if we are on vacation
    if vacation:
        # If we are on vacation, adjust the alarm time accordingly
        if day in [0, 6]:  # Weekend
            return 'off'
        else:  # Weekday
            return '10:00'
    else:
        # If we are not on vacation, determine the alarm time based on the day of the week
        if day in [0, 6]:  # Weekend
            return '10:00'
        else:  # Weekday
            return '7:00'

# Test cases
print(alarm_clock(1, False))   # Output: '7:00'
print(alarm_clock(5, False))   # Output: '7:00'
print(ala
