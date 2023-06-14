from ting_file_management.file_management import txt_importer
import sys

def process(path_file, instance):
    for i in range(len(instance)):
        eachFile = instance.search(i)
        if eachFile["nome_do_arquivo"] == path_file:
            return None
    archive = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(txt_importer(path_file)),
        "linhas_do_arquivo": txt_importer(path_file)
    }
    instance.enqueue(archive)
    print(archive)
    return archive


def remove(instance):
    if len(instance) == 0:
        print("Não há elementos")
        return
    path = instance.dequeue()
    print (f"Arquivo {path['nome_do_arquivo']} removido com sucesso")


def file_metadata(instance, position):
    if 0 <= position < len(instance):
        archive = instance.search(position)
        print(archive)
        return
    sys.stderr.write("Posição inválida")

