# A business class
class Business:
    # Class variable (shared by all instances)
    __business_id = 0

    # Constructor (__init__) with 3 strings and a list
    def __init__(self, name, contact, neighborhood, services: list[str], socials: str, description):
        # Instance variables (unique to each instance)
        self.id = Business.__new_business_id()
        self.name = name
        self.contact = contact
        self.neighborhood = neighborhood
        self.services = set(services)
        self.socials = socials.split(',')
        self.description = description

    # Increment the class ID each time a new object is created
    @staticmethod
    def __new_business_id():
        curr = Business.__business_id
        Business.__business_id += 1
        return curr

    # Getter for business ID
    @property
    def business_id(self):
        return self.id

    # Getter for name
    @property
    def get_name(self):
        return self.name

    # Getter for contact
    @property
    def get_contact(self):
        return self.contact

    # Getter for neighborhood
    @property
    def get_neighborhood(self):
        return self.neighborhood

    # Getter for services (returns the set of services)
    @property
    def get_services(self):
        return self.services

    # Getter for socials (returns the list of socials)
    @property
    def get_socials(self):
        return self.socials

    # Getter for description
    @property
    def get_description(self):
        return self.description

    def __str__(self):
        return str(self.name)

    def __repr__(self) -> str:
        return str(self.id)
