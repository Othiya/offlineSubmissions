public class User extends Observer {
    String name;

    User(String s) {
        name = s;
    }

    @Override
    public void update(String movie, String genre_name) {
        System.out.println();
        System.out.println(name + "--" + movie + "--" + " added in your favourite genre " + "-" + genre_name);
    }

    // does multithreading work?

    // @Override
    // public void update(String movie, String genre_name) {
    // System.out.println(
    // name + " -- " + movie + " -- added in your favourite genre - " + genre_name +
    // " [Handled by Thread: " + Thread.currentThread().getName() + "]");
    // }

}