from tool import Calc

c = Calc()

bool = True
while bool:
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
        if species == 0:
            proton = False
        else:
            proton = True
        cfreq = c.cyclotron_frequency(mag*c.NANO, proton) / c.KILO
        print('Omega_c = %f kHz' % cfreq)
    elif quant == 3:
        species, rho = map(float, input("Input the plasma species (0:electron 1:proton) and its number density (/cc)\n").split())
        if species == 0:
            proton = False
        else:
            proton = True
        pfreq = c.plasma_frequency(rho/c.CENT**3, proton) / c.KILO
        print('Omega_p = %f kHz' % pfreq)
    else:
        species, vel = map(float, input("Input the plasma species (0:electron 1:proton) and the velocity (km/s)\n").split())
        if species == 0:
            proton = False
        else:
            proton = True
        ene = c.vel2joule(vel*c.KILO, proton)
        ev = c.joule2ev(ene) / c.KILO
        print('Energy = %f keV' % ev)

    print("Quit? 1:Yes")
    cont = int(input())
    if cont==1:
        bool = False
