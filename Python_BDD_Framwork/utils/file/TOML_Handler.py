import toml

class TOML_Handler:
    def __init__(self, path):
        self.config = None
        self.path = path

    def load(self):
        with open(self.path, 'r') as file:
            self.config = toml.load(file)
        return self.config

    def save(self):
        with open(self.path, 'w') as file:
            toml.dump(self.config, file)

if __name__ == '__main__':
    t = TOML_Handler('config\config.toml')
    print(t.load())
    t.config['test']['username'] = 'Arindam'
    t.save()