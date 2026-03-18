import ProductGrid from '../components/ProductGrid';
import CategorySidebar from '../components/CategorySidebar';

const products = [
    { id: 1, title: 'Product 1', description: 'Description 1', price: 10.99, image: 'image1.jpg' },
    { id: 2, title: 'Product 2', description: 'Description 2', price: 9.99, image: 'image2.jpg' },
    { id: 3, title: 'Product 3', description: 'Description 3', price: 12.99, image: 'image3.jpg' },
];

const Homepage = () => {
    return (
        <div>
            <h1>Homepage</h1>
            <div className="home-container">
                <CategorySidebar />
                <ProductGrid products={products} />
            </div>
        </div>
    );
};

export default Homepage;