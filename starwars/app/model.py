
class StarshipModel:
    def __init__(self, starship) -> None:
        self.status = starship['status']
        self.name = starship['model']
        self.starship_class = starship['starship_class']
        self.manufacturer = starship['manufacturer']
        self.cost_in_credits = starship['cost_in_credits']
        self.length = starship['length']
        self.crew = starship['crew']
        self.passengers = starship['passengers']
        self.max_atmosphering_speed = starship['max_atmosphering_speed']
        self.mglt = starship['MGLT']
        self.cargo_capacity = starship['cargo_capacity']
        self.consumables = starship['consumables']
        self.films = starship['films']
        self.pilots = starship['pilots']
