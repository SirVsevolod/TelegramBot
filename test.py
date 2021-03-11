from ParseSub import ParseNews
import re

n = ParseNews()
regex = re.compile(r'[\n\r\t]')
print(regex.sub('', n.GetDescriptionNews('/news/kristi-a-skryuchennyy-domishko/')))
print(n.NewsTitle('/news/kristi-a-skryuchennyy-domishko/'))




