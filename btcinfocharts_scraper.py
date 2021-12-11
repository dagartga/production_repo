def current_date():
    """
        Returns the current date
        in a string format 'yyyy/mm/dd'
    """
    
    
    from datetime import date
    
    # get the current date
    today = date.today()
    return str(today).replace('-', '/')