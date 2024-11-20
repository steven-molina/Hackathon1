import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class resultados:
    
    def clean(self,data):
        with open(os.path.join(BASE_DIR, 'SaberPro_Específicas_2016.txt'), 'r') as file:
            data = file.read().replace('¬',',')
        


if __name__ == '__main__':
    resultados().clean()