public class Words {
    public String wordEnds(String word, String target) {
        String result = "";
        int targetLength = target.length();

        for (int i = 0; i <= word.length() - targetLength; i++) {
            // Check if the substring matches the target
            if (word.substring(i, i + targetLength).equals(target)) {
                // Add the character before the target if it exists
                if (i > 0) {
                    result += word.charAt(i - 1);
                }
                // Add the character after the target if it exists
                if (i + targetLength < word.length()) {
                    result += word.charAt(i + targetLength);
                }
            }
        }

        return result;
    }

}
