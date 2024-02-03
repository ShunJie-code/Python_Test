import wordcloud
c = wordcloud.WordCloud()
c.generate('WordCloud for Python')
c.to_file('wordcloud.png')
