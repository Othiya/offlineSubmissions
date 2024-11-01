import java.util.ArrayList;

public class CompositeCombo implements Combo {
    String name;
    ArrayList<Combo> combos;
    // ArrayList<Combo> freeFood;
    // double discount;

    public CompositeCombo(String name) {
        this.name = name;
        combos = new ArrayList<>();
        // freeFood = new ArrayList<>();
        // discount = 0;

    }

    public void addFood(Combo combo) {
        combos.add(combo);
    }

    public void removeFood(Combo combo) {
        combos.remove(combo);
    }

    // public void freeFood(Combo combo) {
    // freeFood.add(combo);
    // }

    // public void getDiscount(double dis) {
    // this.discount = dis;
    // }

    public void fullMenu() {
        for (Combo combo : combos) {
            System.out.println(combo.getName());
        }
    }

    @Override
    public double calculatePrice() {
        double sum = 0;
        for (Combo combo : combos) {
            sum += combo.calculatePrice();
        }

        return sum;
    }

    @Override
    public String getName() {
        return name;
    }

}
