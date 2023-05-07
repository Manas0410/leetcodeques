def secondLargest(height):
    """
    :type height: List[int]
    :rtype: int
    """
    if len(height) < 2:
        return None

    lheightgest = second_lheightgest = float('-inf')

    for num in height:
        if num > lheightgest:
            second_lheightgest = lheightgest
            lheightgest = num
        elif num > second_lheightgest and num < lheightgest:
            second_lheightgest = num

    if second_lheightgest == float('-inf'):
        return None
    else:
        return second_lheightgest


print(secondLargest([1, 8, 6, 2, 5, 4, 8, 3, 7]))
print(secondLargest([1, 1]))
