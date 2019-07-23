def max_area_histogram(arr):
    m_a = 0
    stack = []

    for i in range(len(arr)+1):
        if len(stack) == 0:
            stack.append(i)
        elif i == len(arr):
            while len(stack) > 0:
                top = stack.pop()
                if len(stack) == 0:
                    m_a = max(m_a, arr[top] * i)
                else:
                    m_a = max(m_a, arr[top] * (i - stack[-1] - 1))
        elif arr[stack[-1]] <= arr[i]:
            stack.append(i)
        else:
            while len(stack) > 0 and arr[stack[-1]] >= arr[i]:
                top = stack.pop()
                if len(stack) == 0:
                    m_a = max(m_a, arr[top] * i)
                else:
                    m_a = max(m_a, arr[top] * (i - stack[-1] - 1))
            stack.append(i)
    print(m_a)


max_area_histogram([1,2,2,3,1,0,4,9,1])
