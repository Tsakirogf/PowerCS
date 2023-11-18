import psutil
import time

def get_average_cpu_usage(duration_seconds, interval_seconds=1):
    if duration_seconds < interval_seconds:
        raise ValueError("Duration should be greater than or equal to the interval.")

    num_measurements = duration_seconds // interval_seconds
    total_cpu_percent = 0

    for _ in range(num_measurements):
        # Measure the CPU usage over the interval
        cpu_usage = psutil.cpu_percent(interval=interval_seconds)
        total_cpu_percent += cpu_usage

    # Calculate the average
    average_cpu_percent = total_cpu_percent / num_measurements
    return average_cpu_percent

# Example usage
duration = 10  # Duration over which to measure (in seconds)
interval = 1   # Interval between measurements (in seconds)
average_cpu = get_average_cpu_usage(duration, interval)
print(f"Average CPU usage over {duration} seconds: {average_cpu}%")
