'''
This script is made to plot the number of relativistic degrees of freedom in the early Universe

Unless otherwise stated, the units of temperature are in Giga-electronVolts (GeV) and
    the units of mass are (GeV / c2)
'''
import numpy as np

import matplotlib.pyplot as plt


plt.style.use("dstyle")
_ = plt.figure()



T_QCD = 0.3
T_electronpositron = 5.11e-4

class Higgs_boson:

    def __init__(self):
        self.mass = 125.1
        self.DoF_internal = 1 # spin 0


    def DoF_energydensity(self, temp):
        '''
        Calculate the effective degrees of freedom contribution to energy density

        Args:
            temp (float) : temperature in GeV
        Return:
            (float) : effective degrees of freedom
        '''

        if temp < self.mass:
            return 0.
        else:
            return self.DoF_internal * 1.


    def DoF_entropydensity(self, temp):
        ''' 
        Calculate the effective degrees of freedom contribution to entropy density

        Args:
            temp (float) : temperature in GeV
        Return:
            (float) : effective degrees of freedom
        '''

        if temp < self.mass:
            return 0.
        else:
            return self.DoF_internal * 1.


class Z_boson:

    def __init__(self):
        self.mass = 91.2
        self.DoF_internal = 3 # spin 1 (3 states bc not massless)


    def DoF_energydensity(self, temp):
        ''' 
        Calculate the effective degrees of freedom contribution to energy density

        Args:
            temp (float) : temperature in GeV
        Return:
            (float) : effective degrees of freedom
        '''

        if temp < self.mass:
            return 0.
        else:
            return self.DoF_internal * 1.


    def DoF_entropydensity(self, temp):
        ''' 
        Calculate the effective degrees of freedom contribution to entropy density

        Args:
            temp (float) : temperature in GeV
        Return:
            (float) : effective degrees of freedom
        '''

        if temp < self.mass:
            return 0.
        else:
            return self.DoF_internal * 1.


class W_boson:

    def __init__(self):
        self.mass = 80.4
        self.DoF_internal = 3 * 2 # spin 1 (3 states bc not massless), particle + antiparticle


    def DoF_energydensity(self, temp):
        ''' 
        Calculate the effective degrees of freedom contribution to energy density

        Args:
            temp (float) : temperature in GeV
        Return:
            (float) : effective degrees of freedom
        '''

        if temp < self.mass:
            return 0.
        else:
            return self.DoF_internal * 1.


    def DoF_entropydensity(self, temp):
        ''' 
        Calculate the effective degrees of freedom contribution to entropy density

        Args:
            temp (float) : temperature in GeV
        Return:
            (float) : effective degrees of freedom
        '''

        if temp < self.mass:
            return 0.
        else:
            return self.DoF_internal * 1.


class Photon_boson:

    def __init__(self):
        self.mass = 0.
        self.DoF_internal = 2 # spin 1 (polarization)


    def DoF_energydensity(self, temp):
        ''' 
        Calculate the effective degrees of freedom contribution to energy density

        Args:
            temp (float) : temperature in GeV
        Return:
            (float) : effective degrees of freedom
        '''

        if temp < self.mass:
            return 0.
        else:
            return self.DoF_internal * 1.


    def DoF_entropydensity(self, temp):
        ''' 
        Calculate the effective degrees of freedom contribution to entropy density

        Args:
            temp (float) : temperature in GeV
        Return:
            (float) : effective degrees of freedom
        '''

        if temp < self.mass:
            return 0.
        else:
            return self.DoF_internal * 1.


class Gluon_boson:

    def __init__(self):
        self.mass = 0.
        self.DoF_internal = 8 * 2 # colors, spin 1


    def DoF_energydensity(self, temp):
        ''' 
        Calculate the effective degrees of freedom contribution to energy density

        Args:
            temp (float) : temperature in GeV
        Return:
            (float) : effective degrees of freedom
        '''

        if temp < self.mass:
            return 0.
        else:
            return self.DoF_internal * 1.


    def DoF_entropydensity(self, temp):
        ''' 
        Calculate the effective degrees of freedom contribution to entropy density

        Args:
            temp (float) : temperature in GeV
        Return:
            (float) : effective degrees of freedom
        '''

        if temp < self.mass:
            return 0.
        else:
            return self.DoF_internal * 1.



class Top_quark:

    def __init__(self):
        self.mass = 137.
        self.DoF_internal = 2 * 3 * 2 #  spin 1/2, 3 colors, particle + antiparticle


    def DoF_energydensity(self, temp):
        ''' 
        Calculate the effective degrees of freedom contribution to energy density

        Args:
            temp (float) : temperature in GeV
        Return:
            (float) : effective degrees of freedom
        '''

        if temp < self.mass:
            return 0.
        else:
            return self.DoF_internal * 7. / 8.


    def DoF_entropydensity(self, temp):
        ''' 
        Calculate the effective degrees of freedom contribution to entropy density

        Args:
            temp (float) : temperature in GeV
        Return:
            (float) : effective degrees of freedom
        '''

        if temp < self.mass:
            return 0.
        else:
            return self.DoF_internal * 7. / 8.

class Bottom_quark:

    def __init__(self):
        self.mass = 4.18
        self.DoF_internal = 2 * 3 * 2 #  spin 1/2, 3 colors, particle + antiparticle


    def DoF_energydensity(self, temp):
        ''' 
        Calculate the effective degrees of freedom contribution to energy density

        Args:
            temp (float) : temperature in GeV
        Return:
            (float) : effective degrees of freedom
        '''

        if temp < self.mass:
            return 0.
        else:
            return self.DoF_internal * 7. / 8.


    def DoF_entropydensity(self, temp):
        ''' 
        Calculate the effective degrees of freedom contribution to entropy density

        Args:
            temp (float) : temperature in GeV
        Return:
            (float) : effective degrees of freedom
        '''

        if temp < self.mass:
            return 0.
        else:
            return self.DoF_internal * 7. / 8.



class Charm_quark:

    def __init__(self):
        self.mass = 1.27
        self.DoF_internal = 2 * 3 * 2 #  spin 1/2, 3 colors, particle + antiparticle


    def DoF_energydensity(self, temp):
        ''' 
        Calculate the effective degrees of freedom contribution to energy density

        Args:
            temp (float) : temperature in GeV
        Return:
            (float) : effective degrees of freedom
        '''

        if temp < self.mass:
            return 0.
        else:
            return self.DoF_internal * 7. / 8.


    def DoF_entropydensity(self, temp):
        ''' 
        Calculate the effective degrees of freedom contribution to entropy density

        Args:
            temp (float) : temperature in GeV
        Return:
            (float) : effective degrees of freedom
        '''

        if temp < self.mass:
            return 0.
        else:
            return self.DoF_internal * 7. / 8.


class Strange_quark:

    def __init__(self):
        self.mass = 0.10
        self.DoF_internal = 2 * 3 * 2 #  spin 1/2, 3 colors, particle + antiparticle


    def DoF_energydensity(self, temp):
        ''' 
        Calculate the effective degrees of freedom contribution to energy density

        Args:
            temp (float) : temperature in GeV
        Return:
            (float) : effective degrees of freedom
        '''

        if temp < self.mass:
            return 0.
        else:
            return self.DoF_internal * 7. / 8.


    def DoF_entropydensity(self, temp):
        ''' 
        Calculate the effective degrees of freedom contribution to entropy density

        Args:
            temp (float) : temperature in GeV
        Return:
            (float) : effective degrees of freedom
        '''

        if temp < self.mass:
            return 0.
        else:
            return self.DoF_internal * 7. / 8.


class Up_quark:

    def __init__(self):
        self.mass = 3.e-3
        self.DoF_internal = 2 * 3 * 2 #  spin 1/2, 3 colors, particle + antiparticle


    def DoF_energydensity(self, temp):
        ''' 
        Calculate the effective degrees of freedom contribution to energy density

        Args:
            temp (float) : temperature in GeV
        Return:
            (float) : effective degrees of freedom
        '''

        if temp < self.mass:
            return 0.
        else:
            return self.DoF_internal * 7. / 8.


    def DoF_entropydensity(self, temp):
        ''' 
        Calculate the effective degrees of freedom contribution to entropy density

        Args:
            temp (float) : temperature in GeV
        Return:
            (float) : effective degrees of freedom
        '''

        if temp < self.mass:
            return 0.
        else:
            return self.DoF_internal * 7. / 8.


class Down_quark:

    def __init__(self):
        self.mass = 5.e-3
        self.DoF_internal = 2 * 3 * 2 #  spin 1/2, 3 colors, particle + antiparticle


    def DoF_energydensity(self, temp):
        ''' 
        Calculate the effective degrees of freedom contribution to energy density

        Args:
            temp (float) : temperature in GeV
        Return:
            (float) : effective degrees of freedom
        '''

        if temp < self.mass:
            return 0.
        else:
            return self.DoF_internal * 7. / 8.


    def DoF_entropydensity(self, temp):
        ''' 
        Calculate the effective degrees of freedom contribution to entropy density

        Args:
            temp (float) : temperature in GeV
        Return:
            (float) : effective degrees of freedom
        '''

        if temp < self.mass:
            return 0.
        else:
            return self.DoF_internal * 7. / 8.



class Tau_lepton:

    def __init__(self):
        self.mass = 1.78
        self.DoF_internal = 2  * 2 #  spin 1/2, particle + antiparticle


    def DoF_energydensity(self, temp):
        ''' 
        Calculate the effective degrees of freedom contribution to energy density

        Args:
            temp (float) : temperature in GeV
        Return:
            (float) : effective degrees of freedom
        '''

        if temp < self.mass:
            return 0.
        else:
            return self.DoF_internal * 7. / 8.


    def DoF_entropydensity(self, temp):
        ''' 
        Calculate the effective degrees of freedom contribution to entropy density

        Args:
            temp (float) : temperature in GeV
        Return:
            (float) : effective degrees of freedom
        '''

        if temp < self.mass:
            return 0.
        else:
            return self.DoF_internal * 7. / 8.



class Muon_lepton:

    def __init__(self):
        self.mass = 0.106
        self.DoF_internal = 2  * 2 #  spin 1/2, particle + antiparticle


    def DoF_energydensity(self, temp):
        ''' 
        Calculate the effective degrees of freedom contribution to energy density

        Args:
            temp (float) : temperature in GeV
        Return:
            (float) : effective degrees of freedom
        '''

        if temp < self.mass:
            return 0.
        else:
            return self.DoF_internal * 7. / 8.


    def DoF_entropydensity(self, temp):
        ''' 
        Calculate the effective degrees of freedom contribution to entropy density

        Args:
            temp (float) : temperature in GeV
        Return:
            (float) : effective degrees of freedom
        '''

        if temp < self.mass:
            return 0.
        else:
            return self.DoF_internal * 7. / 8.


class Electron_lepton:

    def __init__(self):
        self.mass = 5.11e-4
        self.DoF_internal = 2  * 2 #  spin 1/2, particle + antiparticle


    def DoF_energydensity(self, temp):
        ''' 
        Calculate the effective degrees of freedom contribution to energy density

        Args:
            temp (float) : temperature in GeV
        Return:
            (float) : effective degrees of freedom
        '''

        if temp < self.mass:
            return 0.
        else:
            return self.DoF_internal * 7. / 8.


    def DoF_entropydensity(self, temp):
        ''' 
        Calculate the effective degrees of freedom contribution to entropy density

        Args:
            temp (float) : temperature in GeV
        Return:
            (float) : effective degrees of freedom
        '''

        if temp < self.mass:
            return 0.
        else:
            return self.DoF_internal * 7. / 8.



class Neutrino_leptons: # all three flavors

    def __init__(self):
        self.mass = 1e-10
        self.DoF_internal = 3 * 2 #  3 flavors, particle + antiparticle


    def DoF_energydensity(self, temp):
        ''' 
        Calculate the effective degrees of freedom contribution to energy density

        Args:
            temp (float) : temperature in GeV
        Return:
            (float) : effective degrees of freedom
        '''

        if temp < self.mass:
            return 0.
        elif (self.mass < temp) and (temp < T_electronpositron):
            return self.DoF_internal * (4. / 11.)**(4/3) * 7. / 8.
        else:
            return self.DoF_internal * 7. / 8.


    def DoF_entropydensity(self, temp):
        ''' 
        Calculate the effective degrees of freedom contribution to entropy density

        Args:
            temp (float) : temperature in GeV
        Return:
            (float) : effective degrees of freedom
        '''

        if temp < self.mass:
            return 0.
        elif (self.mass < temp) and (temp < T_electronpositron):
            return self.DoF_internal * (4. / 11.) * 7. / 8.
        else:
            return self.DoF_internal * 7. / 8.



class NeutralPion_hadron: # all three flavors

    def __init__(self):
        self.mass = 0.1350
        self.DoF_internal = 1 # spin 0, boson


    def DoF_energydensity(self, temp):
        ''' 
        Calculate the effective degrees of freedom contribution to energy density

        Args:
            temp (float) : temperature in GeV
        Return:
            (float) : effective degrees of freedom
        '''

        if temp < self.mass:
            return 0.
        else:
            return self.DoF_internal * 1.0


    def DoF_entropydensity(self, temp):
        ''' 
        Calculate the effective degrees of freedom contribution to entropy density

        Args:
            temp (float) : temperature in GeV
        Return:
            (float) : effective degrees of freedom
        '''

        if temp < self.mass:
            return 0.
        else:
            return self.DoF_internal * 1.0


class ChargedPion_hadron: # all three flavors

    def __init__(self):
        self.mass = 0.1396
        self.DoF_internal = 1 * 2 # spin 0, boson, particle + antiparticle


    def DoF_energydensity(self, temp):
        ''' 
        Calculate the effective degrees of freedom contribution to energy density

        Args:
            temp (float) : temperature in GeV
        Return:
            (float) : effective degrees of freedom
        '''

        if temp < self.mass:
            return 0.
        else:
            return self.DoF_internal * 1.0


    def DoF_entropydensity(self, temp):
        ''' 
        Calculate the effective degrees of freedom contribution to entropy density

        Args:
            temp (float) : temperature in GeV
        Return:
            (float) : effective degrees of freedom
        '''

        if temp < self.mass:
            return 0.
        else:
            return self.DoF_internal * 1.0



def eff_DoF_energydensity(temp):
    '''
    Calculate the effective degrees of freedom from all particles in Standard Model

    Args:
        temp (float) : temperature in GeV
    Return:
        (float) : effective degrees of freedom
    '''

    DoF_energydensity = 0.

    topquark = Top_quark()
    DoF_energydensity += topquark.DoF_energydensity(temp)

    higgs = Higgs_boson()
    DoF_energydensity += higgs.DoF_energydensity(temp)

    zboson = Z_boson()
    DoF_energydensity += zboson.DoF_energydensity(temp)

    wboson = W_boson()
    DoF_energydensity += wboson.DoF_energydensity(temp)

    bottomquark = Bottom_quark()
    DoF_energydensity += bottomquark.DoF_energydensity(temp)

    taulepton = Tau_lepton()
    DoF_energydensity += taulepton.DoF_energydensity(temp)

    charmquark = Charm_quark()
    DoF_energydensity += charmquark.DoF_energydensity(temp)


    if temp > T_QCD:
        gluonboson = Gluon_boson()
        DoF_energydensity += gluonboson.DoF_energydensity(temp)

        upquark = Up_quark()
        DoF_energydensity += upquark.DoF_energydensity(temp)

        downquark = Down_quark()
        DoF_energydensity += downquark.DoF_energydensity(temp)

        strangequark = Strange_quark()
        DoF_energydensity += strangequark.DoF_energydensity(temp)

    else:
        neutralpionboson = NeutralPion_hadron()
        DoF_energydensity += neutralpionboson.DoF_energydensity(temp)

        chargedpionboson = ChargedPion_hadron()
        DoF_energydensity += chargedpionboson.DoF_energydensity(temp)


    muonlepton = Muon_lepton()
    DoF_energydensity += muonlepton.DoF_energydensity(temp)

    neutrinoleptons = Neutrino_leptons()
    DoF_energydensity += neutrinoleptons.DoF_energydensity(temp)

    electronlepton = Electron_lepton()
    DoF_energydensity += electronlepton.DoF_energydensity(temp)

    photonboson = Photon_boson()
    DoF_energydensity += photonboson.DoF_energydensity(temp)

    return DoF_energydensity



def eff_DoF_entropydensity(temp):
    '''
    Calculate the effective degrees of freedom from all particles in Standard Model

    Args:
        temp (float) : temperature in GeV
    Return:
        (float) : effective degrees of freedom
    '''

    DoF_entropydensity = 0.

    topquark = Top_quark()
    DoF_entropydensity += topquark.DoF_entropydensity(temp)

    higgs = Higgs_boson()
    DoF_entropydensity += higgs.DoF_entropydensity(temp)

    zboson = Z_boson()
    DoF_entropydensity += zboson.DoF_entropydensity(temp)

    wboson = W_boson()
    DoF_entropydensity += wboson.DoF_entropydensity(temp)

    bottomquark = Bottom_quark()
    DoF_entropydensity += bottomquark.DoF_entropydensity(temp)

    taulepton = Tau_lepton()
    DoF_entropydensity += taulepton.DoF_entropydensity(temp)

    charmquark = Charm_quark()
    DoF_entropydensity += charmquark.DoF_entropydensity(temp)


    if temp > T_QCD:
        gluonboson = Gluon_boson()
        DoF_entropydensity += gluonboson.DoF_entropydensity(temp)

        upquark = Up_quark()
        DoF_entropydensity += upquark.DoF_entropydensity(temp)

        downquark = Down_quark()
        DoF_entropydensity += downquark.DoF_entropydensity(temp)

        strangequark = Strange_quark()
        DoF_entropydensity += strangequark.DoF_entropydensity(temp)

    else:
        neutralpionboson = NeutralPion_hadron()
        DoF_entropydensity += neutralpionboson.DoF_entropydensity(temp)

        chargedpionboson = ChargedPion_hadron()
        DoF_entropydensity += chargedpionboson.DoF_entropydensity(temp)


    muonlepton = Muon_lepton()
    DoF_entropydensity += muonlepton.DoF_entropydensity(temp)

    neutrinoleptons = Neutrino_leptons()
    DoF_entropydensity += neutrinoleptons.DoF_entropydensity(temp)

    electronlepton = Electron_lepton()
    DoF_entropydensity += electronlepton.DoF_entropydensity(temp)

    photonboson = Photon_boson()
    DoF_entropydensity += photonboson.DoF_entropydensity(temp)

    return DoF_entropydensity




T_early = 0.001
eff_DoF_early = eff_DoF_entropydensity(T_early)
print(f"the effective number of degrees of freedom at temps of {T_early:.3e} Gev is g_* =  {eff_DoF_early:.3f}")

ntemps = 100
l_temp_arr = np.linspace(-5, 3, ntemps)


eff_DoF_energydensity_arr = np.zeros(ntemps)
eff_DoF_entropydensity_arr = np.zeros(ntemps)

for k, l_temp in enumerate(l_temp_arr):
    eff_DoF_energydensity_arr[k] = eff_DoF_energydensity(10**(l_temp))
    eff_DoF_entropydensity_arr[k] = eff_DoF_entropydensity(10**(l_temp))




def time(temp):
    '''
    Calculate the time after the Big Bang in seconds given a temperature in GeV

    Args:
        temp (float) : temperature in GeV
    Return:
        (float) : time in secs
    '''

    curr_eff_DOF_energydensity = eff_DoF_energydensity(temp)

    term1 = ((45.**(1./2.)) * (6.852)) / (2. * (np.pi**(3/2)) * (6.709**(1./2.)) * 10**(11./2.))

    term2 = curr_eff_DOF_energydensity**(-1./2.)

    term3 = temp**(-2.)

    return term1 * term2 * term3



time_arr = np.zeros(ntemps)

for k, l_temp in enumerate(l_temp_arr):
    time_arr[k] = time(10**(l_temp))


fig_DoFTemp, ax_DoFTemp = plt.subplots(nrows=1, ncols=1, figsize=(8,8))
fig_TempTime, ax_TempTime = plt.subplots(nrows=1, ncols=1, figsize=(8,8))
fig_DoFTime, ax_DoFTime = plt.subplots(nrows=1, ncols=1, figsize=(8,8))


temp_arr = 10**l_temp_arr
temp_low, temp_hi = 1.e-5, 1.e3
time_low, time_hi = time(temp_hi), time(temp_low)

_ = ax_DoFTemp.plot(temp_arr, eff_DoF_energydensity_arr, ls='-', label=r'$g_{*}$')
_ = ax_DoFTime.plot(time_arr, eff_DoF_energydensity_arr, ls='-', label=r'$g_{*}$')

_ = ax_DoFTemp.plot(temp_arr, eff_DoF_entropydensity_arr, ls='--', label=r"$g_{*,S}$")
_ = ax_DoFTime.plot(time_arr, eff_DoF_entropydensity_arr, ls='--', label=r"$g_{*,S}$")

_ = ax_TempTime.plot(time_arr, temp_arr)

QCD_str = r"$\rm{QCD\ Phase\ Transition}$"
_ = ax_TempTime.axhline(T_QCD, c='k', ls='--')
_ = ax_TempTime.annotate(QCD_str, xy=(5.e-4, 1.2 * T_QCD), fontsize=16)

electronpos_str = r"$e\bar{e}\ \rm{Annihilation}$"
_ = ax_TempTime.axhline(T_electronpositron, c='k', ls='--')
_ = ax_TempTime.annotate(electronpos_str, xy=(1.e-5, 1.2 * T_electronpositron), fontsize=16)

T_EW = 200.
EW_str = r"$\rm{Electroweak\ Phase\ Transition}$"
_ = ax_TempTime.axhline(T_EW, c='k', ls='--')
_ = ax_TempTime.annotate(EW_str, xy=(1.e-9, 1.2 * T_EW), fontsize=16)

T_neutrino = 3.e-3
neutrino_str = r"$\nu\ \rm{Decoupling}$"
_ = ax_TempTime.axhline(T_neutrino, c='k', ls='--')
_ = ax_TempTime.annotate(neutrino_str, xy=(1.e-7, 1.2 * T_neutrino), fontsize=16)

t_neutron = 880.2
neutron_str = r"$\rm{Free\ Neutron\ Lifetime}$"
_ = ax_TempTime.axvline(t_neutron, c='k', ls='--')
_ = ax_TempTime.annotate(neutron_str, xy=(1.2 * t_neutron, 5.e-1), fontsize=16, rotation=270)


for sub_ax in [ax_DoFTemp, ax_DoFTime, ax_TempTime]:
    _ = sub_ax.set_xscale('log')
    _ = sub_ax.set_yscale('log')
    _ = sub_ax.grid(which='both', axis='both', alpha=0.3)


for sub_ax in [ax_DoFTemp, ax_DoFTime]:
    _ = sub_ax.set_ylim(1e0, 2e2)
    _ = sub_ax.set_ylabel(r"$\rm{Count}$")
    _ = sub_ax.legend()

_ = ax_DoFTemp.set_xlim(temp_low, temp_hi)
_ = ax_DoFTime.set_xlim(time_hi, time_low)

_ = ax_TempTime.set_xlim(time_low, time_hi)
_ = ax_TempTime.set_ylim(temp_low, temp_hi)

_ = ax_DoFTemp.set_xlabel(r'$T\ [\rm{GeV}]$')
_ = ax_DoFTime.set_xlabel(r'$t\ [\rm{s}]$')

_ = ax_TempTime.set_xlabel(r'$t\ [\rm{s}]$')
_ = ax_TempTime.set_ylabel(r'$T\ [\rm{GeV}]$')


for subfig in [fig_DoFTemp, fig_DoFTime, fig_TempTime]:
    _ = subfig.tight_layout()


_ = fig_DoFTemp.savefig("eff_DoF.png", dpi=256, bbox_inches="tight")
_ = fig_DoFTime.savefig("eff_DoF_time.png", dpi=256, bbox_inches="tight")
_ = fig_TempTime.savefig("timetemp.png", dpi=256, bbox_inches="tight")


for subfig in [fig_DoFTemp, fig_DoFTime, fig_TempTime]:
    _ = plt.close(subfig)



