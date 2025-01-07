public int bunnyEars(int bunnies) {
  if (bunnies == 0) {
    return 0; // Base case: No bunnies, no ears.
  }
  return 2 + bunnyEars(bunnies - 1); // Recursive step: Add 2 ears and reduce bunnies by 1.
}
