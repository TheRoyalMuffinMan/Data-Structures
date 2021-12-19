package GenericArrayList;
/**
   * <h1> Generic List Main <h1>
   * The following class is just used to showcase the GenericList class.
   * @author Andy
   * @since 11/28/2021 
 */

public class GenericListMain {
	public static void main(String[] args) {
		GenericList<Integer> bag = new GenericList<Integer>();
		GenericList<Integer> sameBag = new GenericList<Integer>();
		GenericList<Integer> differentBag = new GenericList<Integer>(5);
		// Showcasing the .add() feature
		// Adding to bag object
		for (int i = 0; i < 10; i++) {
			bag.add(i);	
		}
		bag.add(2); bag.add(1);
		// Adding to sameBag object
		sameBag.add(1); sameBag.add(4); sameBag.add(3); sameBag.add(6);
		sameBag.add(1); sameBag.add(2); sameBag.add(9); sameBag.add(7);
		sameBag.add(8); sameBag.add(5); sameBag.add(2); sameBag.add(0);
		// Adding to differentBag object
		for (int i = 0; i < 7; i++) {
			differentBag.add(i * i);	
		}
		// Showcasing the.countOccurances() method with bag object
		System.out.println("Bag: " + bag);
		System.out.println("Below is the showcase of the .countOccurances() method.\n"
			               + "left number is the element -> right number is the count"
			               + " of that element.");
		int index = 0;
		for (; index < 9; index++){
			System.out.print(index + "->" + bag.countOccurances(index) + "; ");	
		}
		System.out.println(index + "->" + bag.countOccurances(index));
		// Showcasing the .grab() method with sameBag object
		System.out.println("\nBag #2: " + sameBag);
		System.out.println("Using the .grab() method, at index [6] (count starts at"
			               + " 0): " + sameBag.grab(6));
		// Showcasing the .remove() method with differentBag object
		System.out.println("\nBag #3: " + differentBag);
		System.out.println("Using the .remove() method, at index [4] (count starts "
							+ "at 0). ");
		differentBag.remove(4);
		System.out.println("\nShowing bag #3 after removal: " + differentBag);
		System.out.println("Using the .remove() method, at index [-1] (count starts "
							+ "at 0). ");
		differentBag.remove(-1);
		// Showcasing the .size() method with differentBag object
		System.out.println("Showcasing the .size() method, current size of bag #3: " 
			               + differentBag.size());
		// Showcasing the .change() method with differentBag object
		System.out.println("\nBag #3: " + differentBag);
		System.out.println("Changing value 9 in the bag to -200 using the .change() "
			               + "method");
		System.out.println("Does it work? " + differentBag.change(9, -200));
		System.out.println("Showing bag #3 after change: " + differentBag);
		// Showcasing the .max() and .min() methods with differentBag object
		System.out.println("Using .max(), current maximum element in the bag #3: "
			               + differentBag.max());
		System.out.println("Using .min(), current minimum element in the bag #3: "
			               + differentBag.min());
		// Showcasing the equalsTo() method
		System.out.print("\nBag #1: " + bag);
		System.out.print("\nBag #2: " + sameBag);
		System.out.println("\nBag #3: " + differentBag);
		System.out.println("Using .equalsTo(), does bag #1 equal bag #2? "
							+ bag.equalsTo(sameBag));
		assert differentBag.equalsTo(bag) == false;
		System.out.println("Before Sort: " + bag);
		System.out.println("Size: " + bag.size());
		System.out.println("Find 5: " + bag.find(5));
		System.out.println("Find -3213: " + bag.find(-3213));
		
	}
}
