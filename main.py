from AndroidImageCollector import AndroidImageCollector
from HashExporter import HashExporter
from DownloadsCollection import Downloads

if __name__ == "__main__":
    collector = AndroidImageCollector()
    collector.run()

    exporter = HashExporter(output_csv=f"{collector.collection_folder}/hashes.csv")
    exporter.export_hashes(collector.collection_folder)


    downloads_collector = Downloads(collector.collection_folder)
    downloads_collector.pull_downloads()