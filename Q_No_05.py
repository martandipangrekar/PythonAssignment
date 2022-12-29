frozen_set_1 = frozenset(['A', 'B', 'C', 'D'])
frozen_set_2 = frozenset(['A', 2, 'C', 4])

frozen_set_union = frozen_set_1.union(frozen_set_2)
print(frozen_set_union)


frozen_set_common = frozen_set_1.intersection(frozen_set_2)
print(frozen_set_common)

frozen_set_difference = frozen_set_1.difference(frozen_set_2)
print(frozen_set_difference)


frozen_set_distinct = frozen_set_1.symmetric_difference(frozen_set_2)
print(frozen_set_distinct)
