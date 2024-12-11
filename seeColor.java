public String seeColor(String str) {
    String red = "red";
    String blue = "blue";
    if (str.startsWith("red")) { // Closing parenthesis added here
        return red;
    }
    if (str.startsWith("blue")) {
        return blue;
    } else {
        return "";
    }
}
