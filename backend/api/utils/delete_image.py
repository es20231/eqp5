import os


def delete_image(instance) -> None:
    try:
        os.remove(instance.image.path)
    except (ValueError, FileNotFoundError):
        pass
