# A business class

class Business:
    # Class variable (shared by all instances)
    __business_id = 0

    # Constructor (__init__) with 3 strings and a list
    def __init__(self, name, contact, neighborhood, services : list[str], socials : str, description):
        # Instance variables (unique to each instance)
        self.id = Business.__new_business_id()
        self.name = name
        self.contact = contact
        self.neighborhood = neighborhood
        self.services = set(services)
        self.socials = socials.split(',')
        self.description = description

        # Increment the class ID each time a new object is created  
    def __new_business_id():
        curr = Business.__business_id
        Business.__business_id += 1
        return curr
    
    def __str__(self):
        return str(self.name)
    
    def __repr__(self) -> str:
        return str(self.id)

    # Method to display object details (optional)
    def display(self):
        print(f"Instance ID: {self.instance_id}")
        print(f"String 1: {self.string1}")
        print(f"String 2: {self.string2}")
        print(f"String 3: {self.string3}")
        print(f"List Data: {self.list_data}")
