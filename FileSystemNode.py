class FileSystemNode:
    """Represents a node in the file system. Can be a directory or type of food."""
    def __init__(self, name):
        self.name = name
        self.children = {}

    def list_contents(self, depth=0):
        """Recursively lists the contents of the directory from the parent directory down to leaf directories.

        Args: 
            depth{int}: the hierarchical level of the directories relative to the parent directory

        Returns:
            A list of strings corresponding to the files for that respective hierarchial directory.
        """
        lines = ["  " * depth + self.name]
        for child in sorted(self.children.values(), key=lambda x: x.name):
            lines.extend(child.list_contents(depth + 1))
        return lines