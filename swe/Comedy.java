import java.util.ArrayList;

public class Comedy implements Genre {
    ArrayList<Observer> observers;
    String name;

    Comedy() {
        observers = new ArrayList<Observer>();
        name = "Comedy";
    }

    @Override
    public void register(Observer o) {

        observers.add(o);
    }

    @Override
    public void unregister(Observer o) {

        observers.remove(o);
    }

    @Override
    public void notifyObservers(String movie) {

        for (Observer o : observers) {
            o.update(movie, name);
        }
    }

}