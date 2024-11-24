from FileSystemNode import FileSystemNode

class VirtualFileSystem:
    """Simulates a file system with basic directory operations."""
    def __init__(self):
        self.root = FileSystemNode("")

    def find_node(self, path, create_missing=False):
        """Finds or optionally creates a node by path.
        
        Args: 
            path{str}: The path to the parent node directory.
            create_missing{bool}: Boolean to create the child directory. 

        Returns:
            A current directory as a FileSystemNode.
        """
        components = path.split("/")
        current = self.root
        for component in components:
            if not component:  # Skip empty components (e.g., from leading '/')
                continue
            if component not in current.children:
                if create_missing:
                    current.children[component] = FileSystemNode(component)
                else:
                    return None
            current = current.children[component]
        return current

    def create(self, path):
        """Creates a directory at the specified path.
        
        Args: 
            path{str}: The path to the parent node directory.
        """
        if self.find_node(path):
            print(f"Cannot create {path} - already exists")
        else:
            self.find_node(path, create_missing=True)
            print(f"CREATE {path}")

    def move(self, source, destination):
        """Moves a directory from source to destination.
        
        Args: 
            source{str}: The path where the source directory exists.
            destination{str}: The path to move the source directory to.

        Returns:
            void
        """
        if "/" in source:
            src_parent_path, src_name = source.rsplit("/", 1)
            src_parent = self.find_node(src_parent_path)
        else:
            src_parent = self.root
            src_name = source

        dest_node = self.find_node(destination)
        
        if not src_parent or src_name not in src_parent.children:
            print(f"Cannot move {source} - source does not exist")
            return
        if not dest_node:
            print(f"Cannot move {source} - destination does not exist")
            return

        # Move the node
        src_node = src_parent.children.pop(src_name)
        dest_node.children[src_name] = src_node
        print(f"MOVE {source} {destination}")

    def delete(self, path):
        """Deletes the specified directory.
        
        Args: 
            path{str}: The path to the parent node directory.

        Returns:
            void
        """
        if "/" in path:
            parent_path, name = path.rsplit("/", 1)
            parent_node = self.find_node(parent_path)
        else:
            parent_node = self.root
            name = path

        if not parent_node or name not in parent_node.children:
            print(f"Cannot delete {path} - {name} does not exist")
            return

        # Delete the node
        del parent_node.children[name]
        print(f"DELETE {path}")

    def list(self):
        """Lists the current hierarchical direcory structure and its files."""
        print("LIST")
        lines = []
        for node in sorted(self.root.children.values(), key=lambda x: x.name):
            lines.extend(node.list_contents(0))
        print("\n".join(lines))