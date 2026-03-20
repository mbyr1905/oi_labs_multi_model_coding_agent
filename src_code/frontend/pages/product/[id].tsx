import type { NextPage, GetServerSideProps } from 'next';
import { useState, useEffect } from 'react';
import { api } from '../lib/api';
import { useRouter } from 'next/router';

const ProductPage: NextPage = () => {
  const [product, setProduct] = useState({});
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const router = useRouter();
  const id = router.query.id;

  useEffect(() => {
    const fetchProduct = async () => {
      setLoading(true);
      try {
        const productResponse = await api(`http://localhost:8000/products/${id}`);
        setProduct(productResponse);
      } catch (error) {
        setError(error);
      } finally {
        setLoading(false);
      }
    };
    fetchProduct();
  }, [id]);

  if (loading) {
    return <div>Loading...</div>;
  }

  if (error) {
    return <div>Error: {error.message}</div>;
  }

  return (
    <div>
      <h1>{product.name}</h1>
      <p>{product.description}</p>
      <p>{product.price}</p>
    </div>
  );
};

export const getServerSideProps: GetServerSideProps = async () => {
  return {
    props: {},
  };
};

export default ProductPage;