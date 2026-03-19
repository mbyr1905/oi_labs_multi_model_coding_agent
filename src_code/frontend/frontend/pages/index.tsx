import type { NextPage } from 'next';
import { useState, useEffect } from 'react';
import ProductGrid from '../components/ProductGrid';
import CategorySidebar from '../components/CategorySidebar';
import { api } from '../lib/api';

const HomePage: NextPage = () => {
    const [products, setProducts] = useState([]);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null);

    useEffect(() => {
        const fetchProducts = async () => {
            setLoading(true);
            try {
                const data = await api('products');
                setProducts(data);
            } catch (error) {
                setError(error.message);
            } finally {
                setLoading(false);
            }
        };
        fetchProducts();
    }, []);

    if (loading) return <div>Loading...</div>;
    if (error) return <div>Error: {error}</div>;

    return (
        <>
            <h1>Home Page</h1>
            <div className="flex">
                <CategorySidebar />
                <ProductGrid products={products} />
            </div>
        </>
    );
};

export default HomePage;