"""
Parameter weekday is True if it is a weekday
Parameter vacation is True if it is a vacation weekday
We sleep in if it is not a weekday or if we're on vacation
Return True if we sleep in
"""

def sleep_in(weekday, vacation):
    if not weekday or vacation:
        return True
    else:
        return False
