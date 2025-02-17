
class Brain:
    def __init__(self):
        self.memory = {}
        self.memory['name'] = 'Yanna'
        self.memory['age'] = 25
        self.memory['location'] = 'Portugal'

        
    def GenerateResponse(self, message):
        response = message
        return response