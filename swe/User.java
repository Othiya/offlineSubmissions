public class User extends Observer {
    String name;

    User(String s) {
        name = s;
    }

    // @Override
    // public void update(String movie, String genre_name) {
    // System.out.println();
    // System.out.println(name + "--" + movie + "--" + " added in your favourite
    // genre " + "-" + genre_name);
    // }

    // with Thread Sleep
    // @Override
    // public void update(String movie, String genre_name) {
    // try {
    // // Sleep for 2 seconds (2000 milliseconds)
    // Thread.sleep(2000);

    // // Print notification message after the delay
    // System.out.println();
    // System.out.println(name + "--" + movie + "--" + " added in your favourite
    // genre " + "-" + genre_name);
    // } catch (InterruptedException e) {
    // // Handle the InterruptedException (restore interrupted status)
    // Thread.currentThread().interrupt();
    // System.out.println("Notification interrupted: " + e.getMessage());
    // }
    // }

    // with thread number

    @Override
    public void update(String movie, String genre_name) {
        System.out.println(
                name + " -- " + movie + " -- added in your favourite genre - " + genre_name +
                        " [Handled by Thread: " + Thread.currentThread().getName() + "]");
    }

}