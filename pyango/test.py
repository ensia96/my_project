class Queue:
    def __init__(self):
        self.waiting = []

    def enqueue(self, person):
        self.waiting.append(person)
        return "{0}이(가)  대기줄에 추가 되었습니다.".format(person)

    def dequeue(self):
        if self.is_empty():
            return "대기자 없음! 아무나 튀어오슈"
        else:
            return self.waiting.pop(0)

    def front(self):
        if self.is_empty():
            return "대기자 없음! 아무나 튀어오슈"
        else:
            person = self.waiting.pop(0)
            return person

    def is_empty(self):
        return len(self.waiting) == 0

    def print_queue(self):
        return "저희 카페 대기 손님은 {0}으로 총{1}명이 대기 중입니다.".format(self.waiting, len(self.waiting) )


queue = Queue()

print( queue.is_empty() )
print( queue.enqueue("예리") )
print( queue.enqueue("두리") )
print( queue.enqueue("준식") )
print( queue.enqueue("승현") )
print( queue.waiting )

print( queue.print_queue() )

print( queue.front() )
print( queue.waiting )

print( queue.dequeue() )
print( queue.dequeue() )

print( queue.print_queue() )

print( queue.waiting )
print( queue.dequeue() )
print( queue.dequeue() )
print( queue.front() )