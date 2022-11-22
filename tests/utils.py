from images.models import Image


def create_image(name, url, slug, description, owner):
    image = Image(name=name, slug=slug, description=description, owner=owner, url=url)
    image.full_clean()
    image.save()
    return image


def delete_image(image):
    image.delete()


def update_image(image, data):
    has_updated = False
    for field in data:
        if getattr(image, field) != data[field]:
            has_updated = True
            setattr(image, field, data[field])

    if has_updated:
        image.full_clean()
        image.save()

    return image
