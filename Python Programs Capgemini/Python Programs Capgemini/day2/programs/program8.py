dict = {"merry":"god", "christmas":"jul", "and":"och","happy":"gott", "new":"nytt", "year":"år"}

def translate(words):
	return map(lambda x: dict[x.lower()], words)

#test
print(list(translate(['Merry', 'christmas', 'and', 'happy', 'new', 'year'])))
