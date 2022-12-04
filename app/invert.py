from PIL import Image, ImageOps
import io


def invert(picture: bytes, content_type: str) -> bytes | None:
    picture = Image.open(io.BytesIO(picture))
    picture_size = _get_picture_size(picture)
    if picture_size > 12 * 10**6:
        return None
    picture = ImageOps.invert(picture)
    return _convert_to_bytes(picture, content_type)


def _convert_to_bytes(picture: Image, content_type: str) -> bytes:
    result = io.BytesIO()
    picture_format = content_type.split("/")[-1]
    picture.save(result, format=picture_format)
    return result.getvalue()


def _get_picture_size(picture: Image) -> int:
    width, height = picture.size
    return width * height
