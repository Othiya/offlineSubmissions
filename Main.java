import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // // Asking for user input
        // System.out.print("Enter your name: ");
        // String name = scanner.nextLine();

        // System.out.print("Enter your age: ");
        // int age = scanner.nextInt();

        // // Displaying the input back to the user
        // System.out.println("Hello, " + name + "! You are " + age + " years old.");

        // // Closing the scanner
        // scanner.close();

        // CustomCombo combo = new CustomCombo("Combo2 (Shawarma + Drink)");
        // combo.addFood(new Shawarma());
        // combo.addFood(new Drink());

        Combo1 combo = new Combo1();
        // combo.addFood(new Shawarma());
        // combo.addFood(new Drink());

        CustomCombo c = new CustomCombo("first");
        c.addFood(new Burger());
        c.addFood(new Drink());
        c.addFood(combo);
        c.fullMenu();
        System.err.println(c.calculatePrice());
    }
}
