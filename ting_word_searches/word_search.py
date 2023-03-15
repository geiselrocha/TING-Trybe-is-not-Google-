def exists_word(word, instance):
    result = []
    
    for i in range(len(instance)):
        data = instance.search(i)
        file_line = data["linhas_do_arquivo"]
        occurrences = []

        for j in range(len(file_line)):
            if word.lower() in file_line[j].lower():
                occurrences.append(j + 1)
    
        if len(occurrences):
            result.append({
                "palavra": word,
                "arquivo": data["nome_do_arquivo"],
                "ocorrencias": [{"linha": row} for row in occurrences],
            })

    return result


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
