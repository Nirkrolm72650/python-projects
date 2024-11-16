import uuid

class Student():
    def __init__(self, id ,lastname, firstname, email):
        self.id = id
        self.lastname = lastname
        self.firstname = firstname
        self.email = email
        
        
        
    def to_dict(self):
        # Retourne un dictionnaire avec les attributs de l'étudiant
        return {
            'id': self.id,
            'lastname': self.lastname,
            'firstname': self.firstname,
            'email': self.email
        }