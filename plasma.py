class Calc():
    def __init__(self):
        self.LVEL = 299792458.
        self.ECHG = 1.60217662e-19

        self.EPSL = 8.85418782e-12
        self.PRMB = 1./(self.LVEL**2*self.EPSL)

        self.MILI = 1.0e-3
        self.MEGA = 1.0e+6
        self.NANO = 1.0e-9
        self.KILO = 1.0e+3
        self.GIGA = 1.0e+9
        self.MICR = 1.0e-6

        self.PMAS = 1.6726219e-27
        self.EMAS = 9.10938356e-31

        self.BOLZ = 1.38064852e-23

    def joule2ev(self, energy):
        return energy/self.ECHG
    def ev2joule(self, evolt):
        return evolt*self.ECHG

    def joule2vel(self, species, energy):
        import math
        if species == 0:
            mass = self.EMAS
        else:
            mass = self.PMAS
        return math.sqrt(2.0*energy/mass)

    def vel2joule(self, species, velocity):
        if species == 0:
            mass = self.EMAS
        else:
            mass = self.PMAS
        return 0.5*mass*velocity**2

    def lfactor(self, vel):
        import math
        return 1./math.sqrt(1. - vel**2/self.LVEL**2)
