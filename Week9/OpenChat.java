package Week9;
import java.util.*;
class OpenChat {
    public String[] solution(String[] record) {
        Map<String, String> nicknameMap = new HashMap<>();
        Map<String, List<Integer>> indexMap = new HashMap<>();
        List<String> log = new ArrayList<>();
        
        for (int i=0 ; i < record.length; i++) {
            String[] arguments = record[i].split(" ");
            String command = arguments[0];
            String userId = arguments[1];
            if (command.equals("Enter")) {
                String nickname = arguments[2];
                nicknameMap.put(userId, nickname);
                log.add(userId+"님이 들어왔습니다.");
                if (indexMap.get(userId) == null) {
                    indexMap.put(userId, new ArrayList<>());
                }
                List<Integer> indexList = indexMap.get(userId);
                indexList.add(log.size()-1);
            }
            else if (command.equals("Leave")) {
                log.add(userId+"님이 나갔습니다.");
                if (indexMap.get(userId) == null) {
                    indexMap.put(userId, new ArrayList<>());
                }
                List<Integer> indexList = indexMap.get(userId);
                indexList.add(log.size()-1);
            }
            else if (command.equals("Change")) {
                String nickname = arguments[2];
                nicknameMap.put(userId, nickname);
            }
        }
        
        for (Map.Entry<String, List<Integer>> entry : indexMap.entrySet()) {
            String userId = entry.getKey();
            String nickname = nicknameMap.get(userId);
            for (int idx : entry.getValue()) {
                String replaced = log.get(idx).replace(userId, nickname);
                log.set(idx, replaced);
            }
        }
        
        return log.stream().toArray(String[]::new);
    }
}