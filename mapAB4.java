public Map<String, String> mapAB4(Map<String, String> map) {
    String a = map.getOrDefault("a", "");
    String b = map.getOrDefault("b", "");
    
    if (a.compareTo(b) > 0) {
        map.put("c", a);
    } else if (a.compareTo(b) < 0) {
        map.put("c", b);
    } else {
        map.put("c", "");
    }
    
    return map;
}
