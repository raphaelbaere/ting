from ting_file_management.priority_queue import PriorityQueue
import pytest


def test_basic_priority_queueing():
    PrioriryQueueInstance = PriorityQueue()
    last = {"qtd_linhas": 7}
    first = {"qtd_linhas": 3}
    second = {"qtd_linhas": 4}
    PrioriryQueueInstance.enqueue(last)
    PrioriryQueueInstance.enqueue(first)
    PrioriryQueueInstance.enqueue(second)

    assert len(PrioriryQueueInstance) == 3

    assert PrioriryQueueInstance.search(0) == first
    assert PrioriryQueueInstance.search(1) == second
    assert PrioriryQueueInstance.search(2) == last

    given = PrioriryQueueInstance.dequeue()
    assert len(PrioriryQueueInstance) == 2
    assert given == first

    with pytest.raises(IndexError):
        PrioriryQueueInstance.search(10)
