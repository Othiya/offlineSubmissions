import java.util.Scanner;

public class Main {
    // public static void main(String[] args) {

    // Combo1 combo1 = new Combo1();
    // // System.out.println(combo1.calculatePrice());

    // CompositeCombo c = new CompositeCombo("first");
    // c.addFood(new Burger());
    // c.addFood(combo1);
    // c.addFood(new Combo2());
    // c.removeFood(combo1);
    // c.freeFood(new Wedges());
    // c.getDiscount(0.05);
    // c.fullMenu();
    // System.out.println(c.calculatePrice());

    // }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        while (true) {
            System.out.print("Press 1 to create a combo, 2 to view menu and 0 to exit:");
            int choice = scanner.nextInt();
            scanner.nextLine(); // Consume newline

            if (choice == 0) {
                System.out.println("Exiting...");
                break;
            } else if (choice == 1) {
                createCombo(scanner);
            } else if (choice == 2) {
                System.out.println("MENU: ");
                System.out.println("Burger - 300tk ");
                System.out.println("Fries - 100tk ");
                System.out.println("Wedges - 150tk ");
                System.out.println("Shawarma - 200tk ");
                System.out.println("Drink - 25tk ");
                System.out.println("Combo1 (Burger + Fries + Drink) - 400tk ");
                System.out.println("Combo2 (Shawarma + Drink) - 225tk ");
            } else {
                System.out.println("Invalid choice. Please try again.");
            }
        }
        scanner.close();
    }

    public static void createCombo(Scanner scanner) {
        Burger burger = new Burger();
        Fries fries = new Fries();
        Wedges wedges = new Wedges();
        Shawarma shawarma = new Shawarma();
        Drink drink = new Drink();
        Combo1 combo1 = new Combo1();
        Combo2 combo2 = new Combo2();

        System.out.print("Enter the name of the combo: ");
        String comboName = scanner.nextLine();

        CompositeCombo c = new CompositeCombo(comboName);

        System.out.println("Available commands: Add [item] Remove [item] Free [item] Discount [percentage] Done");
        while (true) {
            String command = scanner.nextLine();
            String[] parts = command.split(" ", 2); // Split into action and item
            String action = parts[0];
            String food = parts[1];

            if (action.equalsIgnoreCase("Add")) {
                if (food.equalsIgnoreCase("Burger")) {
                    c.addFood(burger);
                } else if (food.equalsIgnoreCase("Fries")) {
                    c.addFood(fries);
                } else if (food.equalsIgnoreCase("Wedges")) {
                    c.addFood(wedges);
                } else if (food.equalsIgnoreCase("Shawarma")) {
                    c.addFood(shawarma);
                } else if (food.equalsIgnoreCase("Drink")) {
                    c.addFood(drink);
                } else if (food.equalsIgnoreCase("Combo1")) {
                    c.addFood(combo1);
                } else if (food.equalsIgnoreCase("Combo2")) {
                    c.addFood(combo2);
                }

            } else if (action.equalsIgnoreCase("Remove")) {
                if (food.equalsIgnoreCase("Burger")) {
                    c.removeFood(burger);
                } else if (food.equalsIgnoreCase("Fries")) {
                    c.removeFood(fries);
                } else if (food.equalsIgnoreCase("Wedges")) {
                    c.removeFood(wedges);
                } else if (food.equalsIgnoreCase("Shawarma")) {
                    c.removeFood(shawarma);
                } else if (food.equalsIgnoreCase("Drink")) {
                    c.removeFood(drink);
                } else if (food.equalsIgnoreCase("Combo1")) {
                    c.removeFood(combo1);
                } else if (food.equalsIgnoreCase("Combo2")) {
                    c.removeFood(combo2);
                }
            } else if (action.equalsIgnoreCase("Free")) {
                if (food.equalsIgnoreCase("Burger")) {
                    c.freeFood(burger);
                } else if (food.equalsIgnoreCase("Fries")) {
                    c.freeFood(fries);

                } else if (food.equalsIgnoreCase("Wedges")) {
                    c.freeFood(wedges);

                } else if (food.equalsIgnoreCase("Shawarma")) {
                    c.freeFood(shawarma);

                } else if (food.equalsIgnoreCase("Drink")) {
                    c.freeFood(drink);

                } else if (food.equalsIgnoreCase("Combo1")) {
                    c.freeFood(combo1);

                } else if (food.equalsIgnoreCase("Combo2")) {
                    c.freeFood(combo2);

                }
            } else if (action.equalsIgnoreCase("Discount")) {

                double discount = Double.parseDouble(parts[1]);

                c.getDiscount(discount / 100);
                String done = scanner.nextLine();
                if (done.equalsIgnoreCase("Done")) {
                    c.fullMenu();
                    System.out.println("Discount-" + discount + "%");
                    System.out.println(c.calculatePrice());
                    break;
                }

            } else {
                System.out.println("Invalid command.");
            }
        }

    }
}
