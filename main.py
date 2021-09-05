from z3 import *
from tools import *
from observedDistr import *
from tqdm import *
import time
from ring6 import *
from localDecomp import *
from spiral import *
from scipy.io import savemat

orbit = np.loadtxt('orbit.txt')
card = 6

unsatLocalDecomp = []
satLocalDecomp = []
satRing = []
unsatRing = []
unsatWeb = []
satWeb = []
satSpiral = []
unsatSpiral = []

print('Ring inflation')
for i in tqdm(orbit, ncols=70):
    state = compatibilityRing6(i)
    if state == sat:
        satRing.append(i)
    elif state == unsat:
        unsatRing.append(i)

print('Locality condition ( cardinality = ', card, ')')
for i in tqdm(satRing, ncols=70):
    state = localDecomp(i, card)
    if state == sat:
        satLocalDecomp.append(i)
    elif state == unsat:
        unsatLocalDecomp.append(i)

print('Spiral inflation')
for i in tqdm(unsatLocalDecomp, ncols=70):
    state = compatibilitySpiral(i)
    if state == sat:
        satSpiral.append(i)
    elif state == unsat:
        unsatSpiral.append(i)

print('unsat ring inflation:', len(unsatRing), '/', len(orbit))
print('Unsat Locality condition:', len(unsatLocalDecomp), '/', len(satRing))
print('unsat spiral inflation:', len(unsatSpiral), '/', len(unsatLocalDecomp))

# savemat('nonLocalNS.mat', {'nonLocalNS': unsatSpiral})
