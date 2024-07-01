def handle_errors(func):
    """
    Decorator to handle exceptions for a function.
    
    Args:
        func (callable): The function to decorate.
        
    Returns:
        callable: The decorated function.
    """
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"An error occurred: {e}")
    return wrapper
