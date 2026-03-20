import type { NextPage } from 'next';
import { useState, useEffect } from 'react';
import { api } from '../lib/api';
import ProductGrid from '../components/ProductGrid';
import CategorySidebar from '../components/CategorySidebar';

const HomePage: NextPage = () => {
  const [products, setProducts] = useState([]);
  const [categories, setCategories] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchProducts = async () => {
      setLoading(true);
      try {
        const productsResponse = await api('http://localhost:8000/products');
        setProducts(productsResponse);
      } catch (error) {
        setError(error);
      } finally {
        setLoading(false);
      }
    };
    const fetchCategories = async () => {
      setLoading(true);
      try {
        const categoriesResponse = await api('http://localhost:8000/categories');
        setCategories(categoriesResponse);
      } catch (error) {
        setError(error);
      } finally {
        setLoading(false);
      }
    };
    fetchProducts();
    fetchCategories();
  }, []);

  if (loading) {
    return <div>Loading...</div>;
  }

  if (error) {
    return <div>Error: {error.message}</div>;
  }

  return (
    <>
      <CategorySidebar categories={categories} />
      <ProductGrid products={products} />
    </>
  );
};

export default HomePage;