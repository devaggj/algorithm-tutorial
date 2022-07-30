/*
[LINK] https://programmers.co.kr/learn/courses/30/lessons/1835?language=java
[REF] https://velog.io/@minskim2/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EB%8B%A8%EC%B2%B4%EC%82%AC%EC%A7%84-%EC%B0%8D%EA%B8%B0
[REF] https://youngest-programming.tistory.com/586
[TITLE] 단체사진 찍기
*/
class Solution {

    static String[] friends = {"A", "C", "F", "J", "M", "N", "R", "T"}; // return 3648
    static int answer = 0;

    public static void main(String[] args) {
        int n = 2;
        String[] data = {"N~F=0", "R~T>2"};

        System.out.println(solution(n, data));
    }

    static int solution(int n, String[] data) {
        boolean[] visited = new boolean[friends.length];
        dfs("", visited, data);

        return answer;
    }

    static void dfs(String combination, boolean[] visited, String[] data) {
        if (combination.length() == 8) {
            if (check(combination, data)) {
                answer++;
            }
            return;
        }

        for (int i=0; i<friends.length; i++) {
            if (!visited[i]) {
                visited[i] = true;
                String newComb = combination + friends[i];
                dfs(newComb, visited, data);
                visited[i] = false;
            }
        }
    }

    static boolean check(String combination, String[] data) {
        for (String condition : data) {
            int friend1 = combination.indexOf(condition.charAt(0));
            int friend2 = combination.indexOf(condition.charAt(2));
            char operator = condition.charAt(3);
            int inBetween = condition.charAt(4) - '0' + 1;

            if (operator == '=') {
                if (!(Math.abs(friend1 - friend2) == inBetween)) return false;
            }
            else if (operator == '>') {
                if (!(Math.abs(friend1 - friend2) > inBetween)) return false;
            }
            else if (operator == '<') {
                if (!(Math.abs(friend1 - friend2) < inBetween)) return false;
            }
        }
        return true;
    }

}