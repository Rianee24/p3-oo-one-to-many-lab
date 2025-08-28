class Pet:
    PET_TYPES = ['dog', 'cat', 'rodent', 'bird', 'reptile', 'exotic']
    all = []

    def __init__(self, name, pet_type, owner=None):
        if pet_type not in Pet.PET_TYPES:
            raise ValueError(f"Invalid pet type: {pet_type}")
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        Pet.all.append(self)

        # If an owner is provided, link the pet to the owner
        if owner:
            owner.add_pet(self)


class Owner:
    def __init__(self, name):
        self.name = name
        self._pets = []

    def pets(self):
        """Return all pets belonging to this owner"""
        return self._pets

    def add_pet(self, pet):
        """Validate the object and add a Pet to this owner's collection"""
        if not isinstance(pet, Pet):
            raise TypeError("pet must be an instance of Pet")
        if pet not in self._pets:
            self._pets.append(pet)
            pet.owner = self

    def get_sorted_pets(self):
        """Return the owner's pets sorted by name"""
        return sorted(self._pets, key=lambda pet: pet.name)

