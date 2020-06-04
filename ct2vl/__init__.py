import numpy as np

print("""Please cite: 
Arnaout et al. SARS-CoV-2 Testing: The Limit of Detection Matters—The Case for Benchmarking. bioRxiv, In press.""")

m = -0.0283 # slope of line relating efficiency to cycle no (R2=0.82)
b = m*1.41 + (1.379 + 1) # = rho_0 = efficiency + 1
vL = 100 # viral load at LoD, in copies/mL
CtL = 26.06 # Ct value at LoD (result of BIDMC validation)

def ct2vl(Ct):
	log_v = np.log(vL) + (CtL-1+b/m)*np.log(m*(CtL-1)+b) - (Ct-1+b/m)*np.log(m*(Ct-1)+b)  + Ct-CtL
	return np.exp( log_v )

assert(np.round(ct2vl(CtL)*100)/100==vL)

