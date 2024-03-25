class Copy:
    def __init__(self, file_path = None) -> None:
        self.file_path = file_path
        self.lines = open(file_path, '+r').readlines()
        self.count = len(self.lines)

    def read_line(self, n):
        self.check_exception(n)
        return self.lines[n]
    
    def prev(self, n):
        self.check_exception(n)
        # AI check if line empty
        pass

    def next(self, n):
        self.check_exception(n)
        # AI check if line empty
        pass

    def check_exception(self, n):
        if n<0 or n>self.count:
            raise Exception(f"Sorry, read_line not valid. n: {n}")