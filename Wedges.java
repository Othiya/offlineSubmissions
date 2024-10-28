public class Wedges extends Food {
    public Wedges() {
        super("Wedges", 150);
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
