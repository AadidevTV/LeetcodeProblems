class Solution:
    def reverse(self, x):
        list_x = list(str(x))
        return_list = []
        if list_x[0] == "-":
            list_x.remove("-")
            for index in range(1, len(list_x)+1):
                number = len(list_x)-index
                return_list.append(list_x[number])
            return_list.insert(0 , "-")
        elif list_x[0] != "-":
            for index in range(1, len(list_x)+1):
                number = len(list_x)-index
                return_list.append(list_x[number])
        if return_list[0] == "0" and len(return_list)!= 1:
            return_list.remove("0")
        final_list = int("".join(return_list))
        if final_list > (2**31-1):
            return 0
        elif final_list < -(2**31):
            return 0
        return final_list

# this works.