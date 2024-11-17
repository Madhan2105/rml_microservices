class FileReaderService:
    def __init__(self, file_path, publisher):
        """Initialize Object."""
        self.file_path = file_path
        self.publisher = publisher

    def process_file(self):
        """Read the file and publish task."""
        with open(self.file_path, 'r') as file:
            for line in file:
                line = line.strip()
                if line:
                    self.publisher.publish(line)
                    print(f"Published line: {line}")
