import os
import subprocess
import hashlib

class AndroidImageCollector:
    def __init__(self):
        self.device_id = None
        self.collection_folder = None

    # Get our connected device
    def get_connected_device(self):
        result = subprocess.run(['adb', 'devices'], capture_output=True, text=True)
        lines = result.stdout.strip().split('\n')[1:]
        devices = [line.split()[0] for line in lines if '\tdevice' in line]

        if not devices:
            raise RuntimeError("No connected devices found.")

        self.device_id = devices[0]
        print(f"Connected device: {self.device_id}")

    #Create our investigation folder
    def create_collection_folder(self):
        self.collection_folder = f"collection_{self.device_id}"
        os.makedirs(self.collection_folder, exist_ok=True)

    def pull_folder(self, remote_path: str, local_subfolder: str):
        local_path = os.path.join(self.collection_folder, local_subfolder)
        print(f"Pulling '{remote_path}' to '{local_path}' ...")
        result = subprocess.run(['adb', 'pull', remote_path, local_path], capture_output=True, text=True)
        if result.returncode != 0:
            print(f"Error pulling {remote_path}:")
            print(result.stderr)
            return False
        print(f"Successfully pulled {remote_path}")
        return True

    def collect_images(self):
        # Pull Screenshots and Camera folders
        if not self.pull_folder('/storage/self/primary/DCIM/Screenshots', 'Screenshots'):
            print("Failed to pull Screenshots folder.")
        if not self.pull_folder('/storage/self/primary/DCIM/Camera', 'Camera'):
            print("Failed to pull Camera folder.")




    def hash_collected_files(self):
        if not self.collection_folder:
            print("Collection folder not set.")
            return

        print(f"Hashing files in: {self.collection_folder}\n")

        for root, _, files in os.walk(self.collection_folder):
            for file in files:
                file_path = os.path.join(root, file)

                try:
                    with open(file_path, 'rb') as f:
                        data = f.read()

                        md5_hash = hashlib.md5(data).hexdigest()
                        sha256_hash = hashlib.sha256(data).hexdigest()

                        print(f"File: {file_path}")
                        print(f"  MD5:    {md5_hash}")
                        print(f"  SHA256: {sha256_hash}\n")

                except Exception as e:
                    print(f"Error reading {file_path}: {e}")

    def run(self):
        try:
            self.get_connected_device()
            self.create_collection_folder()
            self.collect_images()
            print("Image collection complete.")
            self.hash_collected_files()
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    collector = AndroidImageCollector()
    collector.run()
