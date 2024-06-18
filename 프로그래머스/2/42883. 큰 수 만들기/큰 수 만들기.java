import java.util.Stack;

public class Solution {
    public String solution(String number, int k) {
        Stack<Character> stack = new Stack<>();
        
        for (int i = 0; i < number.length(); i++) {
            char num = number.charAt(i);
            
            while (!stack.isEmpty() && stack.peek() < num && k > 0) {
                stack.pop();
                k--;
            }
            stack.push(num);
        }
        
        // k가 남아 있는 경우 뒤에서부터 k개 제거
        while (k > 0) {
            stack.pop();
            k--;
        }
        
        // Stack의 내용을 StringBuilder로 옮김
        StringBuilder answer = new StringBuilder();
        for (char ch : stack) {
            answer.append(ch);
        }
        
        return answer.toString();
    }
}
