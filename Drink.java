public class Drink implements Combo {

    @Override
    public double calculatePrice() {
        return 25;
    }

    @Override
    public String getName() {
        return "Drink";
    }

}
