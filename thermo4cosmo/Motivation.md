# Thermodynamics for Cosmology

The number of internal degrees of freedom for each elementary particle in the Standard Model is described as

| Particle | Flavors | Particle + Antiparticle | Colors | Spin | g |
| ----------- | ----------- | ----------- | ----------- | ----------- | ----------- |
| Quarks ($d,u,s,c,b,t$)  |  6  |  2  |  3  |  2  |  72  |
| Charged Leptons ($e, \mu, \tau$)  |  3  |  2  |  1  |  2  |  12  |
| Neutrinos ($\nu_e, \nu_{\mu}, \nu_{\tau}$)  |  3  |  2  |  1  |  1  |  6  |
| Gluons ($g$)  |  1  |  1  |  8  |  2  |  16  |
| Photon ($\gamma$)  |  1  |  1  |  1  |  2  |  2  |
| $W^{\pm}$  |  1  |  2  |  1  |  3  |  6 |
| $Z$  |  1  |  1  |  1  |  3  |  3 |
| Higgs Boson ($h$)  |  1  |  1  |  1  |  1  |  1 |



The energy density of highly relativistic particles with negligible chemical potential $(T \gg m, \mu)$, can be described with the temperature of the distribution

$$
\rho = 
\begin{cases}
    \frac{\pi^2 g T^4}{30} & (\textrm{Bose-Einstein}) \\
    \frac{7}{8} \frac{\pi^2 g T^4}{30} & (\textrm{Fermi-Dirac})
\end{cases}
$$

where $g$ is the number of internal degrees of freedom of the particles. The energy distribution is dependent on the quantum mechanical structure of the particles at stake - ie whether the [Pauli Exclusion Principle](https://en.wikipedia.org/wiki/Pauli_exclusion_principle) applies - which leads to the statistical description of the momentum phase space occupation function as either Fermi-Dirac distribution or Bose-Einstein distribution.

In cosmology, there is hardly \textit{ever} a situation where one particle species is important. For an ensemble of species, we can describe the energy density with respect to an effective relativistic degrees of freedom $g_*$. More specifically,

$$
\rho = \sum_i \rho_i = \frac{\pi^2 g_{*}(T) T^4}{30}
$$

where we consider the photon temperature $T$ and sum over the $i$-species. That is, 

$$
\rho = \sum_{i=\textrm{bosons}} \rho_{i} + \sum_{i=\textrm{fermions}} \rho_{i} = \sum_{i=\textrm{bosons}} \frac{\pi^2 g_{i} T_{i}^4}{30}  + \sum_{i=\textrm{fermions}} \frac{7}{8} \frac{\pi^2 g_{i} T_{i}^4}{30}
$$

where $T_i$ is the temperature that the species is at. We can describe the energy density with respect to photon temperature

$$
\rho = \frac{\pi^2 T^4}{30} \left(\sum_{i=\textrm{bosons}} g_{i} \left(\frac{T_{i}}{T}\right)^4  + \frac{7}{8} \sum_{i=\textrm{fermions}} g_{i} \left(\frac{T_{i}}{T} \right)^4 \right)
$$

In effect, the effective relativistic degrees of freedom $g_*$ can be described as 

$$
g_{*}(T) =  \left(\sum_{i=\textrm{bosons}} g_{i} \left(\frac{T_{i}}{T}\right)^4  + \frac{7}{8} \sum_{i=\textrm{fermions}} g_{i} \left(\frac{T_{i}}{T} \right)^4 \right)
$$

If all of the particle species are in kinetic equilibrium, then $g_*(T)$ is simply a counting problem: add the bosonic degrees of freedom and seven-eights of the fermionic degrees of freedom.

As the Universe cools the photon temperature lower than that of the mass of a particle species, the annihilation rate of the species does not dominate over the expansion of the Universe. They no longer contribute to the relativistic species bath. There are details related to the phase transition of quantum chromadynamics that describe how, after cooling to a temperature related to the energy scale at which the strong coupling constant (defined perturbatively) is not diverging, gluons and quarks are no longer considered free particles and are "color confined" to hadrons (mesons, baryons, antibaryons). The temperature at which this transition occurs $\Lambda_{\textrm{QCD}}$ dictates the relative amount of species that are formed when the two or more quarks are confined to mesons.


There are further details related to the phase space transition of electromagnetic and weak forces when the bosons $\gamma$, $W^{\pm}$, and $Z$ begin to be described as individual particles. A detailed calculation of $g_{*}(T)$ with both phase transitions requires treatment of the phase space integrals (see effectiveDoF in the bib text). 

When a the photon temperature drops below the mass of a particle species, we say it has decoupled from the photon bath and no longer contributes to $g_{*}(T)$. The one complication is neutrinos because, since they are so light, they remain relativistic even after photon decoupling. Since neutrinos are chargeless particles, they interact with the rest of the thermal bath using the $W^{\pm}$ and $Z$ bosons, not with photons directly. The photon decoupling occurs when the scattering occurs at rates ($\Gamma = n_{e,\nu} \sigma c$) much smaller than that of the Hubble expansion rate ($H$). This occurs at $T_{\nu, \textrm{dc}} \sim 3\ \textrm{MeV}$. Comparing with all of the elementary particles in the Standard Model, the only particle whose mass corresponds to a temperature cooler than $T_{\nu, \textrm{dc}}$ which should still be in the thermal bath is electrons, whose mass is $0.5\ \textrm{MeV}$. In effect, special care is taken at temperatures below $3\ \textrm{MeV}$.

Turning our attention to entropy, we can describe the entropy density as

$$
s = \frac{S}{V} = \frac{\rho + P}{T}
$$

using the relationship between the differential change in internal energy to the change in entropy and volume $\textrm{d}E = T\textrm{S} - P \textrm{d}V$. Just like with energy density, we can describe a particle distribution's entropy density with different particle species as

$$
s = \sum_i s_i = \frac{\pi^2 g_{\*,S}(T) T^3}{30}
$$

where we now have the relativistic number of degrees of freedom in entropy $g_{\*,S}(T)$. For our case of relativistic particles, we can describe the pressure with respect to the energy density as $P = \rho / 3$, so we find

$$
s = \frac{4 \rho}{3 T} = \frac{2 \pi^2 T^3}{45} \left(\sum_{i=\textrm{bosons}} g_{i} \left(\frac{T_{i}}{T}\right)^3  + \frac{7}{8} \sum_{i=\textrm{fermions}} g_{i} \left(\frac{T_{i}}{T} \right)^3 \right)
$$

Applying the conservation of entropy to the expanding Universe, we find

$$
S = sV \propto s a^3 \rightarrow s \propto a^{-3}
$$

Applying our definition of $g_{\*,S}$, we find that the relationship between temperature, number of degrees of freedom in entropy, and entropy density as

$$
g_{\*,S} T^3 \propto a^{-3} \rightarrow T \propto (a g^{1/3}_{\*,S})^{-1}
$$

When the Universe cools to temperatures below that of a particle species, the massive particle is then destroyed more often than it is created. The effect is their abundance being reduced while their energy is transferred into lighter particle species that is in the thermal bath, which is described as "entropy dump".

Applying this concept to neutrinos, we can find the evolution of the temperature of neutrinos after they decoupled from the thermal bath

$$
T_{\nu} a (g_{\*,S}^{nu}(T_{\nu}) )^{1/3} = T_{\nu, \textrm{dc}} a (g_{\*,S}^{\nu}(T_{\nu, \textrm{dc}}) )^{1/3}
$$

We can describe the photon temperature in the same manner. The ratio of the temperature of neutrinos to photons is then 

$$
\frac{T_{\nu}}{T} = \left( \frac{(g_{\*,S}^{\gamma}(T)}{(g_{\*,S}^{gamma}(T_{\nu, \textrm{dc}})} \right)^{1/3}
$$

We find that the temperature ratio of neutrinos to photons after electrons decoupling (electron-positron annihilation) ($T \ll m_{e}$)

$$
\frac{T_{\nu}}{T} = \left(\frac{4}{11} \right)^{1/3}
$$

When describing the two functions of temperature $g_{\*}(T)$ and $g_{\*,S}$, we follow the general equation for kinetic equilibrium

$$
g_{\*}(T) = g_{\*,S}(T) = \left(\sum_{i=\textrm{bosons}} g_{i}  + \frac{7}{8} \sum_{i=\textrm{fermions}} g_{i}  \right)
$$


where we only consider species in the sum whose temperature is below the particle species's mass. For temperatures below the mass of the electron, we modify each to include the scaling of the neutrino to photon temperature.

For temperatures above the QCD transition $T \gg \Lambda_{\textrm{QCD}}$, we treat the quarks and gluons as free particles and in the thermal bath, unless the particle's mass is above the photon temperature. When the Universe cools below this transition temperature, we can treat the surviving quarks primarily as neutral and charged pions ($\pi^{0}, \pi^{+}, \pi^{-}$) as these are the lightest mesons. The lightest baryons are protons, whose rest mass of $938\ \textrm{MeV}$ is greater than the commonly accepted value of $\Lambda_{\textrm{QCD}}$. A more detailed treatment includes other mesons and baryons, like Kaons, as well as the phase space integrals taking into account their masses. To first order (hey I am an astrophysicist!!) the quarks and gluons once $T \ll \Lambda_{\textrm{QCD}}$ are described as the neutral and charged pions.


From the hot dense state of the Big Bang, all Standard Model particles are in kinetic equilibrium. The transitions from this dense state to our present Universe can be modeled by the following annihilation timeline when the expansion rate of the Universe overtakes the rate of particle creation

1. Annihilation of top quarks ($t, \bar{t}$)
2. Annihilation of Higgs Boson ($h$)
3. Annihilation of $Z$ boson
4. Annihilation of $W^{\pm}$ boson
5. Annihilation of bottom quarks ($b, \bar{b}$)
6. Annihilation of charged $\tau^{\pm}$ leptons
7. Annihilation of charm quarks ($c, \bar{c}$)
8. QCD transition, effective annihilation of gluons and remaining quarks to mesons (pions)
9. Annihilation of mesons (pions, $\pi^{0}, \pi^{+}, \pi^{-}$)
10. Annihilation of muons ($\mu^{\pm}$)
11. Neutrino decoupling ($\nu_e, \nu_{\mu}, \nu_{\tau}$)
12. Annihilation of $e^{\pm}$ leptons

To recreate Figure 4.1, we create a 12-piecewise function.

Running `nRelDoF.py` creates three plots: effective degrees of freedom as a function of temperature and time, as well as temperature as a function of time.

Apart from the textbook and lectures, I found the following resources helpful:
1. Dr. Lars Husdal's "On Effective Degrees of Freedom in the Early Universe" article [here](https://www.fuw.edu.pl/~bohdang/wyklady/Cosmology/Husdal_1609.04979.pdf)
2. Section 22 of the Particle Data Group's Review of Particle Physics [here](https://pdg.lbl.gov/2015/download/rpp2014-Chin.Phys.C.38.090001.pdf)
3. Professor Chris Hirata's Cosmology lecture notes over The radiation-dominated era [here](https://hirata10.github.io/ph8803/Lec06_EarlyUniverse.pdf)




