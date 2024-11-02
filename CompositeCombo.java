import java.util.ArrayList;

public class CompositeCombo implements Combo {
    String name;
    ArrayList<Combo> combos;
    ArrayList<Combo> freeFood;
    double discount;

    public CompositeCombo(String name) {
        this.name = name;
        combos = new ArrayList<>();
        freeFood = new ArrayList<>();
        discount = 0;

    }

    public void addFood(Combo combo) {
        // System.out.println(String.format("%s Added", combo.getName()));
        combos.add(combo);
    }

    public void removeFood(Combo combo) {
        combos.remove(combo);
    }

    public void freeFood(Combo combo) {
        freeFood.add(combo);
    }

    public void getDiscount(double dis) {
        this.discount = dis;
    }

    public void fullMenu() {
        System.out.print("Your Combo:");
        System.out.println(name);
        for (Combo combo : combos) {
            System.out.println(combo.getName());
        }
        for (Combo combo : freeFood) {
            System.out.println(String.format("%s (Free!!!)", combo.getName()));

        }

        System.out.println("Total-" + calculatePriceWithoutDiscount());
    }

    public double calculatePriceWithoutDiscount() {
        double sum = 0;
        for (Combo combo : combos) {
            sum += combo.calculatePrice();

        }

        for (Combo combo : freeFood) {
            sum += combo.calculatePrice();
        }

        return sum;
    }

    @Override
    public double calculatePrice() {
        double sum = 0;
        for (Combo combo : combos) {
            sum += combo.calculatePrice();

        }

        // for (Combo combo : freeFood) {
        // sum -= combo.calculatePrice();
        // }

        // System.out.println(sum);
        // System.out.println(sum * discount);
        sum -= (sum * discount);
        return sum;
    }

    @Override
    public String getName() {
        return name;
    }

}
