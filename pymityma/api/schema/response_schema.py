class ResponseSchema:
    success = 1
    error = 0

    def __init__(self, success: int, data):
        self.success = success
        self.data = data
