import type { NextPage } from 'next';
import { useState, useEffect } from 'react';
import { api } from '../lib/api';
import CartItem from '../components/CartItem';

const CartPage: NextPage = () => {
  const [cartItems, setCartItems] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchCartItems = async () => {
      setLoading(true);
      try {
        const cartItemsResponse = await api('http://localhost:8000/cart');
        setCartItems(cartItemsResponse);
      } catch (error) {
        setError(error);
      } finally {
        setLoading(false);
      }
    };
    fetchCartItems();
  }, []);

  if (loading) {
    return <div>Loading...</div>;
  }

  if (error) {
    return <div>Error: {error.message}</div>;
  }

  return (
    <>
      <h1>Cart</h1>
      {cartItems.map((item) => (
        <CartItem key={item.id} item={item} />
      ))}
    </>
  );
};

export default CartPage;