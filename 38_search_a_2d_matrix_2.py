def searchMatrix(self, matrix, target):
    # write your code here
    if not matrix or not matrix[0]:
        return 0 
    row, col = len(matrix)-1, 0
    count = 0
    while row >= 0 and col < len(matrix[0]):
        if matrix[row][col] == target:
            count += 1
            row -= 1
            col += 1
        elif matrix[row][col] > target:
            row -= 1
        else:
            col += 1
    return count 