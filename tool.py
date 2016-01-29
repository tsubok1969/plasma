import math
class Calc():
    def __init__(self):
        self.LVEL = 299792458.
        self.ECHG = 1.60217662e-19

        self.EPSL = 8.85418782e-12
        self.PRMB = 1./(self.LVEL**2*self.EPSL)

        self.CENT = 1.0e-2
        self.MILI = 1.0e-3
        self.MEGA = 1.0e+6
        self.NANO = 1.0e-9
        self.KILO = 1.0e+3
        self.GIGA = 1.0e+9
        self.MICR = 1.0e-6

        self.PMAS = 1.6726219e-27
        self.EMAS = 9.10938356e-31

        self.BOLZ = 1.38064852e-23

    def mass(self, species):
        if species == 0:
            return self.EMAS
        else:
            return self.PMAS

    def joule2ev(self, energy):
        return energy/self.ECHG
    def ev2joule(self, evolt):
        return evolt*self.ECHG

    def joule2vel(self, species, energy):
        mass = self.mass(species)
        return math.sqrt(2.0*energy/mass)

    def vel2joule(self, species, velocity):
        mass = self.mass(species)
        return 0.5*mass*velocity**2

    def lorentz_factor(self, vel):
        return 1./math.sqrt(1. - vel**2/self.LVEL**2)

    def alfven_velocity(self,rho,bmag):
        return bmag/math.sqrt(self.PRMB*self.PMAS*rho)

    def plasma_frequency(self, species, rho):
        mass = self.mass(species)
        return math.sqrt(rho*self.ECHG**2/mass/self.EPSL)

    def cyclotron_frequency(self, species, mag):
        mass = self.mass(species)
        return self.ECHG*mag/mass

    def inertial_length(self, species, rho):
        freq = plasma_frequency(species, rho)
        return self.LVEL/freq

    def thermal_velocity(self, species, eth):
        mass = self.mass(species)
        return math.sqrt(eth/mass)
