class PlayerResources:
    def __init__(self, energy, minerals, metals, retail_goods, food, water, fossil_fuels, rare_elements, chemicals,
                 bio_resources, science, population, labour):
        self.energy = energy
        self.minerals = minerals
        self.metals = metals
        self.retail_goods = retail_goods
        self.food = food
        self.water = water
        self.fossil_fuels = fossil_fuels
        self.rare_elements = rare_elements
        self.chemicals = chemicals
        self.bio_resources = bio_resources
        self.science = science
        self.population = population
        self.labour = labour

    def update_energy(self, e):
        self.energy = e

    def update_minerals(self, m):
        self.minerals = m

    def update_metals(self, m):
        self.metals = m

    def update_retail_goods(self, r):
        self.retail_goods = r

    def update_food(self, f):
        self.food = f

    def update_water(self, w):
        self.water = w

    def update_fossil_fuels(self, f):
        self.fossil_fuels = f

    def update_rare_elements(self, re):
        self.rare_elements = re

    def update_chemicals(self, c):
        self.chemicals = c

    def update_bio_resources(self, br):
        self.bio_resources = br

    def update_science(self, s):
        self.science = s

    def update_population(self, p):
        self.population = p

    def update_labour(self, proletariat):
        self.labour = proletariat


class BigRockResources:
    def __init__(self, space, energy, minerals, metals, retail_goods, food, water, fossil_fuels, rare_elements,
                 chemicals, bio_resources, science, population, labour):
        self.space = space
        self.energy = energy
        self.minerals = minerals
        self.metals = metals
        self.retail_goods = retail_goods
        self.food = food
        self.water = water
        self.fossil_fuels = fossil_fuels
        self.rare_elements = rare_elements
        self.chemicals = chemicals
        self.bio_resources = bio_resources
        self.science = science
        self.population = population
        self.labour = labour

    def update_energy(self, e):
        self.energy = e

    def update_minerals(self, m):
        self.minerals = m

    def update_metals(self, m):
        self.metals = m

    def update_retail_goods(self, r):
        self.retail_goods = r

    def update_food(self, f):
        self.food = f

    def update_water(self, w):
        self.water = w

    def update_fossil_fuels(self, f):
        self.fossil_fuels = f

    def update_rare_elements(self, re):
        self.rare_elements = re

    def update_chemicals(self, c):
        self.chemicals = c

    def update_bio_resources(self, br):
        self.bio_resources = br

    def update_science(self, s):
        self.science = s

    def update_population(self, p):
        self.population = p

    def update_labour(self, proletariat):
        self.labour = proletariat
