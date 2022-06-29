class Stack():
    def __init__(self, elements: list):
        self.elements = elements

    def isEmpty(self):
        return self.elements == None

    def push(self, element):
        self.elements.append(element)

    def pop(self):
        delete_first_out = self.elements.pop()
        return delete_first_out

    def peek(self):
        first_out = self.elements[len(self.elements)-1]
        return first_out

    def size(self):
        number_of_elements = len(self.elements)
        return number_of_elements


def check(cheking_list):
    if len(cheking_list) % 2:
        return 'Несбалансированно'
    else:
        new_stack = Stack([])
        open_dir = {1:'(', 2:'[', 3:'{'}
        close_dir = {1:')', 2:']', 3:'}'}
        for id, item in enumerate(cheking_list):
            if item in open_dir.values():
                new_stack.push(item)
            else:
                for k, v in open_dir.items():
                    if new_stack.peek() == v:
                        key = k
                if item != close_dir[key]:
                    return 'Несбалансированно'
                elif item == close_dir[key]:
                    new_stack.pop()
    return 'Cбалансированно'


subsequence1 = ('(((([{}]))))')
subsequence2 = ('[([])((([[[]]])))]{()}')
subsequence3 = ('{{[()]}}')
bad_subsequence1 = ('}{}')
bad_subsequence2 = ('{{[(])]}}')
bad_subsequence3 = ('[[{())}]')


if __name__ == "__main__":
    subsequence_string = input('Введите строку, состоящую из скобок, для проверки: ').strip('')
    subsequence_list = list(subsequence_string)
    print(check(subsequence_list))