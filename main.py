from math import *

# Mass Defect
c = 3 * pow(10, 8)
n = 1.008665
p = 1.007825
amu_kg = 1.66054 * pow(10, -27)
amu_eV = 931.5 * pow(10, 6)
amu_MeV = 931.5
mol_atom = 6.022 * pow(10, 23)


def Avogradro(mol):
    mol *= 6.022 * pow(10, 23)
    return mol


def amu_to_kg(amu):
    return amu * amu_kg


def E_in_MeV(mass_defect):
    return mass_defect * amu_MeV


def Mass_Defect_Fission(mass_R, mass_P):
    mass_R += n
    mass_P += p
    m = mass_R - mass_P
    m_kg = amu_to_kg(m)
    e = m_kg * pow(c, 2)
    e_per_mole = Avogradro(e)

    print(f"""Mass Defect:
        {m} amu
        {m_kg} kg""")
    print(f"Energy: {e} J")
    print(f"Energy/mole: {e_per_mole} J/mole")
    print("\n")


def Mass_Defect_Decay(proton, atomic_mass, spec_mass):
    neutron = (atomic_mass - proton) * n
    proton *= p
    mass_R = proton + neutron
    if spec_mass == 0:
        mass_P = atomic_mass
    else:
        mass_P = spec_mass
    m = mass_R - mass_P
    m_kg = amu_to_kg(m)
    e = m_kg * pow(c, 2)
    e_MeV = E_in_MeV(m)
    e_per_nucleon = e_MeV / atomic_mass

    print(f"""Mass Defect:
        {m} amu
        {m_kg} kg""")
    print(f"Energy: {e} J")
    print(f"E in Mev: {e_MeV} MeV")
    print(f"Energy/nucleon: {e_per_nucleon} MeV/nucleon")
    print("\n")


def Decay_Law(mass, half_life, spec_mass, time):  # mass must be in grams, half_life and  time must be in days
    k = log(2) / half_life
    g_to_mol = mass / spec_mass
    N_o = g_to_mol * mol_atom
    N_t = N_o * (pow(e, (-k * time)))

    print(f"No: {N_o} atoms")
    print(f"e: {e}")
    print(f"t: {time} days")
    print(f"k: {k}")
    print(f"Nt: {N_t} atoms")
    print("\n")



print("""
[1] Mass Defect Fission
[2] Mass Defect Decay
[3] Decay Law
[4] Fuel Consumption / Carbon Dioxide Emission
""")

while True:

    choice = int(input("choose: "))

    if choice == 1:
        mass_R = float(input("Mass of Reactant: "))
        mass_P = float(input("Mass of Product: "))
        Mass_Defect_Fission(mass_R, mass_P)

    elif choice == 2:
        proton = float(input("Proton: "))
        atomic_mass = float(input("Mass Number: "))
        spec_mass = float(input("Specified Mass: "))
        Mass_Defect_Decay(proton, atomic_mass, spec_mass)

    elif choice == 3:
        mass = float(input("Given Mass (grams): "))
        half_life = float(input("Half Life (days): "))
        spec_mass = float(input("Specified Mass: "))
        time = float(input("Time (days}: "))
        Decay_Law(mass, half_life, spec_mass, time)

    elif choice == 4:
        weight_L = float(input("Weight per Liter (g): "))
        carbon_percent = float(input("Carbon Percentage (%): "))
        oxygen_needed = float(input("oxygen needed to combust this carbon (g): "))
        ave_consumption = float(input("Average Consumption (L/km): "))
        carbon_percent = (carbon_percent / 100) * weight_L
        Sum = carbon_percent + oxygen_needed
        ave_consumption *= Sum
        print(f"The Average Consumption Corresponds to {ave_consumption} g/km")
        print("\n")
