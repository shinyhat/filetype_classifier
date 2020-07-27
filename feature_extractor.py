
class FeatureExtractor:
    def __init__(self, filename):
        self.filename = filename
        with open(self.filename, 'r') as inFile:
            self.fileContents = inFile.read()
        
        self.features = None
        self.gram2 = dict.fromkeys(range(0,257))
        for key in range(0,257):
            self.gram2[key] = dict(zip(range(0,257), [0]*257))

    def getFeatures(self):
        self.get2gram(self.gram2)
        self.features = self.gram2

    def get2gram(self, gram2):
        fileSize = len(self.fileContents)
        for i in range(0,fileSize-1):
            if ord(self.fileContents[i]) > 256 or ord(self.fileContents[i+1]) > 256:
                continue
            gram2[ord(self.fileContents[i])][ord(self.fileContents[i+1])] += 1 

    def printFile(self):
        print(self.fileContents)
    
    def print2gram(self, gram2):
        for i in range(0,256):
            for j in range(0,256):
                if gram2[i][j] > 0:
                    print('feature['+str(i)+']['+str(j)+']=', gram2[i][j])

    def printFeatures(self):
        self.print2gram(self.gram2)

        
#fe = FeatureExtractor("feature_extractor.py")
fe = FeatureExtractor("../dataset/programming_languages/javascript/source_1/upload-to-cdn.js")
fe.getFeatures()
fe.printFeatures()