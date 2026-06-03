class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for st in strs:
            key = "".join(sorted(st))
            groups[key].append(st)

        return list(groups.values())



# ["act","pots","tops","cat","stop","hat"]

# for st = act
# key = act
# groups = {
#     act:[act]

#     }
# for st = pots
# key = opst
# groups = {
#     act:[act]
#     opst:[pots]

#     }
# for st = tops
# key = opst
# groups = {
#     act:[act]
#     opst:[pots,tops]

#     }
# for st = cat
# key = act
# groups = {
#     act:[act,cat]
#     opst:[pots,tops]

#     }
# for st = stop
# key = opst
# groups = {
#     act:[act,cat]
#     opst:[pots,tops,stop]

#     }
# for st = hat
# key = aht
# groups = {
#     act:[act,cat]
#     opst:[pots,tops,stop]
#     aht:[hat]
#     }