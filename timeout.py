from time import sleep


class Timeout:
    def __init__(self, min):
        self.seconds = min*60
        self.text = "Timeout: "

    def start(self):
        for i in range(self.seconds, 0, -1):
            sleep(1)
            text = f"{self.text} {i}"
            print('\b'*len(text), end='', flush=True)
            print(text, end='')
