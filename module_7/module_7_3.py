class WordsFinder():
  def __init__(self, *args):
    self.file_names = args


  def get_list_words(self, file):
    list_chr = ['\n', ',', '.', '=', '!', '?', ';', ':', ' - ']
    new_str = file.lower()
    for chr in list_chr:
      new_str = new_str.replace(chr, ' ')
    return new_str.split()
    

  def get_all_words(self):
    all_words = {}
    for file_name in self.file_names:
      with open(file_name, 'r', encoding='utf-8') as file:
        all_words.update({file_name: self.get_list_words(file.read())})
    return all_words    


  def find(self, word):
    all_words = self.get_all_words()
    result = {}
    for file_name, list_words in all_words.items():
      try:
        index = list_words.index(word.lower())
        result.update({file_name: index})
      except ValueError:
        result.update({file_name: -1})
    return result


  def count(self, word):
    all_words = self.get_all_words()
    result = {}
    for file_name, list_words in all_words.items():
      count = list_words.count(word.lower())
      result.update({file_name: count})
    return result


finder2 = WordsFinder('text1.txt', "monday's chaild.txt", 'O Captain! My Captain.txt', 'if.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего

print(finder2.find('the'))
print(finder2.count('the'))
