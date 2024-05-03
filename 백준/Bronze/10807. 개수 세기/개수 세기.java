import java.util.ArrayList;
import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        ArrayList<Integer> numbers = new ArrayList();
        int count = 0;

        for (int i = 0; i < n; i++) {
            numbers.add(sc.nextInt());
        }

        int findNumber = sc.nextInt();

        for (int i = 0; i < n; i++) {
            if(findNumber == numbers.get(i)) {
                count++;
            }
        }

        System.out.println(count);

    }
}
