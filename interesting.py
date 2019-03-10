from models.slide import Slide

def calculate_interesting_factor(slide1: Slide, slide2: Slide) -> int:
    """Calculate interesting factor between two given slides."""

    photo1_tags = set(slide1.get_tags())
    photo2_tags = set(slide2.get_tags())

    # Set operations return a new set
    only_photo1 = len(photo1_tags-photo2_tags)
    only_photo2 = len(photo2_tags-photo1_tags)
    in_both_photos = len(photo1_tags&photo2_tags)

    return min(min(only_photo1, only_photo2), in_both_photos)
