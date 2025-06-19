import hashlib
import os
import csv

class HashExporter:
    def __init__(self, output_csv):
        self.output_csv = output_csv

    def hash_file(self, filepath):
        with open(filepath, 'rb') as f:
            data = f.read()
            md5 = hashlib.md5(data).hexdigest()
            sha256 = hashlib.sha256(data).hexdigest()
        return md5, sha256

    def export_hashes(self, folder_path):
        with open(self.output_csv, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Filename', 'MD5', 'SHA256'])  # header

            for root, _, files in os.walk(folder_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    try:
                        md5, sha256 = self.hash_file(file_path)
                        writer.writerow([file_path, md5, sha256])
                    except Exception as e:
                        print(f"Error hashing {file_path}: {e}")
