package Week9;

import java.util.LinkedList;
import java.util.Queue;
import java.util.Stack;

public class DeliveryBox {
    public int solution(int[] order) {
        int loaded = 0;
        Queue<Integer> belt = new LinkedList<>();
        Stack<Integer> secondBelt = new Stack<>();
        
        for(int i=1; i<=order.length; i++) {
            belt.offer(i);
        }
        
        for(int i=0; i<order.length; i++){
            int pick = 0;
            if (!belt.isEmpty()) {
                if (belt.peek() > order[i]) pick = belt.peek();
                else pick = belt.poll();
            }
            while(!belt.isEmpty() && pick < order[i]) {
                secondBelt.add(pick);
                pick = belt.poll();
            }
            if (pick == order[i]) {
                loaded++;
                continue;
            }
            int second = 0;
            if (!secondBelt.isEmpty()) {
                second = secondBelt.pop();
            }
            if (second != order[i]) break;
            else loaded++;
        }
        
        return loaded;
    }
}
