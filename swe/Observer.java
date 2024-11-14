public abstract class Observer {
    protected Genre genre;

    public abstract void update(String movie, String genre_name);

}