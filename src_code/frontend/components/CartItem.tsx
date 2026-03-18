import { useState } from 'react';

const CartItem = ({ product }) => {
    const [quantity, setQuantity] = useState(1);

    const handleQuantityChange = (e) => {
        setQuantity(e.target.value);
    };

    return (
        <div className="cart-item">
            <img src={product.image} alt={product.title} />
            <div className="cart-item-info">
                <h2>{product.title}</h2>
                <p>Quantity: {quantity}</p>
                <input type="number" value={quantity} onChange={handleQuantityChange} />
                <p>Subtotal: ${product.price * quantity}</p>
            </div>
        </div>
    );
};

export default CartItem;