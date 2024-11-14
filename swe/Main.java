public class main {
    public static void main(String[] args) {
        Comedy comedy = new Comedy();
        Horror horror = new Horror();
        Thriller thriller = new Thriller();

        User user1 = new User("Sheldon");
        User user2 = new User("Leonerd");

        comedy.register(user2);
        horror.register(user1);

        comedy.notifyObservers("Life is a Joke");
    }

}
