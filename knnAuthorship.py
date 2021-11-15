import pandas as pd
import sys
from collections import Counter, defaultdict


# def knn(d: Data, k: int):
#     data_distance = defaultdict(list)
#     data = d.data
#     result = []
#     for index, current_data in enumerate(data):
#         other_data = data[0:index] + data[index+1:]
#         for j , other in enumerate(other_data):
#             distance_computed = eucledian_distance(d, current_data, other)
#             if j < index:
#                 data_distance[index].append((distance_computed, j))
#             else:
#                 data_distance[index].append((distance_computed,j + 1))
#
#     for index, value in data_distance.items():
#         sorted_value = sorted(value, key=lambda x: x[0])
#         closest_point = sorted_value[0:k]
#         closest_point_class_variable = [data[x[1]][d.index_class_variable] for x in closest_point]
#         counter_result = Counter(closest_point_class_variable)
#         most_popular_class = max(counter_result, key=counter_result.get)
#         result.append(most_popular_class)
#     return result
#
#
# def eucledian_distance(d: Data, current_data: [], other_data: []):
#     i = 0
#     distance_total = 0
#     while i < len(current_data):
#         attribute = d.attributes[i]
#         categorical = d.categorical_numerical[attribute] == 'categorical'
#         if not categorical: #means numeric
#
#             try:
#                 current_value = float(current_data[i])
#                 other_value = float(other_data[i])
#                 distance_total = distance_total + (current_value - other_value) ** 2
#             except:
#                 i += 1
#                 continue
#         else: #for categorical
#             #just compute it using ascii value of each word and add them up
#             current_value = list(current_data[i])
#             other_value = list(other_data[i])
#             # import pdb; pdb.set_trace()
#             similarity = jaccard_similarity(current_value, other_value)
#             distance = 1 - similarity
#             distance_total = distance_total + distance
#         i += 1
#     return distance_total ** (0.5)
#
# def jaccard_similarity(current_value, other_value):
#     intersection = len(list(set(current_value).intersection(list(set(other_value)))))
#     union = (len(current_value) + len(other_value) - intersection)
#     return float(intersection) / union


if __name__ == '__main__':

    tfidf_file = sys.argv[1]
    words_file = sys.argv[2]
    tfidf_data = pd.read_csv(tfidf_file, index_col=False)
    words_data = pd.read_csv(words_file, index_col=False)
    import pdb; pdb.set_trace()