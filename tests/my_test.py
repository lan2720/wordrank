import wordrank
from wordrank.features.text_feature import TextFeature
from wordrank.features.statistics_feature import StatisticsFeature
from wordrank.features.language_feature import LanguageFeature

q = "腾讯的Q3财报"#'哪里下载电视剧周恩来？'
r = wordrank.rank(q)
print(r)
tf = TextFeature()
