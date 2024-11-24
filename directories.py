from VirtualFileSystem import VirtualFileSystem

# Simulate the input commands
def simulate_filesystem(commands):
    """Organize the files on a computer.
        
    Args: 
        commands{List[str]}: The input commands.
    """
    vfs = VirtualFileSystem()
    for command in commands:
        parts = command.split()
        operation = parts[0]
        if operation == "CREATE":
            vfs.create(parts[1])
        elif operation == "MOVE":
            vfs.move(parts[1], parts[2])
        elif operation == "DELETE":
            vfs.delete(parts[1])
        elif operation == "LIST":
            vfs.list()


# Input commands
commands = [
    "CREATE fruits",
    "CREATE vegetables",
    "CREATE grains",
    "CREATE fruits/apples",
    "CREATE fruits/apples/fuji",
    "LIST",
    "CREATE grains/squash",
    "MOVE grains/squash vegetables",
    "CREATE foods",
    "MOVE grains foods",
    "MOVE fruits foods",
    "MOVE vegetables foods",
    "LIST",
    "DELETE fruits/apples",
    "DELETE foods/fruits/apples",
    "LIST",
]

simulate_filesystem(commands)
