from tool import Calc

c = Calc()

print ("Choose the quantity:")
print ("1: Alfven velocity\n2: Cyclotron frequency\n3: Plasma frequency\n4: Velocity to eV")
quant = input()
quant = int(quant)

if quant == 1:
    rho, mag = map(float, input("Input the plasma number density (/cc) and magnetic field magnitude (nT)\n").split())
    va = c.alfven_velocity(rho/c.CENT**3, mag*c.NANO) / c.KILO
    print('Va = %f km/s' % va)
elif quant == 2:
    species, mag = map(float, input("Input the plasma species (0:electron 1:proton) and the magnetic field magnitude (nT)\n").split())
    cfreq = c.cyclotron_frequency(species, mag*c.NANO) / c.KILO
    print('Omega_c = %f kHz' % cfreq)
else quant == 3:
    species, rho = map(float, input("Input the plasma species (0:electron 1:proton) and its number density (/cc)\n").split())
    pfreq = c.plasma_frequency(species, rho/c.CENT**3) / c.KILO
    print('Omega_p = %f kHz' % pfreq)
else:
    species, vel = map(float, input("Input the plasma species (0:electron 1:proton) and the velocity (km/s)").split())
    ene = c.vel2joule(species, vel*c.KILO)
    ev = c.joule2ev(ene) / c.KILO
    print('Energy = %f keV' % ev)
