import type { NextPage } from 'next';
import { useState, useEffect } from 'react';
import CartItem from '../components/CartItem';
import { api } from '../lib/api';

const CartPage: NextPage = () => {
    const [cartItems, setCartItems] = useState([]);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null);

    useEffect(() => {
        const fetchCartItems = async () => {
            setLoading(true);
            try {
                const data = await api('cart');
                setCartItems(data);
            } catch (error) {
                setError(error.message);
            } finally {
                setLoading(false);
            }
        };
        fetchCartItems();
    }, []);

    if (loading) return <div>Loading...</div>;
    if (error) return <div>Error: {error}</div>;

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