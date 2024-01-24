import os
import subprocess


def get_tracked_files(repo_root_path):
    # Run the git ls-tree command to get a list of tracked files
    tracked_entities_process = subprocess.run(
        ["git", "ls-tree", "-r", "--name-only", "HEAD"],
        cwd=repo_root_path,
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    # Split the output into a list of file paths
    entity_paths = tracked_entities_process.stdout.strip().split('\n')

    # Dictionary to store the file type (file or dir)
    tracked_entity_hash = {}

    for entity_path in entity_paths:
        full_path = os.path.join(repo_root_path, entity_path)
        # Check if the path is a directory or a file
        if os.path.isfile(full_path):
            tracked_entity_hash[entity_path] = 'file'
            # Add each part of the directory structure to the dictionary
            dir_path = os.path.dirname(entity_path)
            while dir_path:
                if dir_path not in tracked_entity_hash:
                    tracked_entity_hash[dir_path] = 'directory'
                dir_path = os.path.dirname(dir_path)

    return tracked_entity_hash

print(get_tracked_files(r"C:\Users\Dan\VSCodeProjects\SentimentAnalyzer"))