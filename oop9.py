# multi level inheritance


class Dad:
    dance = 1
    basketball = 2
    def d(self):
        return f"i dance {self.dance} times a day"
    pass
class Son(Dad):
    dance=2
    def d(self):
        return f"i dance {self.dance} times a day"

    pass
class Grnadson(Son):
    dance = 3
    # def d(self):
    #     return f"i dance {self.dance} times a day"
    #
    # pass


carry = Dad()
larry = Son()
Harry = Grnadson()

print(Harry.basketball)