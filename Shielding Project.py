import math
def primary_barrier():
    total_wl = 0
    try:
        energy = float(input("Input energy in MV: "))

        # Ask for number of workloads
        num_workloads = int(input("Input # of workloads from that energy: "))

        for i in range(num_workloads):
            print('-------------------------')
            workload_type = input("IMRT or conventional? (Type 'IMRT' or 'C'): ")
            wl = float(input(f"Enter workload #{i + 1} (Gy/wk):"))
            usage = float(input("Input usage factor: "))

            if workload_type.lower() == 'imrt':
                c_i = float(input("Input correction factor: "))
                result = c_i * wl * usage

            elif workload_type.lower() == 'c':
                result = wl * usage

            total_wl += result

        print('----------------------')
        occupancy = float(input("Input occupancy factor:  "))
        design_goal = float(input("Enter your design goal (mSv/wk):  "))
        d_primary = float(input("Enter distance from iso to distal surface (inches):  "))
        print("The 0.3m and 1m are already considered in the code")
        print('------------------------------------------------------')
        TVL1 = float(input(f"Enter TVL_1 (cm) for {energy} MV:  "))
        TVLe = float(input(f"Enter TVL_e (cm) for {energy} MV:  "))

        d_primary = (d_primary * 2.54) / 100 + 0.3 + 1  # Distance from target to 0.3m beyond distal wall in meters

        B = (design_goal*10**-3 * (d_primary**2)) / (total_wl * occupancy)  # d_primary in cm
        # Calculates number of TVLs
        n = -math.log10(B)
        # Calculates required thickness for the primary barrier
        thickness = TVL1 + (n-1) * TVLe

    except ValueError:
        print("Invalid input. Please enter numeric values only.")
        return None, None

    print('---------------------------')
    print(f"Total workload: {total_wl} Gy/wk")
    print(f"d_primary: {d_primary} m")
    print('---------------------------')
    print(f"Transmission factor: {B}")
    print(f"Number of TVLs: {n}")
    print(f"Thickness required: {thickness} cm")

primary_barrier()