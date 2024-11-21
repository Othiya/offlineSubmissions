public interface Subject {

    void register(Observer o);

    void unregister(Observer o);

    void upload(String movie);

}
