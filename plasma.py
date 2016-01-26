from tool import Calc

c = Calc()

print ("Choose the quantity:")
print ("1: Alfven velocity\n2: Cyclotron frequency\n3: Plasma frequency")
quant = input()
quant = int(quant)

if quant == 1:
    rho, mag = map(float, input("Input the plasma number density (/cc) and magnetic field magnitude (nT)\n").split())
    va = c.alfven_velocity(rho, mag*c.NANO)
    print(va)
elif quant == 2:
    mag = map(float, input("Input the magnetic field magnitude (nT)\n").split())
    cfreq = c.cyclotron_frequency(mag*c.NANO)
    print(cfreq)
else:
    species, rho = map(float, input("Input the plasma species (0:electron 1:proton) and its number density (/cc)\n").split())
    pfreq = c.plasma_frequency(species, rho)
    print(pfreq)
