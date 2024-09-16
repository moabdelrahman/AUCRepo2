from lxml import html
import os
with open('Leaderboard _ HackerRank.html', 'r', encoding='UTF-8') as file:
	data = file.read()
tree = html.fromstring(data)
rows = tree.xpath("//div[@class='leaderboard-list-view']")
for row in rows:
	children = row.getchildren()[0].getchildren()
	print(children[1].getchildren()[0].getchildren()[0].text.strip(),'\t' ,children[3].getchildren()[0].text.strip());
print("Total Scores =", len(rows))