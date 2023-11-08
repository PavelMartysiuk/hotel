import os


class ModelMethods:
    @staticmethod
    def get_upload_path(self, filename):
        return os.path.join(self.image_path(), filename)
