class Node(object):  ## Trie Node 구성
    def __init__(self, key):
        self.key = key  ## 시작값(이전의 값 개념)
        self.remain_length = {}  ## Terminal까지 남아있는 문자열의 길이
        self.children = {}  ## 자식


class Trie(object):
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        ## key에는 문자, length에는 남아있는 string의 길이를 담았음
        curr_node = self.head

        remain_length = len(string)
        if remain_length in curr_node.remain_length:
            curr_node.remain_length[remain_length] += 1
        else:
            curr_node.remain_length[remain_length] = 1
        for char in string:
            if char not in curr_node.children:
                curr_node.children[char] = Node(char)

            curr_node = curr_node.children[char]
            remain_length -= 1
            if remain_length in curr_node.remain_length:
                curr_node.remain_length[remain_length] += 1
            else:
                curr_node.remain_length[remain_length] = 1

    def search_count(self, string, check_length):
        curr_node = self.head
        ## 찾아야할 "?" 포함한 string의 길이가 없다면 return 0
        if check_length + len(string) not in curr_node.remain_length:
            return 0

        for char in string:
            ## 찾아야할 string이 없다면 return 0
            if char in curr_node.children:
                curr_node = curr_node.children[char]
            else:
                return 0
        ## string은 존재하는데 check_length가 remain_length에 있는지 확인!
        if check_length in curr_node.remain_length:
            return curr_node.remain_length[check_length]
        else:
            return 0


def solution(words, queries):
    t = Trie()
    inv_t = Trie()
    for word in words:
        t.insert(word)
        inv_t.insert(word[-1::-1])

    answer = []
    for i in range(len(queries)):
        query = queries[i]
        if query[0] is '?':  # 시작이 '?'
            query = query[-1::-1]
            chars = query.replace("?", "")
            check_length = len(query) - len(chars)
            # end = query.find('?')
            # chars = query[:end]
            answer.append(inv_t.search_count(chars, check_length))
        else:  # 시작이 알파벳
            chars = query.replace("?", "")
            check_length = len(query) - len(chars)
            # end = query.find('?')
            # chars = query[:end]
            answer.append(t.search_count(chars, check_length))

    return answer
