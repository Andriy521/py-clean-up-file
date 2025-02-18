import os


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename
        self.file = None

    def __enter__(self) -> "CleanUpFile":
        self.file = open(self.filename, "w")
        return self

    def __exit__(self, exc_type: any, exc_val: any, exc_tb: any) -> None:
        self.file.close()
        os.remove(self.filename)
