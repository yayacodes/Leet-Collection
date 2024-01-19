package Easy.Strings;

public class Strings {
    public Strings() {

    }

    public static void main(String[] args) {
        Strings a = new Strings();

        String x = "Hello world";
        a.reverseString(x.toCharArray());
    }

    // Reverse String
    public void reverseString(char[] s) {
        int i = 0;
        int j = s.length - 1;

        while (i < j) {
            char temp = s[i];
            s[i] = s[j];
            s[j] = temp;

            i++;
            j--;
        }
    }

    // First Unique Character in String
    public int firstUniqChar(String s) {
        int[] count = new int[26];

        for (char c : s.toCharArray()) {
            count[c - 'a']++;
        }

        for (int i = 0; i < s.length(); i++) {
            if (count[s.charAt(i) - 'a'] == 1) {
                return i;
            }
        }

        return -1;
    }
}
