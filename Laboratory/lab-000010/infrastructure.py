import os



class WorkingWithFile:
    def __init__(self, fileName: str, content: str) -> None:
        self.fileName = fileName
        self.content = content
        
    def writeFile(self, mode: str) -> None:
        with open(file=self.fileName, mode=mode) as f: 
            f.write(self.content)
            
    def readFile(self, mode: str) -> str:
        with open(file=self.fileName, mode=mode) as f:
            textFull = f.read()
            return textFull
        

class WorkingWithCSV(WorkingWithFile):
    def __init__(self, fileName: str, content: str, format: str) -> None:
        super().__init__(fileName, content)
        self.format = format
        
    def writeFile(self, mode: str) -> None:
        self.fileName += self.format
        return super().writeFile(mode)
    
    def readFile(self, mode: str) -> str:
        self.fileName += self.format
        return super().readFile(mode)
        
        
        
file = WorkingWithCSV(
    fileName="Long",
    content="Nguyen Thanh Long",
    format=".csv"
)

file.writeFile(mode='w')
content = file.readFile(mode='r')
print(content)