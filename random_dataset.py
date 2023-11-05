import random

def generate_array(size, status):
    if status == "sorted":
        arr = list(range(size))
    elif status == "reversed":
        arr = list(range(size, 0, -1))
    elif status == "random":
        arr = [random.randint(0, size) for _ in range(size)]
    return arr

def generate_dataset():
    sizes = [200, 2000, 20000]
    statuses = ["sorted", "reversed", "random"]
    dataset = []

    for size in sizes:
        for status in statuses:
            arr = generate_array(size, status)
            print(f"Array with size {size} and status {status}: {arr[:10]}... ({len(arr)} elements in total)")
            dataset.append([arr, size, status])
            # create txt file for each dataset
            with open(f"dataset_{size}_{status}.txt", "w") as file:
                for element in arr:
                    file.write(f"{element}\n")
    return dataset