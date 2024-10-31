public class Burger extends Food {

    public Burger() {
        super("Burger", 300);
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