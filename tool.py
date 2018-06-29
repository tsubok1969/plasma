import numpy as np
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

    def mass(self, proton=True):
        if proton:
            return self.PMAS
        else:
            return self.EMAS

    def joule2ev(self, energy):
        return energy/self.ECHG
    def ev2joule(self, evolt):
        return evolt*self.ECHG

    def joule2vel(self, energy, proton=True):
        mass = self.mass(proton)
        return np.sqrt(2.0*energy/mass)

    def vel2joule(self, velocity, proton=True):
        mass = self.mass(proton)
        return 0.5*mass*velocity**2

    def lorentz_factor(self, vel):
        return 1./np.sqrt(1. - vel**2/self.LVEL**2)

    def alfven_velocity(self,rho,bmag):
        return bmag/np.sqrt(self.PRMB*self.PMAS*rho)

    def plasma_frequency(self, rho, proton=True):
        mass = self.mass(proton)
        return np.sqrt(rho*self.ECHG**2/mass/self.EPSL)

    def cyclotron_frequency(self, mag, proton=True):
        mass = self.mass(proton)
        return self.ECHG*mag/mass

    def inertial_length(self, rho, proton=True):
        freq = plasma_frequency(rho, proton)
        return self.LVEL/freq

    def thermal_velocity(self, eth, proton=True):
        mass = self.mass(proton)
        return np.sqrt(eth/mass)

    def mag_pressure(self, mag):
        return 0.5*mag**2/self.PRMB

    def plasma_beta(self, pre, mag):
        return self.ev2joule(pre)/self.mag_pressure(mag)

    def omegap2density(self, wp, proton=True):
        mass = self.mass(proton)
        return wp**2*self.EPSL*mass/self.ECHG**2
