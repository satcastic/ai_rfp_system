import json


def estimate_cost(machine_selection):

    with open("data/machine_catalog.json") as f:
        catalog = json.load(f)

    price_lookup = {}

    for category in catalog.values():
        for item in category:
            price_lookup[item["model"]] = item["price"]

    # mapping description → catalog model
    machine_mapping = {
        "6 Axis Robotic Palletizer": "KUKA KR 180 PA",
        "Robotic Palletizer": "ABB IRB 460",
        "Conveyor": "Dematic Modular Conveyor",
        "PLC": "Siemens S7-1500"
    }

    results = {}

    for scenario, machines in machine_selection.items():

        breakdown = {}
        total = 0

        for machine_type in machines.values():

            for machine in machine_type:

                mapped_model = None

                for key in machine_mapping:
                    if key.lower() in machine.lower():
                        mapped_model = machine_mapping[key]
                        break

                if mapped_model:
                    price = price_lookup.get(mapped_model, 0)

                    breakdown[mapped_model] = breakdown.get(mapped_model, 0) + price
                    total += price

        print("\nScenario:", scenario)
        print("Machines:", machines)
        print("Breakdown:", breakdown)
        print("Total:", total)
        results[scenario] = {
            "machine_breakdown": breakdown,
            "total_cost": total
        }

    return results