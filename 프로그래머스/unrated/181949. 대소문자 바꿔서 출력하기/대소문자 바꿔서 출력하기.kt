fun main(args: Array<String>) {
    val s1 = readLine()!!
    
    val S = s1.toMutableList()
    var index = 0
    
    for (s in S) {
        if (s.isUpperCase()) {
            S[index] = s.toLowerCase()
            index++
        } else {
            S[index] = s.toUpperCase()
            index++
        }
    }
    print(S.joinToString(""))
    
}