package Week9;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class FileNameSort {
    private static final String regex = "([^0-9]+)([0-9]{1,5})(.*)";
    public String[] solution(String[] files) {
        List<String> fileList = new ArrayList<>(Arrays.asList(files));
        fileList.sort((f1, f2) -> {
            File file1 = parse(f1);
            File file2 = parse(f2);
            int first = file1.head.toLowerCase().compareTo(file2.head.toLowerCase());
            if (first != 0) return first;
            else return Integer.parseInt(file1.number) - Integer.parseInt(file2.number);
        });
        return fileList.stream().toArray(String[]::new);
    }
    
    File parse(String fileName) {
        Pattern pattern = Pattern.compile(regex);
        Matcher matcher = pattern.matcher(fileName);
        if (matcher.find()) {
            File file = new File(matcher.group(1), matcher.group(2), matcher.group(3));
            return file;
        }
        return null;
    }
    
    class File {
        String head;
        String number;
        String tail;
        File (String head, String number, String tail) {
            this.head = head;
            this.number = number;
            this.tail = tail;
        }
    }
}
