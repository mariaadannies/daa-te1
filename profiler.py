import time
import psutil
from memory_profiler import profile
from prettytable import PrettyTable
from clustered_binary_is import clustered_binary_insertion_sort
from randomized_quick_sort import randomized_quick_sort
from random_dataset import generate_dataset

@profile
def profile_algorithm_cbis(data):
    start_time = time.time()
    memory_before = psutil.virtual_memory().used

    result = clustered_binary_insertion_sort(data)

    end_time = time.time()
    memory_after = psutil.virtual_memory().used

    execution_time = end_time - start_time
    memory_used = memory_after - memory_before

    return result, execution_time, memory_used

@profile
def profile_algorithm_rqis(data):
    start_time = time.time()
    memory_before = psutil.virtual_memory().used

    result = randomized_quick_sort(data, 0, len(data) - 1)

    end_time = time.time()
    memory_after = psutil.virtual_memory().used

    execution_time = end_time - start_time
    memory_used = memory_after - memory_before

    return result, execution_time, memory_used

dataset = generate_dataset()
sizes = [200, 2000, 20000]
statuses = ["sorted", "reversed", "random"]
table_time = PrettyTable()
table_memory = PrettyTable()
table_time.field_names = ["Size", "Status", "CBIS", "RQIS"]
table_memory.field_names = ["Size", "Status", "CBIS", "RQIS"]

for size in sizes:
    for status in statuses:
        # read dataset from file
        with open("dataset_" + str(size) + "_" + status + ".txt", "r") as file:
            data = file.read().splitlines()
        result_1, time_1, memory_1 = profile_algorithm_cbis(data)
        result_2, time_2, memory_2 = profile_algorithm_rqis(data)

        print("CBIS: Execution time =", time_1, "Memory used =", memory_1, "size = ", size, "status = ", status)
        print("RQIS: Execution time =", time_2, "Memory used =", memory_2, "size = ", size, "status = ", status)
        table_time.add_row([size, status, time_1, time_2])
        table_memory.add_row([size, status, memory_1, memory_2])

with open("output.txt", "w") as file:
    file.write("Execution Time Comparison\n")
    file.write(str(table_time))
    file.write("\n\n\n")
    file.write("Memory Usage Comparison\n")
    file.write(str(table_memory))