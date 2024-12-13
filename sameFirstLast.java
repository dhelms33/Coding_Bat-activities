public boolean sameFirstLast(int arr[]) {
  if (arr.length == 0) {
    return false;
  }
  return arr[0] == arr[arr.length-1];
}