class App:
    def __init__(self, env):
        self.__env = env

    def read_config(self):
        DatabaseConfig.filename = os.path.join(self.__env, 'database.json')
    
    def configure_services(self):
        services = [
            OCRService(),
            ClassificationService(),
            FeedbackService()
        ]
        for service in services:
            service.run()

    def update_config(self) -> None:
        """
        Method to update configuration on the fly
        """

    def run():
        pass

if __name__ == '__main__':
    app = App(os.getenviron('ENVIRONMENT'))
    app.read_config()
    app.run()
