import java.util.ArrayList;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

public class Genre implements Subject {
    ArrayList<Observer> observers;
    String name;
    private ExecutorService executorService;

    Genre(String s) {
        observers = new ArrayList<Observer>();
        name = s;
        executorService = Executors.newCachedThreadPool(); // new Thread when needed,otherwise reuse old available
                                                           // threads
    }

    @Override
    public void register(Observer o) {

        observers.add(o);
    }

    @Override
    public void unregister(Observer o) {

        observers.remove(o);
    }

    // @Override
    // public void notifyObservers(String movie) {

    // for (Observer o : observers) {
    // o.update(movie, name);
    // }
    // }

    @Override
    public void upload(String movie) {
        for (Observer o : observers) {
            executorService.submit(() -> o.update(movie, name)); // each update in a separate thread
        }
    }

    public void shutdown() {
        executorService.shutdown(); // shut down the executor
    }

}
