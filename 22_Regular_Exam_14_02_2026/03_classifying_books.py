def classify_books(*args, **kwargs):
    books = {}
    fiction = []
    non_fiction = []
    result = []

    for number, name in kwargs.items():
        if name not in books:
            books[name] = ""
        books[name] = number

    for genre, name in args:
        if genre == "fiction":
            if name in books:
                fiction.append((books[name], name))
        elif genre == "non_fiction":
            if name in books:
                non_fiction.append((books[name], name))

    sorted_fiction = sorted(fiction)
    sorted_non_fiction = sorted(non_fiction, reverse=True)

    if sorted_fiction:
        result.append("Fiction Books:")
        for number, title in sorted_fiction:
            result.append(f"~~~{number}#{title}")

    if sorted_non_fiction:
        result.append("Non-Fiction Books:")
        for number, title in sorted_non_fiction:
            result.append(f"***{number}#{title}")

    return "\n".join(result)


print(classify_books(
    ("fiction", "Brave New World"),
    ("non_fiction", "The Art of War"),
    NF3421NN="The Art of War",
    FF1234UU="Brave New World"
))
print("==========================================")
print(classify_books(
    ("non_fiction", "The Art of War"),
    ("fiction", "The Great Gatsby"),
    ("non_fiction", "A Brief History of Time"),
    ("fiction", "Brave New World"),
    FF1234HH="The Great Gatsby",
    NF3845UU="A Brief History of Time",
    NF3421NN="The Art of War",
    FF1234UU="Brave New World"
))
print("==========================================")
print(classify_books(
    ("fiction", "Brave New World"),
    ("fiction", "The Catcher in the Rye"),
    ("fiction", "1984"),
    FICCITRZZ="The Catcher in the Rye",
    FIC1984XX="1984",
    FICBNWYYY="Brave New World"
))
print("==========================================")
print(classify_books(
    ("non_fiction", "Sapiens"),
    ("non_fiction", "Homo Deus"),
    ("non_fiction", "The Selfish Gene"),
    NF123ABC="Sapiens",
    NF987XYZ="Homo Deus",
    NF456DEF="The Selfish Gene"
))

