from ting_file_management.priority_queue import PriorityQueue
import pytest

mock_one = { "nome_do_arquivo": "file_name_one.txt", "qtd_linhas": 3,}
mock_two = { "nome_do_arquivo": "file_name_two.txt", "qtd_linhas": 5,}
mock_six = { "nome_do_arquivo": "file_name_six.txt", "qtd_linhas": 7,}


def test_basic_priority_queueing():
    priority_queue = PriorityQueue()
    priority_queue.enqueue(mock_one)
    priority_queue.enqueue(mock_two)
    priority_queue.enqueue(mock_six)
    assert len(priority_queue) == 3
    assert priority_queue.search(2) is mock_six
    priority_queue.dequeue()
    assert len(priority_queue) == 2
    with pytest.raises(IndexError):
        priority_queue.search(4)
    assert priority_queue.is_priority(mock_two) is False
