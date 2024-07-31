# Домашнее задание по теме "Оператор "with".

class WordsFinder:

    def __init__(self, *file_names):
        self.file_names = file_names

    def del_sign(self, str_f):  # создаем функцию для удаления знаков пунктуации
        sign = [',', '.', '=', '!', '?', ';', ':', ' - ']  # создаем список знаков, которые нужно удалить
        for x in sign:
            str_f = str_f.replace(x, '')  # заменяем знаки на пробел
        return str_f  # возвращаем очищенную от знаков строку

    def get_all_words(self):
        all_words = {}  # создаем пустой словарь
        for name in self.file_names:
            with open(name, 'r', encoding='utf-8') as file:
                str_f = file.read().lower()  # считываем текст и приводим к нижнему регистру
                str_rezult = self.del_sign(str_f)  # очищааем текст от знаков препинания
                sub_words = str_rezult.split()  # делим весь текст на подстроки
                all_words[name] = sub_words  # создается словарь с ключом - наимен-ие файла, а значение -
                # список из слов этого файла
        return all_words

    def find(self, word):
        find_word = {}  # создаем пустой словарь
        word = word.lower()  # Приводим искомое слово к нижнему регистру
        all_words = self.get_all_words()
        for name, sub_words in all_words.items():
            if word in sub_words:
                index = sub_words.index(word) + 1  # +1 потому что индексация начинается с 0
                find_word[name] = index
        return find_word

    def count(self, word):
        count_word = {}  # создаем пустой словарь
        word = word.lower()  # Приводим искомое слово к нижнему регистру
        all_words = self.get_all_words()
        for name, sub_words in all_words.items():
            count = sub_words.count(word)
            if count > 0:
                count_word[name] = count
            else:
                print('Искомого слова в словаре нет!')
                return ''
        return count_word


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT'))  # 4 слова teXT в тексте всего
finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
                      'Rudyard Kipling - If.txt',
                      'Mother Goose - Monday’s Child.txt')
print(finder1.get_all_words())
print(finder1.find('the'))
print(finder1.count('the'))
