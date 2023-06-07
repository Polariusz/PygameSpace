from ResourceList import Resources


class BuildingTemplate:
    def __init__(self, image, cost, upkeep, produces, labour_need):
        self.image = image
        self.cost = cost
        self.upkeep = upkeep
        self.produces = produces
        self.labour_need = labour_need


class LowEntrySchool:
    def __init__(self):
        self.image = None
        self.cost = [[0, 300, 0, 600, 0, 0], [0, 0, 0, 0, 500, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0]]
        self.cost = Resources(energy=0, common_alloy=300, rare_alloy=0, concrete=600, electronic=0,
                              military_equipment=0,

                              raw_metal=0, uranium=0, limestone=0, granite=0, wood=500, plastic=0, science_box=0,

                              liquid_fossil=0, solid_fossil=0, hydrogen=0,

                              food=0, water=0, consumer_good=0,
                              common_alloy_trash=0, rare_alloy_trash=0, electronic_trash=0, wood_trash=0,
                              plastic_trash=0, uranium_trash=0,

                              population=0, labour=0, science=0)
        self.upkeep = Resources(energy=1, common_alloy=0, rare_alloy=0, concrete=0, electronic=0,
                                military_equipment=0,

                                raw_metal=0, uranium=0, limestone=0, granite=0, wood=0, plastic=0, science_box=0,

                                liquid_fossil=0, solid_fossil=0, hydrogen=0,

                                food=0, water=0, consumer_good=1,

                                common_alloy_trash=0, rare_alloy_trash=0, electronic_trash=0, wood_trash=0,
                                plastic_trash=0, uranium_trash=0,

                                population=0, labour=0, science=0)
        self.produces = ["LowEducation", 4]
        self.labour_need = 100
        self.building = BuildingTemplate(self.image, self.cost, self.upkeep, self.produces, self.labour_need)


class HighEntrySchool:
    def __init__(self):
        self.image = None
        self.cost = Resources(energy=0, common_alloy=400, rare_alloy=0, concrete=800, electronic=200,
                              military_equipment=0,

                              raw_metal=0, uranium=0, limestone=0, granite=0, wood=300, plastic=0, science_box=0,

                              liquid_fossil=0, solid_fossil=0, hydrogen=0,

                              food=0, water=0, consumer_good=0,
                              common_alloy_trash=0, rare_alloy_trash=0, electronic_trash=0, wood_trash=0,
                              plastic_trash=0, uranium_trash=0,

                              population=0, labour=0, science=0)
        self.upkeep = Resources(energy=1, common_alloy=0, rare_alloy=0, concrete=0, electronic=0,
                                military_equipment=0,

                                raw_metal=0, uranium=0, limestone=0, granite=0, wood=0, plastic=0, science_box=0,

                                liquid_fossil=0, solid_fossil=0, hydrogen=0,

                                food=0, water=0, consumer_good=2,

                                common_alloy_trash=0, rare_alloy_trash=0, electronic_trash=0, wood_trash=0,
                                plastic_trash=0, uranium_trash=0,

                                population=0, labour=0, science=0)
        self.produces = ["HighEducation", 3]
        self.labour_need = 200
        self.building = BuildingTemplate(self.image, self.cost, self.upkeep, self.produces, self.labour_need)


class University:
    def __init__(self):
        self.image = None
        self.cost = Resources(energy=0, common_alloy=400, rare_alloy=100, concrete=1000, electronic=400,
                              military_equipment=0,

                              raw_metal=0, uranium=0, limestone=0, granite=0, wood=0, plastic=0, science_box=0,

                              liquid_fossil=0, solid_fossil=0, hydrogen=0,

                              food=0, water=0, consumer_good=0,
                              common_alloy_trash=0, rare_alloy_trash=0, electronic_trash=0, wood_trash=0,
                              plastic_trash=0, uranium_trash=0,

                              population=0, labour=0, science=0)
        self.upkeep = Resources(energy=2, common_alloy=0, rare_alloy=0, concrete=0, electronic=0,
                                military_equipment=0,

                                raw_metal=0, uranium=0, limestone=0, granite=0, wood=0, plastic=0, science_box=0,

                                liquid_fossil=0, solid_fossil=0, hydrogen=0,

                                food=0, water=0, consumer_good=3,

                                common_alloy_trash=0, rare_alloy_trash=0, electronic_trash=0, wood_trash=0,
                                plastic_trash=0, uranium_trash=0,

                                population=0, labour=0, science=0)
        self.produces = ["UniEducation", 1]
        self.labour_need = 400
        self.building = BuildingTemplate(self.image, self.cost, self.upkeep, self.produces, self.labour_need)


class VeganFarm:
    def __init__(self):
        self.image = None
        self.cost = Resources(energy=0, common_alloy=300, rare_alloy=0, concrete=600, electronic=0,
                              military_equipment=0,

                              raw_metal=0, uranium=0, limestone=0, granite=0, wood=500, plastic=0, science_box=0,

                              liquid_fossil=0, solid_fossil=0, hydrogen=0,

                              food=0, water=0, consumer_good=0,
                              common_alloy_trash=0, rare_alloy_trash=0, electronic_trash=0, wood_trash=0,
                              plastic_trash=0, uranium_trash=0,

                              population=0, labour=0, science=0)
        self.upkeep = Resources(energy=1, common_alloy=0, rare_alloy=0, concrete=0, electronic=0,
                                military_equipment=0,

                                raw_metal=0, uranium=0, limestone=0, granite=0, wood=0, plastic=0, science_box=0,

                                liquid_fossil=0, solid_fossil=0, hydrogen=0,

                                food=0, water=0, consumer_good=1,

                                common_alloy_trash=0, rare_alloy_trash=0, electronic_trash=0, wood_trash=0,
                                plastic_trash=0, uranium_trash=0,

                                population=0, labour=0, science=0)
        self.produces = None
        self.labour_need = None
        self.building = BuildingTemplate(self.image, self.cost, self.upkeep, self.produces, self.labour_need)


class MeatFarm:
    def __init__(self):
        self.image = None
        self.cost = None
        self.upkeep = None
        self.produces = None
        self.labour_need = None
        self.building = BuildingTemplate(self.image, self.cost, self.upkeep, self.produces, self.labour_need)


class Hydroponics:
    def __init__(self):
        self.image = None
        self.cost = None
        self.upkeep = None
        self.produces = None
        self.labour_need = None
        self.building = BuildingTemplate(self.image, self.cost, self.upkeep, self.produces, self.labour_need)


class InfrastructureCentre:
    def __init__(self):
        self.image = None
        self.cost = None
        self.upkeep = None
        self.produces = None
        self.labour_need = None
        self.building = BuildingTemplate(self.image, self.cost, self.upkeep, self.produces, self.labour_need)


class TreeFarm:
    def __init__(self):
        self.image = None
        self.cost = None
        self.upkeep = None
        self.produces = None
        self.labour_need = None
        self.building = BuildingTemplate(self.image, self.cost, self.upkeep, self.produces, self.labour_need)


class Clinic:
    def __init__(self):
        self.image = None
        self.cost = None
        self.upkeep = None
        self.produces = None
        self.labour_need = None
        self.building = BuildingTemplate(self.image, self.cost, self.upkeep, self.produces, self.labour_need)


class Hospital:
    def __init__(self):
        self.image = None
        self.cost = None
        self.upkeep = None
        self.produces = None
        self.labour_need = None
        self.building = BuildingTemplate(self.image, self.cost, self.upkeep, self.produces, self.labour_need)


class TransportationFactory:
    def __init__(self):
        self.image = None
        self.cost = None
        self.upkeep = None
        self.produces = None
        self.labour_need = None
        self.building = BuildingTemplate(self.image, self.cost, self.upkeep, self.produces, self.labour_need)


class ConsumerGoodsFactory:
    def __init__(self):
        self.image = None
        self.cost = None
        self.upkeep = None
        self.produces = None
        self.labour_need = None
        self.building = BuildingTemplate(self.image, self.cost, self.upkeep, self.produces, self.labour_need)


class RecycleCentre:
    def __init__(self):
        self.image = None
        self.cost = None
        self.upkeep = None
        self.produces = None
        self.labour_need = None
        self.building = BuildingTemplate(self.image, self.cost, self.upkeep, self.produces, self.labour_need)


class NaturalDisasterPreventionCentre:
    def __init__(self):
        self.image = None
        self.cost = None
        self.upkeep = None
        self.produces = None
        self.labour_need = None
        self.building = BuildingTemplate(self.image, self.cost, self.upkeep, self.produces, self.labour_need)


class EnforcerCentre:
    def __init__(self):
        self.image = None
        self.cost = None
        self.upkeep = None
        self.produces = None
        self.labour_need = None
        self.building = BuildingTemplate(self.image, self.cost, self.upkeep, self.produces, self.labour_need)


class MilitaryEquipmentFactory:
    def __init__(self):
        self.image = None
        self.cost = None
        self.upkeep = None
        self.produces = None
        self.labour_need = None
        self.building = BuildingTemplate(self.image, self.cost, self.upkeep, self.produces, self.labour_need)


class MilitaryCentre:
    def __init__(self):
        self.image = None
        self.cost = None
        self.upkeep = None
        self.produces = None
        self.labour_need = None
        self.building = BuildingTemplate(self.image, self.cost, self.upkeep, self.produces, self.labour_need)


class FossilPowerPlant:
    def __init__(self):
        self.image = None
        self.cost = None
        self.upkeep = None
        self.produces = None
        self.labour_need = None
        self.building = BuildingTemplate(self.image, self.cost, self.upkeep, self.produces, self.labour_need)


class GreenPowerPlant:
    def __init__(self):
        self.image = None
        self.cost = None
        self.upkeep = None
        self.produces = None
        self.labour_need = None
        self.building = BuildingTemplate(self.image, self.cost, self.upkeep, self.produces, self.labour_need)


class NuclearPowerPlant:
    def __init__(self):
        self.image = None
        self.cost = None
        self.upkeep = None
        self.produces = None
        self.labour_need = None
        self.building = BuildingTemplate(self.image, self.cost, self.upkeep, self.produces, self.labour_need)


class FusionPowerPlant:
    def __init__(self):
        self.image = None
        self.cost = None
        self.upkeep = None
        self.produces = None
        self.labour_need = None
        self.building = BuildingTemplate(self.image, self.cost, self.upkeep, self.produces, self.labour_need)


class HydrogenFactory:
    def __init__(self):
        self.image = None
        self.cost = None
        self.upkeep = None
        self.produces = None
        self.labour_need = None
        self.building = BuildingTemplate(self.image, self.cost, self.upkeep, self.produces, self.labour_need)


class ConcreteFactory:
    def __init__(self):
        self.image = None
        self.cost = None
        self.upkeep = None
        self.produces = None
        self.labour_need = None
        self.building = BuildingTemplate(self.image, self.cost, self.upkeep, self.produces, self.labour_need)


class ElectronicFactory:
    def __init__(self):
        self.image = None
        self.cost = None
        self.upkeep = None
        self.produces = None
        self.labour_need = None
        self.building = BuildingTemplate(self.image, self.cost, self.upkeep, self.produces, self.labour_need)


class PlasticFactory:
    def __init__(self):
        self.image = None
        self.cost = None
        self.upkeep = None
        self.produces = None
        self.labour_need = None
        self.building = BuildingTemplate(self.image, self.cost, self.upkeep, self.produces, self.labour_need)


class SurfaceMiner:
    def __init__(self):
        self.image = None
        self.cost = None
        self.upkeep = None
        self.produces = None
        self.labour_need = None
        self.building = BuildingTemplate(self.image, self.cost, self.upkeep, self.produces, self.labour_need)


class DeepMiners:
    def __init__(self):
        self.image = None
        self.cost = None
        self.upkeep = None
        self.produces = None
        self.labour_need = None
        self.building = BuildingTemplate(self.image, self.cost, self.upkeep, self.produces, self.labour_need)


class DeepOceanMiners:
    def __init__(self):
        self.image = None
        self.cost = None
        self.upkeep = None
        self.produces = None
        self.labour_need = None
        self.building = BuildingTemplate(self.image, self.cost, self.upkeep, self.produces, self.labour_need)


class CommonAlloyFactory:
    def __init__(self):
        self.image = None
        self.cost = None
        self.upkeep = None
        self.produces = None
        self.labour_need = None
        self.building = BuildingTemplate(self.image, self.cost, self.upkeep, self.produces, self.labour_need)


class RareAlloyFactory:
    def __init__(self):
        self.image = None
        self.cost = None
        self.upkeep = None
        self.produces = None
        self.labour_need = None
        self.building = BuildingTemplate(self.image, self.cost, self.upkeep, self.produces, self.labour_need)


class ScienceBoxFactory:
    def __init__(self):
        self.image = None
        self.cost = None
        self.upkeep = None
        self.produces = None
        self.labour_need = None
        self.building = BuildingTemplate(self.image, self.cost, self.upkeep, self.produces, self.labour_need)


class SpaceShipFactory:
    def __init__(self):
        self.image = None
        self.cost = None
        self.upkeep = None
        self.produces = None
        self.labour_need = None
        self.building = BuildingTemplate(self.image, self.cost, self.upkeep, self.produces, self.labour_need)
