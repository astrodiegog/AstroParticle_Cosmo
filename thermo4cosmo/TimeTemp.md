# Time and Temperature

We can solve the second Friedmann equation and use the temperature-entropy degrees of freedom-scale factor relationship to find a relationship between the time since Big Bang and temperature.

In a radiation-dominated Universe where the spatial curvature is not important, the Friedmann equation reads

$$
H^2 = \left(\frac{1}{a} \frac{\textrm{d}a}{\textrm{d}t} \right)^{1/2} = \frac{8 \pi G}{3} \rho = \frac{8 \pi G}{3} \frac{\pi^2 g_{\*}(T) T^4}{30}
$$


We also know that the entropy density is related to the temperature of the Universe as 

$$
T = \left( \frac{45 s}{2 \pi^2 g_{\*,S}} right)^{1/3} \frac{1}{a} = \left( \frac{45 s}{2 \pi^2 g_{\*}} right)^{1/3} \frac{1}{a}
$$

where in the last line, we assume that the number of degrees of freedom in energy density and entropy are quite similar.

We look at the relationship of scale factor and temperature

$$
\frac{1}{a} \frac{\textrm{d}a}{\textrm{d}t}  = \left(\frac{8 \pi^3 G}{90} \right)^{1/2} g_{\*}^{1/2}(T) T^2 
$$

Plugging in the temperature relationship from the entropy density we find

$$
\frac{1}{a} \frac{\textrm{d}a}{\textrm{d}t}  = \left(\frac{8 \pi^3 G}{90} \right)^{1/2} g_{\*}^{1/2}(T) \left(\left( \frac{45 s}{2 \pi^2 g_{\*}(T)} right)^{1/3} \frac{1}{a} \right)^2 =  \left(\frac{8 \pi^3 G}{90} \right)^{1/2} g_{\*}^{1/2}(T) \left( \frac{45 s}{2 \pi^2 g_{\*}(T)} right)^{2/3} a^{-2}
$$

Focusing just on the scale factor we find

$$
a \textrm{d}a = \left(\frac{8 \pi^3 G}{90} \right)^{1/2}  \left( \frac{45}{2 \pi^2} right)^{2/3} s^{2/3} g_{\*}^{1/2 - 2/3}(T) \textrm{d}t
$$

Integrating from $a=0, t=0$ up to $a=a, t=t$ we find (assuming $g_{\*}$ is subdominant)

$$
\frac{1}{2} a^{2} = \left(\frac{8 \pi^3 G}{90} \right)^{1/2}  \left( \frac{45}{2 \pi^2} right)^{2/3} s^{2/3} g_{\*}^{-1/6}(T) t
$$

Solving for the scale factor as a function of time, we find

$$
a(t) = \left(2  \right)^{1/2} \left(\frac{8 \pi^3 G}{90} \right)^{1/4}  \left( \frac{45}{2 \pi^2} right)^{1/3} s^{1/3} g_{\*}^{-1/12}(T) t^{1/2}
$$

Plugging into the initial entropy density and temperature relationship, we find

$$
T = \left( \frac{45 s}{2 \pi^2 g_{\*}} right)^{-1/3} \left( 2 \right)^{-1/2} \left(\frac{8 \pi^3 G}{90} \right)^{-1/4}  \left( \frac{45}{2 \pi^2} right)^{-1/3} s^{-1/3} g_{\*}^{1/12}(T) t^{-1/2} = \left( 2 \right)^{-1/2} \left(\frac{4 \pi^3 G}{45} \right)^{-1/4} g_{\*}^{1/12 - 1/3}(T) t^{-1/2}
$$

Simplifying, we find 

$$
T = \left( 4 \right)^{-1/4} \left(\frac{4 \pi^3 G}{45} \right)^{-1/4} g_{\*}^{- 1/4}(T) t^{-1/2} = \left( 16 \right)^{-1/4} \left(\frac{\pi^3 G}{45} \right)^{-1/4} g_{\*}^{- 1/4}(T) t^{-1/2}
$$

such that

$$
T = \left( \frac{1}{2} \right) \left(\frac{45}{\pi^3 G} \right)^{1/4} g_{\*}^{- 1/4}(T) t^{-1/2} = \frac{45^{1/4}}{2 \pi^{3/4}} G^{-1/4} g_{\*}^{- 1/4}(T) t^{-1/2}
$$


We can solve for the expression of time as a function of temperature

$$
t = \frac{45^{1/2}}{2 \pi^{3/2}} G^{-1/2} g_{\*}^{- 1/2}(T) T^{-2}
$$

In natural units ($\hbar = c = k_B = 1$), we can express Newton's gravitational constant as

$$
G = 6.709 \times 10^{-39}\ \textrm{GeV}^{-2}
$$

$$
t = \frac{45^{1/2}}{2 \pi^{3/2}} g_{\*}^{- 1/2}(T) \left(6.709 \times 10^{-39}\ \textrm{GeV} ^{-2} \right)^{-1/2} T^{-2} = \frac{45^{1/2}}{2 \pi^{3/2}} \left(6.709 \times 10^{-39} \right)^{-1/2} g_{\*}^{- 1/2}(T)\ \textrm{GeV} T^{-2}
$$

Measuring the temperature in GeV we find

$$
t = \frac{45^{1/2}}{2 \pi^{3/2}} \left(6.709 \times 10^{-39} \right)^{-1/2} g_{\*}^{- 1/2}(T) \left(\frac{\textrm{GeV}}{T} \right)^{-2} \textrm{GeV}^{-1}
$$

In natural units, we can relate the energy and time with the reduced Planck's constant $\hbar = 6.582 \times 10^{-25}\ \textrm{GeV}\ \textrm{s} \rightarrow \textrm{GeV} = \hbar /(6.852) \times 10^{25}\ \textrm{s}^{-1} = 1 /(6.852) \times 10^{25}\ \textrm{s}^{-1}$

$$
t = \frac{45^{1/2}}{2 \pi^{3/2}} \left(6.709 \times 10^{-39} \right)^{-1/2} g_{\*}^{- 1/2}(T) \left(\frac{\textrm{GeV}}{T} \right)^{-2} \left(1 /(6.852) \times 10^{25}\ \textrm{s}^{-1} \right)^{-1}  = \frac{45^{1/2}}{2 \pi^{3/2}} \left(6.709 \times 10^{-39} \right)^{-1/2} \left(6.852 \times 10^{-25} \right)  g_{\*}^{- 1/2}(T) \left(\frac{\textrm{GeV}}{T} \right)^{-2} \ \textrm{s}
$$

Simplifying a bit...

$$
t = \frac{45^{1/2} 10^{39/2} (6.852)  }{2 \pi^{3/2} (6.709)^{1/2} 10^{25}}  g_{\*}^{- 1/2}(T) \left(\frac{\textrm{GeV}}{T} \right)^{-2} \ \textrm{s}
$$

and a bit more...

$$
t = \frac{45^{1/2} (6.852)  }{2 \pi^{3/2} (6.709)^{1/2} 10^{11/2}}  g_{\*}^{- 1/2}(T) \left(\frac{\textrm{GeV}}{T} \right)^{-2} \ \textrm{s}
$$


Inverting for the temperature as a function of time

$$
T = \left(\frac{45^{1/2} (6.852)  }{2 \pi^{3/2} (6.709)^{1/2} 10^{11/2}}\right)^{1/2}  g_{\*}^{- 1/4}(T)  \left( \frac{t}{\textrm{s}}\right)^{-1/2} \ \textrm{GeV}
$$



