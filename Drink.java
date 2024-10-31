public class Drink extends Food {
    public Drink() {
        super("Drink", 25);
    }

    @Override
    public double calculatePrice() {
        return price;
    }

    @Override
    public String getName() {
        return name;
    }

}
