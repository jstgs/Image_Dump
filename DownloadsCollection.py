import os
import subprocess

class Downloads:
    def __init__(self, collection_folder):
        self.collection_folder = collection_folder
    def pull_downloads(self):
        remote_path = '/storage/self/primary/Download'
        local_path = os.path.join(self.collection_folder, 'Downloads')

        print(f"Pulling Downloads folder from device '{remote_path}' to '{local_path}' ...")
        result = subprocess.run(['adb', 'pull', remote_path, local_path], capture_output=True, text=True)

        if result.returncode != 0:
            print(f"Failed to pull Downloads folder:\n{result.stderr}")
            return False

        print("Successfully pulled Downloads folder.")
        return True
