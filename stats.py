def count_words(text):
	words = text.split()
	return len(words)

def count_characters(text):
	lower = text.lower()

	count = {}
	for char in lower:
		if char in count:
			count[char] += 1
		else:
			count[char] = 1
	return count

def convert_to_list(dict):
	list = []
	for item in dict:
		n = {
			"char": item,
			"count": dict[item]
		}
		list.append(n)
	list.sort(key=lambda x: x["count"], reverse=True)
	return list
