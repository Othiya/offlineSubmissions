import java.util.ArrayList;

public class Horror implements Genre {
    ArrayList<Observer> observers;
    String name;

    Horror() {
        observers = new ArrayList<Observer>();
        name = "Horror";
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
