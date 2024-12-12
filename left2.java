public String left2(String str) {
    if (str.length() < 2) {
        return "";
    }
    String rotatedLeft = str.substring(2, str.length()) + str.substring(0, 2);
    return rotatedLeft;
}