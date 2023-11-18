import platform

def identify_os():
    os_name = platform.system()

    actions = {
        "Windows": "Win",
        "Linux": "Linux",
        "Darwin": "Mac"
    }

    return actions.get(os_name, f"Running on an unknown system: {os_name}")

print(identify_os())