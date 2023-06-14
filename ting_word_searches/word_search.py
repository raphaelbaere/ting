def exists_word(word, instance):
    r = []
    c = 0

    for i in range(len(instance)):
        q = instance.search(i)
        ins_obj = {
            "palavra": word,
            "arquivo": q["nome_do_arquivo"],
            "ocorrencias": [
                {"linha": index + 1}
                for index, line in enumerate(q["linhas_do_arquivo"])
                if word.lower() in line.lower()
            ],
        }

        r.append(ins_obj)

        if not len(ins_obj["ocorrencias"]):
            c += 1

    if c == len(instance):
        return []

    return r


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
