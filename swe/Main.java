import java.util.Scanner;

public class main {
    public static void main(String[] args) {

        Genre comedy = new Genre("Comedy");
        Genre horror = new Genre("Horror");
        Genre thriller = new Genre("Thriller");

        User user1 = new User("Sheldon");
        User user2 = new User("Leonard");

        // Users subscribe to genres
        comedy.register(user1);
        horror.register(user2);
        thriller.register(user1);
        thriller.register(user2);

        // Upload movie and notify observers asynchronously
        comedy.upload("The Hitchhiker's Guide to the Galaxy");
        thriller.upload("Star Wars");
        thriller.upload("Inception");

        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter your name: ");
        String name = scanner.nextLine();

        User user3 = new User(name);

        while (true) {
            System.out.println("1. Subscribe to a genre");
            System.out.println("2. Unsubscribe from a genre");
            System.out.println("3. Upload a movie");
            System.out.println("4. Exit");
            System.out.print("Enter your choice: ");
            int choice = scanner.nextInt();
            scanner.nextLine(); // Consume newline

            switch (choice) {
                case 1:
                    // Subscribe a user to a genre
                    System.out.print("Enter genre to subscribe (Thriller, Horror, Comedy): ");
                    String subscribe = scanner.nextLine();
                    if (subscribe.equalsIgnoreCase("Comedy")) {
                        comedy.register(user3);
                    } else if (subscribe.equalsIgnoreCase("Thriller")) {
                        thriller.register(user3);
                    } else {
                        horror.register(user3);
                    }
                    break;

                case 2:
                    // Unsubscribe a user from a genre
                    System.out.print("Enter genre to unsubscribe (Thriller, Horror, Comedy): ");
                    String unsubscribe = scanner.nextLine();
                    if (unsubscribe.equalsIgnoreCase("Comedy")) {
                        comedy.unregister(user3);
                    } else if (unsubscribe.equalsIgnoreCase("Thriller")) {
                        thriller.unregister(user3);
                    } else {
                        horror.unregister(user3);
                    }
                    break;

                case 3:
                    // Upload a movie and notify users
                    System.out.print("Enter the genre of the movie (Thriller, Horror, Comedy): ");
                    String genre = scanner.nextLine();
                    System.out.print("Enter the name of the movie: ");
                    String movie = scanner.nextLine();

                    if (genre.equalsIgnoreCase("Comedy")) {
                        comedy.upload(movie);
                    } else if (genre.equalsIgnoreCase("Thriller")) {
                        thriller.upload(movie);
                    } else {
                        horror.upload(movie);
                    }
                    break;

                case 4:
                    // Exit the program
                    System.out.println("Exiting...");
                    scanner.close();
                    // Shut down the executors after the loop ends
                    try {
                        Thread.sleep(2000); // Wait to allow all notifications to complete
                    } catch (InterruptedException e) {
                        e.printStackTrace();
                    }

                    // Shut down the executors
                    comedy.shutdown();
                    horror.shutdown();
                    thriller.shutdown();
                    return;
                default:
                    System.out.println("Invalid choice! Try again.");
            }
        }
    }
}
