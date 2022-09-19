class Solution(object):
    def findDuplicate(self, paths):
        dict_of_files = {}
        for direct in paths:
            files = direct.split()[1:]
            file_path = direct.split()[0] + '/'
            for file in files:
                enterin = file.split('.')[1]
                value = dict_of_files.get(enterin, list())
                value.append(file_path + file.split('(')[0])
                dict_of_files[enterin] = value
        res = []
        for value in dict_of_files.values():
            if len(value) > 1:
                res.append(value)
        print(res)
        return res
            
        