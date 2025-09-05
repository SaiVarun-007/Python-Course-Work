class Status:
    def __init__(self,caption):
        self.caption=caption
    def display(self):
        print(f"'{self.caption}' is added")
        
class Status1V1(Status):
    def __init__(self,url,caption):
        super().__init__(caption)
        
    def displat(self):
        super().display()
        print(f"'{self.url}' is uploaded")