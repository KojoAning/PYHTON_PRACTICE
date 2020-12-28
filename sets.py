
# m = [2,1,3] # 1st set
# another_set = set(m)
# print(set(m))
# l = [1,3,2,5,4] # 2nd set
# s_from_list = set(l)
# print(s_from_list)
# s_from_list.add(91) # this is the differance between set and list. set retains only unique value not list.
# s_from_list.add(91)
# print(s_from_list)
# another_set.union(s_from_list)
# another_set.intersection(s_from_list)
# print(another_set)

k = [1,2]
s = set(k)
s.add(3)
s4 = {5,9}
s1 = s.union({1,2,3})
s2 = s. intersection({2,4,3})
s3 = s.isdisjoint(s4)
s4.remove(9)
print(s4)
