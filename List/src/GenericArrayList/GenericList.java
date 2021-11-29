package GenericArrayList;
/**
   * <h1> Generic ArrayList Class <h1>
   * The following class represents a ArrayList that holds generic types.
   * The list is unordered (can be ordered) and supports the following 
   * options such as adding, removing, counting, and grabbing elements, 
   * searching. As well as computing the size of the list, finding its 
   * maximums and minimums and determining if two list equal to each other.
   * Finally, a method to print out the contents of the 
   * list is included.
   * @author Andrew Hoyle
   * @since 11/28/2021
*/

public class GenericList<T extends Comparable<T>> {
	private T[] items;
	// Current number of elements placed into the array
	private int size;
	
	@SuppressWarnings("unchecked")
	public GenericList() {
		this.items = (T[]) new Comparable[10];	
	}
	@SuppressWarnings("unchecked")
	public GenericList(int capacity) {
		if (capacity <= 0) {
			this.items = (T[]) new Comparable[10];
		} else {
			this.items = (T[]) new Comparable[capacity];	
		}
	}
	/**
	   * The .add() method adds an element to the list. If the list is
	   * too small, the list is resized and doubled. After resizing,
	   * the element is then added and the size of elements in the
	   * bag is incremented.
	   * @param element to be added
	 */
	@SuppressWarnings("unchecked")
	public void add(T element) {
		if (this.size >= this.items.length) {
			T[] newItems = (T[]) new Comparable[this.items.length * 2];
			for(int i = 0; i < this.size; i++) {
				newItems[i] = this.items[i];
			}
			this.items = newItems;
		}
		this.items[this.size++] = element;
	}
	/**
	   * The .countOccurances() method takes a value to be search
	   * for in the list, a count is incremented every time that value
	   * is found. Once the search is done, the count is returned.
	   * @param value to be searched and counted
	   * @returns count of the searched value
	*/
	public int countOccurances(T value) {
		int count = 0;
		for (int i = 0; i < this.size; i++) {
			if (this.items[i].compareTo(value) == 0) {
				count++;
			}
		}
		return count;
	}
	/**
	   * The .grab() method locates a element in the bag using its index,
	   * then returns that element. If the index is out of bounds, an exception
	   * is grabbed and an error is output to the screen.
	   * @param index of the element to be returned
	   * @returns element of the passed index or a error is raised
	*/
	public T grab(int index) {
		try {
			return this.items[index];
		} catch (ArrayIndexOutOfBoundsException e) {
			System.out.println("Array out of bounds");
			return null;
		}
	}
	/**
	   * The .find() method attempts to perform a linear search to find
	   * a element in the given list. If its found, it returns true if not,
	   * it returns false.
	   * @param target to be searched for
	   * @returns true if the target is found, else false
	*/
	public boolean find(T target) {
		for (int i = 0; i < this.size; i++) {
			if (this.items[i].compareTo(target) == 0) {
				return true;
			}
		}
		return false;
	}
	
	/**
	   * The .remove() method takes a index to be removed as a
	   * parameter and deletes element at that index. To delete it,
	   * the the loop index starts ahead of the target to be deleted.
	   * The elements after the target index to be removed, is shuffled down,
	   * until the target is at the end of the array. The size is decremented 
	   * and the index value is set to "0", the element is removed.
	   * @param target index to be removed
	*/
	public boolean remove(int target) {
		if (target >= 0 && target < this.size) {
			for (int i = target + 1; i < this.size; i++) {
				this.items[i - 1] = this.items[i];	
			}
			this.items[--this.size] = null;
			return true;
		} else {
			return false;	
		}
	}
	/**
	   * The .size() method returns the current occupied space in the 
	   * bag by elements placed in it.
	   * @returns size of all the elements place into the list
	*/
	public int size() {
		return this.size;
	}
	/**
	   * The .change() method replaces the first occurrence of the passed
	   * "oldVal" in the parameters and replaces it with the "newVal".
	   * @param the old value to be replaced
	   * @param the new value to replace the old value
	   * @returns boolean, true or false
	*/
	public boolean change(T oldVal, T newVal) {
		if (this.size > 0) {
			for (int i = 0; i < this.size; i++) {
				if (this.items[i].compareTo(oldVal) == 0) {
					this.items[i] = newVal;
					return true;
				}
			}
		}
		return false;
	}
	/**
	   * The .max() method searches through the bag for the current largest element,
	   * if the bag is defined with a size equal to 0, returns a trash value. 
	   * @returns current max element in the bag or null
	*/
	public T max() {
		if (this.size == 0) {
			return null;
		}
		T max = this.items[0];
		for (int i = 1; i < this.size; i++) {
			if (this.items[i].compareTo(max) > 0) {
				max = this.items[i];	
			}
		}
		return max;
	}
	/**
	   * The .min() method searchs through the bag for the current smallest element,
	   * if the bag is defined with a size equal to 0, returns a trash value.
	   * @returns current min element in the bag or null
	*/
	public T min() {
		if (this.size == 0) {
			return null;
		}
		T min = this.items[0];
		for (int i = 1; i < size; i++) {
			if (this.items[i].compareTo(min) < 0) {
				min = this.items[i];
			}
		}
		return min;
	}	
	/**
	   * The .equalsTo() method compares two different IntArrayBag objects
	   * to see if they have the same number of elements in each bag (
	   * order does not matter). 
	   * @param IntArrayBag object to be compared
	   * @returns boolean, true or false
	*/
	public boolean equalsTo(GenericList<T> otherBag) {
		if (this.size != otherBag.size()) {
			return false;
		}
		for (int i = 0; i < this.size; i++) {
			if (countOccurances(this.items[i]) != 
				otherBag.countOccurances(this.items[i])) {
				return false;
			}
		}
		return true;
	}
	
	/**
	   * Just a simple .toString() method for the bag
	   * @returns string of bag 
	*/
	public String toString() {
		if (this.size == 0) {
			return "[]";
		}
		String temp = "[";
		for(int i = 0; i < this.size - 1; i++) {
			temp += this.items[i] + ", ";
			if (i % 15 == 0 && i != 0) {
				temp += "\n";	
			}
		}
		return temp + this.items[this.size - 1] + "]";
	}
}
