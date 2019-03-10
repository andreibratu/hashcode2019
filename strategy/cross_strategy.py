# import random
# from typing import Callable, List, Set
#
# from interesting import calculate_interesting_factor
# from models.individual import Individual
# from models.photo import Photo
#
# from config import Config
#
#
# def slice_cross(i1: Individual, i2: Individual) -> Individual:
#
#     def find_slide(i: Individual, id: int) -> int:
#         """Find the id of a given slide in individual."""
#
#         for idx, s in enumerate(i.slides):
#             if s.id == id:
#                 return idx
#
#         raise ValueError
#
#
#     def calculate_score(slides: List[Slide]) -> int:
#         score = 0
#         for idx in range(len(slides)-1):
#             score += calculate_interesting_factor(slides[idx], slides[idx+1])
#         return score
#
#
#     def get_slice(ids: Set[int], slides: List[Slide], idx: int) -> List[Slide]:
#         idx_l = idx
#         while idx_l not in ids:
#             idx_l -= 1
#             if idx-idx_l == Config.CHUNK:
#                 break
#
#         idx_r = idx
#         while idx_r not in ids:
#             idx_r += 1
#             if idx_r-idx == Config.CHUNK:
#                 break
#
#         return slides[idx_l:idx_r]
#
#
#     def add_to_used_ids(ids: Set[int], slides: List[Slide]):
#         for s in slides:
#             if s.photo2 is not None:
#                 s.add(s.photo2.id)
#             s.add(s.photo1.id)
#
#
#     def get_best_chunk_permutation(chunks: List[List[Slide]]) -> List[Slide]:
#         best_score = -1
#         best_permutation = []
#
#         for _ in range(Config.PERMUTATIONS):
#             random.shuffle(chunks)
#             permutation = [slide for chunk in chunks for slide in chunk]
#             score = calculate_score(permutation)
#             if score > best_score:
#                 best_score = score
#                 best_permutation = permutation
#
#         return best_permutation
#
#
#     flag_select_first = True
#     chunks = []
#     used_slide_ids = set()
#
#     ids = [s.id for s in i1.slides]
#     assert ids == [s.id for s in i2.slides]
#
#     for id in ids:
#         if id not in used_slide_ids:
#             idx1 = find_slide(i1, id)
#             idx2 = find_slide(i2, id)
#             slice1 = get_slice(used_slide_ids, i1.slides, idx1)
#             slice2 = get_slice(used_slide_ids, i2.slides, idx2)
#
#             if calculate_score(slice1) > calculate_score(slice2):
#                 selected = slice1
#             else:
#                 selected = slice2
#             add_to_used_ids(used_slide_ids, selected)
#
#     new_slides = get_best_chunk_permutation(chunks)
#     return Individual(new_slides)
