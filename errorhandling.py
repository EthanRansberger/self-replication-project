# errorhandling.py

import logging

# Configure logging
logging.basicConfig(filename='error.log', level=logging.ERROR,
                    format='%(asctime)s %(levelname)s: %(message)s')

def handle_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logging.error(f'Error in {func.__name__}: {str(e)}')
            # Optionally, raise or handle the exception further
            raise e  # Rethrow the exception for further handling
    return wrapper