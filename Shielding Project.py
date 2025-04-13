import math
from fractions import Fraction


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

    except ValueError:
        print("Invalid input. Please enter numeric values only.")
        return None, None

    print('---------------------------')
    print(f"Total workload: {total_wl}")
    return energy, occupancy


primary_barrier()