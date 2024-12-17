public boolean less20(int num) {
    return ((num % 20 == 19) || (num % 20 == 18));
    //if remainder == 1 or 2 this only works for a couple of circumstances
    //if rem == 19 or 18 then this works for bigger nums
  }