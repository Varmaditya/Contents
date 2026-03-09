// Program: Store Management System

import java.util.ArrayList;

class Product {

    // Product attributes
    String productName;
    double productPrice;

    // Constructor to initialize product details
    public Product(String productName, double productPrice) {
        this.productName = productName;
        this.productPrice = productPrice;
    }

    // Method to get product details
    public String getProductDetails() {
        return "Product Name: " + productName + ", Price: $" + productPrice;
    }
}

class Store {

    // Store attributes
    int storeID;
    String storeName;
    ArrayList<Product> productList;
    double revenue;

    // Constructor to initialize store details
    public Store(int storeID, String storeName) {
        this.storeID = storeID;
        this.storeName = storeName;
        this.productList = new ArrayList<>();
        this.revenue = 0.0;
    }

    // Method to add a product to the product list
    public void addProduct(Product product) {
        productList.add(product);

        // Add product price to total revenue
        revenue += product.productPrice;
    }

    // Method to calculate and display total revenue
    public double calculateTotalRevenue() {
        return revenue;
    }

    // Method to display store information
    public void displayStoreInfo() {
        System.out.println("Store ID: " + storeID);
        System.out.println("Store Name: " + storeName);
        System.out.println("Product List: ");
        for (Product product : productList) {
            System.out.println(product.getProductDetails());
        }
        System.out.println("Total Revenue: $" + calculateTotalRevenue());
    }
}

public class StoreSystemP89 {
    public static void main(String[] args) {

        // Create products
        Product product1 = new Product("Laptop", 800.00);
        Product product2 = new Product("Smartphone", 500.00);
        Product product3 = new Product("Tablet", 300.00);

        // Create a store
        Store store = new Store(101, "Tech Haven");

        // Add products to the store and update revenue
        store.addProduct(product1);
        store.addProduct(product2);
        store.addProduct(product3);

        // Display store information
        store.displayStoreInfo();
    }
}