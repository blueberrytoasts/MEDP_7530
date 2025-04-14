import math

def B1(thickness, TVL): # Calculates B factor using only 1 TVL. Important for PATIENT SCATTER
    '''
    param thickness: thickness of barrier (cm)
    param TVL: TVL (cm) where it is ALWAYS dependent on energy. Can also depend on the angle too
    '''
    B = 10**-(thickness/TVL)
    return B

def B2(thickness, TVL1, TVLe): # Calculates B factor using 2 TVLs. Important for LEAKAGE
    '''
    param thickness: thickness of barrier (cm)
    param TVL1: first TVL (cm)
    param TVLe: equilibrium TVL (cm)
    '''
    B = 10**-(1+((thickness-TVL1)/TVLe))
    return B

def H_ps_unshielded(W, d_secondary, d_scatter, a, F): # Calculates unshielded equivalent dose for PATIENT SCATTER
    '''
    param W: workload in a typical week (Gy/wk)
    param d_secondary: distance from isocenter to the point of interest (cm). Includes the 0.3 m
    param d_scatter: distance from target to isocenter. Usually 1 m
    param a: scatter fraction dependent on angle (deg) and beam energy (MV)
    param F: field size in cm^2
    '''
    H_ps_uns = (W * a * F) / (d_secondary**2 * d_scatter**2 * 400) * 10**3
    return H_ps_uns # (mSv/wk)


def H_leak_unshielded(W_L, d_leakage): # Calculates UNSHIELDED equivalent dose for LEAKAGE
    '''
    param W_L: leakage workload (Gy/wk)
    param d_leakage: distance from source of leakage to point of protection (cm)
    '''
    H_leak_uns = ((W_L*10**-3) / d_leakage**2) * 10**3 # 10**-3 is the included barriers from the head and 10**3 converts Sv to mSv
    return H_leak_uns # (mSv/wk)


def find_t_secondary(P, T, F):
    thickness = 10  # cm
    H_total_shielded = 100000
    # Add QA energy
    while (P/T) < H_total_shielded:
        H_total_shielded = ((10**-(thickness/TVLa) * (W_a * a_a * F) / (d_sec**2 * d_sca**2 * 400) * 10**3) +
                            (10**-(thickness/TVLb) * (W_b * a_b * F) / (d_sec**2 * d_sca**2 * 400) * 10**3)) + \
            (10**-(1+((thickness-TVL1_c)/TVLe_c)) * (W * 10**-3) / (d_leak**2) * 10**3) + \
            (10**-(1+((thickness-TVL1_d)/TVLe_d)) * (W * 10**-3) / (d_leak**2) * 10**3)
            
        