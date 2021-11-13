

class VariableNotFoundException(Exception):
    """
    Exception for variable lookup.
    """

    def __init__(self, variable):
        self.message = f"The variable {variable} doesn't exist in the environment."
        super().__init__(self.message)
