from dataclasses import dataclass

@dataclass
class File:
    id: int
    name: str
    categories: list[str]
    parent: int
    size: int


"""
Task 1
"""
def leafFiles(files: list[File]) -> list[str]:
    leaf_nodes = {}
    for file in files:
        if leaf_nodes.get(file.id) != False:
            leaf_nodes[file.id] = file.name
        leaf_nodes[file.parent] = False
    return [name for name in leaf_nodes.values() if name]


"""
Task 2
"""
def kLargestCategories(files: list[File], k: int) -> list[str]:
    category_count = {}
    category_names = []

    for file in files:
        for category in file.categories:
            if category_count.get(category) is None:
                category_names.append(category)
                category_count[category] = 0
            category_count[category] += 1

    return sorted(category_names, key = lambda x: (-category_count[x], x))[:k]


"""
Task 3
"""
def largestFileSize(files: list[File]) -> int:
    
    weights = {}
    children = {}
    roots = []

    for file in files:
        if file.parent == -1:
            roots.append(file.id)

        weights[file.id] = file.size
        if children.get(file.parent) is None:
            children[file.parent] = []

        children[file.parent].append(file.id)

    max_size = 0

    for root in roots:
        curr_size = 0
        stack = [root]
        while stack:
            v = stack.pop()
            curr_size += weights[v]
            
            v_children = children.get(v)

            if v_children is not None:
                for w in children.get(v):
                    stack.append(w)
        max_size = max(curr_size, max_size)
    return max_size



if __name__ == '__main__':
    testFiles = [
        File(1, "Document.txt", ["Documents"], 3, 1024),
        File(2, "Image.jpg", ["Media", "Photos"], 34, 2048),
        File(3, "Folder", ["Folder"], -1, 0),
        File(5, "Spreadsheet.xlsx", ["Documents", "Excel"], 3, 4096),
        File(8, "Backup.zip", ["Backup"], 233, 8192),
        File(13, "Presentation.pptx", ["Documents", "Presentation"], 3, 3072),
        File(21, "Video.mp4", ["Media", "Videos"], 34, 6144),
        File(34, "Folder2", ["Folder"], 3, 0),
        File(55, "Code.py", ["Programming"], -1, 1536),
        File(89, "Audio.mp3", ["Media", "Audio"], 34, 2560),
        File(144, "Spreadsheet2.xlsx", ["Documents", "Excel"], 3, 2048),
        File(233, "Folder3", ["Folder"], -1, 4096),
    ]

    assert sorted(leafFiles(testFiles)) == [
        "Audio.mp3",
        "Backup.zip",
        "Code.py",
        "Document.txt",
        "Image.jpg",
        "Presentation.pptx",
        "Spreadsheet.xlsx",
        "Spreadsheet2.xlsx",
        "Video.mp4"
    ]

    assert kLargestCategories(testFiles, 3) == [
        "Documents", "Folder", "Media"
    ]

    assert largestFileSize(testFiles) == 20992
