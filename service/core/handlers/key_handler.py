import os
from service.core.exceptions import VariableNotFoundException


class KeyHandler:
    """
    Class that allows to manage the environment keys
    """

    @property
    def encryption_key(self):
        return self.load_variable("encryption_key")

    @property
    def encryption_iv(self):
        return self.load_variable("encryption_iv")

    # @property
    # def database_host(self):
    #     return self.load_variable("POSTGRES_HOST")
    
    # @property
    # def database_port(self):
    #     return self.load_variable("POSTGRES_PORT")

    # @property
    # def database_user(self):
    #     return self.load_variable("POSTGRES_USER")

    # @property
    # def database_password(self):
    #     return self.load_variable("POSTGRES_PASSWORD")

    # @property
    # def database_db(self):
    #     return self.load_variable("POSTGRES_DB")


    def load_variable(self, variable):
        var = os.environ.get(variable)
        if var is None:
            raise VariableNotFoundException(variable)
        else:
            return var
