public interface Genre {

    void register(Observer o);

    void unregister(Observer o);

    void notifyObservers(String movie);

}
