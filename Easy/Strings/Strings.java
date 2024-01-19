package Easy.Strings;

public class Strings {
    public Strings() {

    }

    public static void main(String[] args) {
        Strings a = new Strings();

        String x = "Hello world";
        a.reverseString(x.toCharArray());
        int g = 0;
    }

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
}
