class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1 = tuple(map(int, version1.split(".")))
        version2 = tuple(map(int, version2.split(".")))
        for i in range(min(len(version1), len(version2))):
            if version1[i] > version2[i]:
                return 1
            elif version2[i] > version1[i]:
                return -1
            else:
                continue
        i = min(len(version1), len(version2))
        if len(version1) < len(version2):
            while i < len(version2):
                if version2[i] != 0:
                    return -1
                i += 1
        elif len(version2) < len(version1):
            while i < len(version1):
                if version1[i] != 0:
                    return 1
                i += 1
        return 0