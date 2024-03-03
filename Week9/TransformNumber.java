package Week9;

import java.util.HashSet;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Set;

public class TransformNumber {
    int min = Integer.MAX_VALUE;
    Set<Integer> numbers = new HashSet<>();
    
    public int solution(int x, int y, int n) {
        Queue<Calculation> queue = new LinkedList<>();
        return bfs(queue, x, y, n);
    }
    
    int bfs(Queue<Calculation> queue, int x, int y, int n) {
        queue.add(new Calculation(x, 0));
        while (!queue.isEmpty()) {
            Calculation cal = queue.poll();
						// numbers.add(cal.x); -> 여기서 하지 않음.
		
            if (cal.x == y) return cal.depth;
            
            int added = add(cal.x, n);
            int doubled = makeDouble(cal.x);
            int tripled = makeTriple(cal.x);

            if (tripled <= y && !numbers.contains(tripled)) {
                queue.offer(new Calculation(tripled, cal.depth + 1)); 
                numbers.add(tripled);
            }
            if (doubled <= y && !numbers.contains(doubled)) {
                queue.offer(new Calculation(doubled, cal.depth + 1)); 
                numbers.add(doubled);
            }
            if (added <= y && !numbers.contains(added)) {
                queue.offer(new Calculation(added, cal.depth + 1)); 
                numbers.add(added);
            }
        }
        return -1;
    }
   
    int add(int x, int n) {
        return x + n;
    }
    
    int makeDouble(int x) {
        return x * 2;
    }
    
    int makeTriple(int x) {
        return x * 3;
    }
    
    class Calculation {
        int x;
        int depth;
        
        Calculation(int x, int depth) {
            this.x = x;
            this.depth = depth;
        }
    }
    
}
