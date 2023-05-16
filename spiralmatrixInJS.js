function spiralOrder(matrix) {
    let res = [];
    let start_row = 0;
    let start_col = 0;
    let end_row = matrix.length - 1;
    let end_col = matrix[0].length - 1;
  
    while (start_row <= end_row && start_col <= end_col) {
      for (let i = start_col; i <= end_col; i++) {
        res.push(matrix[start_row][i]);
      }
      start_row++;
  
      for (let i = start_row; i <= end_row; i++) {
        res.push(matrix[i][end_col]);
      }
      end_col--;
  
      if (start_row <= end_row) {
        for (let i = end_col; i >= start_col; i--) {
          res.push(matrix[end_row][i]);
        }
        end_row--;
      }
  
      if (start_col <= end_col) {
        for (let i = end_row; i >= start_row; i--) {
          res.push(matrix[i][start_col]);
        }
        start_col++;
      }
    }
  
    return res;
  }
  
  let matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]];
  console.log(spiralOrder(matrix)); // Output: [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10]