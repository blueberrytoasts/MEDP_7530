import csv
import os

def find_t_secondary(P, T, F, dist, d_sca, filename='secondary_shielding.csv'):
    """
    Calculates required secondary barrier thickness and stores the results in a CSV file.
    """

    wall = input("Which wall? ")
    energy_choice = input("Which energy? (6, 18, or both): ").strip()

    data = {
        'Wall': wall,
        'Energy': energy_choice,
        'P (mSv/wk)': P,
        'T': T,
        'F (cm^2)': F,
        'Distance (m)': dist,
        'Scatter Distance (m)': d_sca,
    }

    thickness = 10.0  # starting value in cm

    if energy_choice in ['6', 'both']:
        print("\n--- 6 MV Inputs ---")
        TVLa = float(input("6 MV Patient Scatter TVL (cm): "))
        W_a = float(input("6 MV Workload (Gy/wk): "))
        a_a = float(input("6 MV Scatter fraction: "))
        TVL1_c = float(input("6 MV Leakage TVL_1 (cm): "))
        TVLe_c = float(input("6 MV Leakage TVL_e (cm): "))
        W_c = float(input("6 MV Leakage Workload (Gy/wk): "))

        data.update({
            '6MV_TVL': TVLa,
            '6MV_Workload': W_a,
            '6MV_Scatter_Frac': a_a,
            '6MV_TVL1_Leak': TVL1_c,
            '6MV_TVLe_Leak': TVLe_c,
            '6MV_Leak_Workload': W_c,
        })
    else:
        data.update({
            '6MV_TVL': '',
            '6MV_Workload': '',
            '6MV_Scatter_Frac': '',
            '6MV_TVL1_Leak': '',
            '6MV_TVLe_Leak': '',
            '6MV_Leak_Workload': '',
        })

    if energy_choice in ['18', 'both']:
        print("\n--- 18 MV Inputs ---")
        TVLb = float(input("18 MV Patient Scatter TVL (cm): "))
        W_b = float(input("18 MV Workload (Gy/wk): "))
        a_b = float(input("18 MV Scatter fraction: "))
        TVL1_d = float(input("18 MV Leakage TVL_1 (cm): "))
        TVLe_d = float(input("18 MV Leakage TVL_e (cm): "))
        W_d = float(input("18 MV Leakage Workload (Gy/wk): "))

        data.update({
            '18MV_TVL': TVLb,
            '18MV_Workload': W_b,
            '18MV_Scatter_Frac': a_b,
            '18MV_TVL1_Leak': TVL1_d,
            '18MV_TVLe_Leak': TVLe_d,
            '18MV_Leak_Workload': W_d,
        })
    else:
        data.update({
            '18MV_TVL': '',
            '18MV_Workload': '',
            '18MV_Scatter_Frac': '',
            '18MV_TVL1_Leak': '',
            '18MV_TVLe_Leak': '',
            '18MV_Leak_Workload': '',
        })

    while True:
        H_total = 0

        if energy_choice in ['6', 'both']:
            scatter_6MV = 10 ** -(thickness / TVLa) * (W_a * a_a * F) / (dist ** 2 * d_sca ** 2 * 400)
            leak_6MV = 10 ** -(1 + ((thickness - TVL1_c) / TVLe_c)) * (W_c * 1e-3) / dist ** 2
            H_total += scatter_6MV + leak_6MV

        if energy_choice in ['18', 'both']:
            scatter_18MV = 10 ** -(thickness / TVLb) * (W_b * a_b * F) / (dist ** 2 * d_sca ** 2 * 400)
            leak_18MV = 10 ** -(1 + ((thickness - TVL1_d) / TVLe_d)) * (W_d * 1e-3) / dist ** 2
            H_total += scatter_18MV + leak_18MV

        H_total *= 1e3  # convert to mSv/wk

        if P / T > H_total:
            break
        thickness += 0.1

    data['Required_Thickness_cm'] = round(thickness, 1)

    # Write to CSV
    file_exists = os.path.isfile(filename)
    with open(filename, mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=data.keys())
        if not file_exists:
            writer.writeheader()
        writer.writerow(data)

    print(f"\nShielding thickness for wall '{wall}' recorded: {thickness:.1f} cm")

#  Wall A
find_t_secondary(0.02, 0.025, 1600, 7.3260137, 1, filename='secondary_shielding.csv')


# Wall C
# find_t_secondary(0.1, 0.5, 1600, 7.158, 1, filename='secondary_shielding.csv')