/**
 * @author     Crispin Stichart
 * @version    0.01
 * @since      2015-01-27
 */

class fizzbuzz {
/**
 * Hey, at least it compiles.
 */
    public static void print(String thing) {
        System.out.println(thing);
    }

    public static void main(String[] args) {
        for (int i = 0; i<=100; i++) {
            String s = "";
            if ((i % 3) == 0) {
                s = s + "Fizz";
            }
            if ((i % 5) == 0) {
                s = s + "Buzz";
            }
            if (((i % 3) != 0) && ((i % 5) != 0)) {
                s = "" + i;
            }
            print(s + "");
        }

    }
}