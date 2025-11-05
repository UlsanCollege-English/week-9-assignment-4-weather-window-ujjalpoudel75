import heapq

def sliding_window_max(nums, k):
    # Handle invalid or edge cases
    if not nums or k <= 0:
        return []
    n = len(nums)
    if k > n:
        return [max(nums)]

    result = []
    heap = []  # will store (-value, index)

    for i in range(n):
        # Push current element (as negative to simulate max-heap)
        heapq.heappush(heap, (-nums[i], i))

        # Remove elements that are outside the current window
        while heap and heap[0][1] <= i - k:
            heapq.heappop(heap)

        # Record current window max once we have at least k elements
        if i >= k - 1:
            result.append(-heap[0][0])

    return result
