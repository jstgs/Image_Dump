from AndroidImageCollector import AndroidImageCollector
from HashExporter import HashExporter

if __name__ == "__main__":
    collector = AndroidImageCollector()
    collector.run()

    exporter = HashExporter(output_csv=f"{collector.collection_folder}/hashes.csv")
    exporter.export_hashes(collector.collection_folder)