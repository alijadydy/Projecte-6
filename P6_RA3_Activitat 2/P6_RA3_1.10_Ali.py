# Autor: Ali
# Data: 09/05/2025
# Exercici: 10 - Email d’un usuari
# Descripció: Classe CompteUsuari amb email validat.

class CompteUsuari:
    def __init__(self, email):
        self.__email = email

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, nou_email):
        if "@" in nou_email and "." in nou_email:
            self.__email = nou_email
