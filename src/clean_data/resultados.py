import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class resultados:
    
    def clean(self):
        path= os.chdir(os.path.join(os.getcwd(),"../../"))
        print(path)

if __name__ == '__main__':
    resultados().clean()