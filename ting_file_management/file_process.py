import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    for i in range(instance.__len__()):
        if instance.search(i)["nome_do_arquivo"] == path_file:
            return None
    
    file_line = txt_importer(path_file)
    
    file_info = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(file_line),
        "linhas_do_arquivo": file_line,
    }
    instance.enqueue(file_info)
    print(file_info, file=sys.stdout)


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
