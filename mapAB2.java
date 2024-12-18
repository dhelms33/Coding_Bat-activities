public Map<String, String> mapAB2(Map<String, String> map) {
    // Check if both keys "a" and "b" are present in the map
    if (map.containsKey("a") && map.containsKey("b")) {
        // Check if their values are equal
        if (map.get("a").equals(map.get("b"))) {
            // Remove both keys
            map.remove("a");
            map.remove("b");
        }
    }
    // Return the modified map
    return map;
}
