spisok = ["Ароматизатор", "Окно", "Море", "Русалка", "Бейбибум", "Годзила"]

count = 0

for word in spisok:
    print(word) 
    if "г" in word.lower():
        count += 1 

print(count)
