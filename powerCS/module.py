def start_consuption_timer():
    return f"Starting...!"

def publish_consumption_report():
    import platform_discovery
    from CPU import CPUsage

    if platform_discovery.identify_os() == "Win":
        return
    elif platform_discovery.identify_os() == "Mac":
       print(CPUsage.get_average_cpu_usage(10))
    return "Report"

print(start_consuption_timer())
print(publish_consumption_report())