import math
import csv

def B1(thickness, TVL):  # Calculates B factor using only 1 TVL. Important for PATIENT SCATTER
    """
    param thickness: thickness of barrier (cm)
    param TVL: TVL (cm) where it is ALWAYS dependent on energy. Can also depend on the angle too
    """
    B = 10 ** -(thickness / TVL)
    return B


def B2(thickness, TVL1, TVLe):  # Calculates B factor using 2 TVLs. Important for LEAKAGE
    """
    param thickness: thickness of barrier (cm)
    param TVL1: first TVL (cm)
    param TVLe: equilibrium TVL (cm)
    """
    B = 10 ** -(1 + ((thickness - TVL1) / TVLe))
    return B


def H_ps_unshielded(W, d_secondary, d_scatter, a, F):
    # Calculates unshielded equivalent dose for PATIENT SCATTER
    """
    param W: workload in a typical week (Gy/wk)
    param d_secondary: distance from isocenter to the point of interest (cm). Includes the 0.3 m
    param d_scatter: distance from target to isocenter. Usually 1 m
    param a: scatter fraction dependent on angle (deg) and beam energy (MV)
    param F: field size in cm^2
    """
    H_ps_uns = (W * a * F) / (d_secondary ** 2 * d_scatter ** 2 * 400) * 10 ** 3
    return H_ps_uns  # (mSv/wk)


def H_leak_unshielded(W_L, d_leakage):
    # Calculates UNSHIELDED equivalent dose for LEAKAGE
    """
    param W_L: leakage workload (Gy/wk)
    param d_leakage: distance from source of leakage to point of protection (cm)
    """
    H_leak_uns = ((W_L * 10 ** -3) / d_leakage ** 2) * 10 ** 3
    # 10**-3 is the included barriers from the head and 10**3 converts Sv to mSv
    return H_leak_uns  # (mSv/wk)


# If we assume uniform gantry rotation, you must find average scatter fraction and d_sec = d_L.
def find_t_secondary(P, T, F, dist, d_sca):
    """
    :param P: design goal (mSv/wk)
    :param T: occupancy factor
    :param F: field size (cm^2)
    :param dist: distance from iso to distal surface of wall. Does not include 0.3 m
    :param d_sca: scatter distance (m) from source to point of scatter. Usually 1 m
    :return:
    """
    wall = input("Which wall?  ")
    print(f"Wall {wall}")
    print("6 MV Patient Scatter")
    TVLa = float(input("Input TVL (cm):  "))
    W_a = float(input("Input workload: "))
    a_a = float(input("Input average scatter fraction:  "))

    print("6 MV Leakage")
    TVL1_c = float(input("Input TVL_1 (cm):  "))
    TVLe_c = float(input("Input TVL_e (cm):  "))
    W_c = float(input("Input workload: "))

    print("18 MV Patient Scatter")
    TVLb = float(input("Input TVL (cm):  "))
    W_b = float(input("Input workload: "))
    a_b = float(input("Input average scatter fraction:  "))

    print("18 MV Leakage")
    TVL1_d = float(input("Input TVL_1 (cm):  "))
    TVLe_d = float(input("Input TVL_e (cm):  "))
    W_d = float(input("Input workload: "))

    d_sec = dist
    d_leak = dist
    thickness = 10  # cm

    # Add QA workload
    flag = True
    while flag:
        H_total_shielded = ((10 ** -(thickness / TVLa) * (W_a * a_a * F) / (d_sec ** 2 * d_sca ** 2 * 400)) +
                            (10 ** -(thickness / TVLb) * (W_b * a_b * F) / (d_sec ** 2 * d_sca ** 2 * 400)) +
                            (10 ** -(1 + ((thickness - TVL1_c) / TVLe_c)) * (W_c * 10 ** -3) / d_leak ** 2) +
                            (10 ** -(1 + ((thickness - TVL1_d) / TVLe_d)) * (W_d * 10 ** -3) / d_leak ** 2)) * 10**3
        if P/T > H_total_shielded:
            flag = False
            print('---------------')
            print(f"Thickness {thickness} cm")

        else:
            thickness += 0.1

    print(f"Design Goal {P} mSv/wk")
    print(f"Occupancy Factor {T}")
    print(f"Field Size {F}")
    print(f"Distance {dist} m")


find_t_secondary(0.1,0.5,1600,7.158,1)