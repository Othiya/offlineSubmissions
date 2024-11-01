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

        Combo1 combo = new Combo1();

        CompositeCombo c = new CompositeCombo("first");
        c.addFood(new Burger());
        c.addFood(new Shawarma());
        c.addFood(combo);
        Combo c2 = new FreeCombo(new Drink());
        c.addFood(c2);
        c.fullMenu();
        Combo cFinal = new DiscountCombo(c, 0.10);

        System.err.println(cFinal.calculatePrice());
    }
}
