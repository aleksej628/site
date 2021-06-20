# class Translate(object):
#     """Улучшает предложение"""
#     DOT = "."
#
#     def translate_function(self, a):
#         return print(f'{a}+{self.DOT}')
#     """ Добавляет точку к предложению"""
#
#
# translate = Translate()
# translate.translate_function("")
class Retrieval(object):
    i = 1
    i2 = 1
    i3 = 1
    obj1 = True
    obj2 = True
    object_ = None
    dictionary = ["Я встану в 6 утра", "Жду тебя в 18:00",
                  "13:00 1 дня это 13:00",
                  "2 брата вернулись лишь в 20:00 вечера",
                  "жаль что не существует 25:00", ]

    def retrieval_function(self):
        for self.i in self.dictionary:
            while self.i3 != len(self.i):
                while self.i2 != len(self.i):
                    self.object_ = self.i[self.i3: self.i2]
                    if self.object_== '1 у' or '2 у' or '3 у' or '4 у' or '5 у' or'6 у' or '7 у' or '8' or'9' or '10'
                    if self.object_ == '6 утра':
                        return print('6:00')
                    elif self.object_ == '13:00':
                        return print(self.object_)
                    elif self.object_ == '20:00':
                        return print(self.object_)
                    elif self.object_ == '25:00':
                        return print('-')
                    self.i2 += 1


Retrieval().retrieval_function()
