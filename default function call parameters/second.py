def process(subject, action='мыла', object='раму'):
    print("Кто - ", subject)
    print("Делал(а) - ", action)
    print("Над чем - ", object)
    print("Получается :", subject, action, object)


process(subject='Мама')
process(subject='Папа', action='сломал')
process(subject='Крижановский', action='видел', object='Ленина')
