open_list = ['[', '{', '(']
close_list = [']', '}', ')']

class Stack:
    def __init__(self, size, _max=5):
        self.max = _max
        if size < 1:
            raise Exception('Пустой стек')
        if size > _max:
            raise Exception('Неправильные данные')
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)
        if self.size() > self.max:
            raise Exception('Стек переполнен')

    def pop(self):
        return self.items.pop()
        if self.size() < 1:
            raise Exception('Стек пустой')

    def peek(self):
        return self.items[len(self.items) -1]

    def size(self):
        return len(self.items)

    def show_elements(self):
        return(self.items)

    def check(myStr):
        stack = []
        for i in myStr:
            if i in open_list:
                stack.append(i)
            elif i in close_list:
                pos = close_list.index(i)
                if ((len(stack) > 0) and
                    (open_list[pos] == stack[len(stack) -1])):
                    stack.pop()
                else:
                    return 'Unbalanced'

        if len(stack) == 0:
            return 'Balance'


if __name__ == '__main__':
    print('Введите количество элементов в стеке')
    n = int(input())
    st = Stack(n)
    for i in range(n):
        element=int(input())
        st.push(element)
    print('Ваш стек', st.show_elements())

    string = '{[]{()}}'
    print(string,'-', check(string))