class Resources:
    def __init__(self, energy, common_alloy, rare_alloy, concrete, electronic,
                 raw_metal, uranium, limestone, granite, wood, plastic, science_box,
                 liquid_fossil, solid_fossil, hydrogen,
                 food, water, consumer_good,
                 common_alloy_trash, rare_alloy_trash, electronic_trash, wood_trash, plastic_trash, uranium_trash,
                 population, labour, science):
        self.resources = [[energy, common_alloy, rare_alloy, concrete, electronic],
                          [raw_metal, uranium, limestone, granite, wood, plastic, science_box],
                          [liquid_fossil, solid_fossil, hydrogen],
                          [food, water, consumer_good],
                          [common_alloy_trash, rare_alloy_trash, electronic_trash, wood_trash, plastic_trash,
                           uranium_trash],
                          [population, labour, science]]


class RockFiniteResources:
    def __init__(self, raw_metal, uranium, limestone, granite, liquid_fossil, solid_fossil, water):
        self.raw_metal = raw_metal
        self.uranium = uranium
        self.limestone = limestone
        self.granite = granite
        self.liquid_fossil = liquid_fossil
        self.solid_fossil = solid_fossil
        self.water = water
