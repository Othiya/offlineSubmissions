public class Shawarma extends Food {
    public Shawarma() {
        super("Shawarma", 200);
    }

    @Override
    public double calculatePrice() {
        return price;
    }
}
