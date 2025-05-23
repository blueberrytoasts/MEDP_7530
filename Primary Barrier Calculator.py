import math
def primary_barrier():
    total_wl_u = 0
    try:
        energy = float(input("Input energy in MV: "))

        # Ask for number of workloads
        num_workloads = int(input("Input # of workloads from that energy: "))

        for i in range(num_workloads):
            print('-------------------------')
            wl = float(input(f"Enter workload #{i + 1} (Gy/wk):"))
            usage = float(input("Input usage factor: "))
            result = wl * usage
            total_wl_u += result

        print('----------------------')
        occupancy = float(input("Input occupancy factor:  "))
        design_goal = float(input("Enter your design goal (mSv/wk):  "))
        d_primary = float(input("Enter distance from iso to distal surface (inches):  "))
        print("The 0.3m and 1m are already considered in the code")
        print('------------------------------------------------------')
        TVL1 = float(input(f"Enter TVL_1 (cm) for {energy} MV:  "))
        TVLe = float(input(f"Enter TVL_e (cm) for {energy} MV:  "))

        d_primary = ((d_primary * 2.54) / 100) + 0.3 + 1  # Distance from source to 0.3m beyond distal wall in meters

        B = (design_goal*10**-3 * (d_primary**2)) / (total_wl_u * occupancy)  # d_primary in cm
        # Calculates number of TVLs
        n = -math.log10(B)
        # Calculates required thickness for the primary barrier
        thickness = TVL1 + (n-1) * TVLe
        H_unshielded = (design_goal / occupancy) / B
    except ValueError:
        print("Invalid input. Please enter numeric values only.")
        return None, None

    print('---------------------------')
    print(f"Total workload with U: {total_wl_u} Gy/wk")
    print(f"d_primary: {d_primary} m")
    print('---------------------------')
    print(f"Transmission factor: {B}")
    print(f"Number of TVLs: {n}")
    print(f"Thickness required: {thickness} cm")
    print(f"H_unshielded = {H_unshielded}")

primary_barrier()