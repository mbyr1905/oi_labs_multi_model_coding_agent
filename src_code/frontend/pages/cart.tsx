import CartItem from '../components/CartItem';
import OrderSummary from '../components/OrderSummary';

const cartItems = [
    { id: 1, title: 'Product 1', description: 'Description 1', price: 10.99, image: 'image1.jpg', quantity: 2 },
    { id: 2, title: 'Product 2', description: 'Description 2', price: 9.99, image: 'image2.jpg', quantity: 1 },
];

const CartPage = () => {
    return (
        <div>
            <h1>Cart Page</h1>
            <div className="cart-container">
                {cartItems.map((item) => (
                    <CartItem key={item.id} product={item} />
                ))}
                <OrderSummary products={cartItems} />
            </div>
        </div>
    );
};

export default CartPage;