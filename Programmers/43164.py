def solution(tickets):
    # 1. 그래프 생성
    routes = dict()

    for (start, end) in tickets:
        routes[start] = routes.get(start, []) + [end]

        # 2. 시작점 - [끝점] 역순으로 정렬
    for r in routes.keys():
        routes[r].sort(reverse=True)

    # 3. DFS 알고리즘으로 path를 만들어줌.
    st = ["ICN"]
    path = []

    while st:
        top = st[-1]
        if top not in routes or len(routes[top]) == 0:
            path.append(st.pop())
        else:
            st.append(routes[top][-1])
            routes[top] = routes[top][:-1]

    # 4. 만든 path를 거꾸로 돌림.
    answer = path[::-1]
    return answer
